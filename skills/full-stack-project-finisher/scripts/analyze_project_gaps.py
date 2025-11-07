#!/usr/bin/env python3
"""
Project Gap Analyzer
Scans a project directory to identify incomplete work, missing components,
and areas that need attention before production deployment.
"""
import os
import sys
import re
import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple

class ProjectGapAnalyzer:
    """Analyzes a project to identify gaps and incomplete work."""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path).resolve()
        self.gaps = defaultdict(list)
        self.stats = {
            'total_files': 0,
            'files_with_todos': 0,
            'total_todos': 0,
            'test_files': 0,
            'missing_tests': [],
            'security_issues': 0,
            'documentation_gaps': 0
        }

        # Patterns to search for
        self.todo_pattern = re.compile(r'(TODO|FIXME|XXX|HACK|BUG):\s*(.+)', re.IGNORECASE)
        self.commented_code_pattern = re.compile(r'^\s*[#//]\s*[a-zA-Z_].*\(.*\)', re.MULTILINE)

        # Extensions to scan
        self.code_extensions = {'.js', '.ts', '.jsx', '.tsx', '.py', '.java', '.go', '.rs', '.rb', '.php'}
        self.test_patterns = {'test', 'spec', '__tests__', 'tests'}

        # Directories to skip
        self.skip_dirs = {'node_modules', 'venv', 'env', '.git', 'dist', 'build', '__pycache__', '.next', 'coverage'}

    def analyze(self) -> Dict:
        """Run complete project analysis."""
        print(f"🔍 Analyzing project: {self.project_path}")
        print("=" * 80)

        self._scan_for_todos()
        self._analyze_test_coverage()
        self._check_documentation()
        self._check_security_configs()
        self._check_error_handling()
        self._check_database_migrations()

        return self._generate_report()

    def _scan_for_todos(self):
        """Scan for TODO, FIXME, and similar markers."""
        print("\n📝 Scanning for incomplete work markers...")

        for file_path in self._get_code_files():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.stats['total_files'] += 1

                    # Find TODOs
                    todos = self.todo_pattern.findall(content)
                    if todos:
                        self.stats['files_with_todos'] += 1
                        self.stats['total_todos'] += len(todos)
                        relative_path = file_path.relative_to(self.project_path)
                        for marker, description in todos:
                            self.gaps['incomplete_work'].append({
                                'file': str(relative_path),
                                'type': marker,
                                'description': description.strip(),
                                'priority': self._assess_todo_priority(marker, description)
                            })

                    # Find commented code blocks (potential incomplete work)
                    commented_blocks = len(self.commented_code_pattern.findall(content))
                    if commented_blocks > 3:  # More than 3 commented functions/methods
                        self.gaps['commented_code'].append({
                            'file': str(file_path.relative_to(self.project_path)),
                            'blocks': commented_blocks
                        })

            except Exception as e:
                print(f"⚠️  Error reading {file_path}: {e}")

    def _analyze_test_coverage(self):
        """Analyze test coverage and identify missing tests."""
        print("\n🧪 Analyzing test coverage...")

        source_files = set()
        test_files = set()

        for file_path in self._get_code_files():
            relative_path = file_path.relative_to(self.project_path)
            path_str = str(relative_path)

            if any(pattern in path_str.lower() for pattern in self.test_patterns):
                test_files.add(relative_path)
                self.stats['test_files'] += 1
            else:
                source_files.add(relative_path)

        # Find source files without corresponding test files
        for source_file in source_files:
            has_test = False
            for test_file in test_files:
                # Check if test file name relates to source file
                source_name = source_file.stem
                if source_name in str(test_file):
                    has_test = True
                    break

            if not has_test:
                # Skip config files and entry points
                if not any(skip in str(source_file).lower() for skip in ['config', 'index', 'main', 'app']):
                    self.gaps['missing_tests'].append(str(source_file))
                    self.stats['missing_tests'].append(str(source_file))

        coverage_ratio = len(test_files) / len(source_files) if source_files else 0
        self.stats['test_coverage_ratio'] = f"{coverage_ratio:.1%}"

    def _check_documentation(self):
        """Check for documentation gaps."""
        print("\n📚 Checking documentation...")

        docs_to_check = ['README.md', 'API.md', 'CONTRIBUTING.md', 'CHANGELOG.md']
        for doc in docs_to_check:
            doc_path = self.project_path / doc
            if not doc_path.exists():
                self.gaps['missing_docs'].append(doc)
                self.stats['documentation_gaps'] += 1
            elif doc == 'README.md' and doc_path.exists():
                # Check if README is substantial
                with open(doc_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if len(content) < 500:  # Less than 500 chars is probably insufficient
                        self.gaps['insufficient_docs'].append({
                            'file': doc,
                            'issue': 'README is too brief (< 500 characters)'
                        })

    def _check_security_configs(self):
        """Check for security-related configuration issues."""
        print("\n🔒 Checking security configurations...")

        # Check for .env.example
        if not (self.project_path / '.env.example').exists():
            if (self.project_path / '.env').exists():
                self.gaps['security'].append({
                    'issue': 'Missing .env.example file',
                    'severity': 'medium',
                    'recommendation': 'Create .env.example with placeholder values'
                })
                self.stats['security_issues'] += 1

        # Check if .env is in .gitignore
        gitignore_path = self.project_path / '.gitignore'
        if gitignore_path.exists():
            with open(gitignore_path, 'r', encoding='utf-8') as f:
                gitignore_content = f.read()
                if '.env' not in gitignore_content:
                    self.gaps['security'].append({
                        'issue': '.env not in .gitignore',
                        'severity': 'high',
                        'recommendation': 'Add .env to .gitignore immediately'
                    })
                    self.stats['security_issues'] += 1

        # Check for hardcoded secrets
        secret_patterns = [
            (r'password\s*=\s*["\'][^"\']{3,}["\']', 'Possible hardcoded password'),
            (r'api[_-]?key\s*=\s*["\'][^"\']{10,}["\']', 'Possible hardcoded API key'),
            (r'secret\s*=\s*["\'][^"\']{10,}["\']', 'Possible hardcoded secret'),
        ]

        for file_path in self._get_code_files():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    for pattern, description in secret_patterns:
                        if re.search(pattern, content, re.IGNORECASE):
                            self.gaps['security'].append({
                                'file': str(file_path.relative_to(self.project_path)),
                                'issue': description,
                                'severity': 'high'
                            })
                            self.stats['security_issues'] += 1
            except Exception:
                pass

    def _check_error_handling(self):
        """Check for basic error handling patterns."""
        print("\n⚠️  Checking error handling...")

        for file_path in self._get_code_files():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                    # Check for try-catch or error handling
                    has_try_catch = bool(re.search(r'\b(try|catch|except|rescue)\b', content))
                    has_functions = bool(re.search(r'(function|def|fn)\s+\w+', content))

                    # If file has functions but no error handling, flag it
                    if has_functions and not has_try_catch and len(content) > 500:
                        # Don't flag test files
                        if not any(pattern in str(file_path).lower() for pattern in self.test_patterns):
                            self.gaps['error_handling'].append({
                                'file': str(file_path.relative_to(self.project_path)),
                                'issue': 'No apparent error handling'
                            })
            except Exception:
                pass

    def _check_database_migrations(self):
        """Check for database migration files and patterns."""
        print("\n🗄️  Checking database setup...")

        migration_dirs = ['migrations', 'db/migrations', 'database/migrations', 'prisma/migrations']
        has_migrations = False

        for migration_dir in migration_dirs:
            dir_path = self.project_path / migration_dir
            if dir_path.exists() and dir_path.is_dir():
                has_migrations = True
                migration_files = list(dir_path.glob('*'))
                if len(migration_files) == 0:
                    self.gaps['database'].append({
                        'issue': f'Empty migrations directory: {migration_dir}',
                        'recommendation': 'Create initial migration or remove empty directory'
                    })

        # Check for database config files
        db_config_files = ['knexfile.js', 'ormconfig.json', 'prisma/schema.prisma', 'database.yml']
        has_db_config = any((self.project_path / config).exists() for config in db_config_files)

        if has_db_config and not has_migrations:
            self.gaps['database'].append({
                'issue': 'Database config exists but no migrations found',
                'recommendation': 'Set up database migrations'
            })

    def _assess_todo_priority(self, marker: str, description: str) -> str:
        """Assess priority of TODO items."""
        high_priority_keywords = ['critical', 'urgent', 'security', 'bug', 'broken', 'fix asap']
        medium_priority_keywords = ['important', 'should', 'refactor']

        description_lower = description.lower()
        marker_lower = marker.lower()

        if marker_lower in ['fixme', 'bug'] or any(kw in description_lower for kw in high_priority_keywords):
            return 'high'
        elif marker_lower in ['hack', 'xxx'] or any(kw in description_lower for kw in medium_priority_keywords):
            return 'medium'
        else:
            return 'low'

    def _get_code_files(self) -> List[Path]:
        """Get all code files in the project."""
        code_files = []
        for root, dirs, files in os.walk(self.project_path):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if d not in self.skip_dirs]

            for file in files:
                file_path = Path(root) / file
                if file_path.suffix in self.code_extensions:
                    code_files.append(file_path)

        return code_files

    def _generate_report(self) -> Dict:
        """Generate final analysis report."""
        print("\n" + "=" * 80)
        print("📊 ANALYSIS COMPLETE")
        print("=" * 80)

        # Summary statistics
        print(f"\n📈 Statistics:")
        print(f"   Total files scanned: {self.stats['total_files']}")
        print(f"   Files with TODOs: {self.stats['files_with_todos']}")
        print(f"   Total TODO markers: {self.stats['total_todos']}")
        print(f"   Test files: {self.stats['test_files']}")
        print(f"   Test coverage ratio: {self.stats.get('test_coverage_ratio', 'N/A')}")
        print(f"   Security issues: {self.stats['security_issues']}")
        print(f"   Documentation gaps: {self.stats['documentation_gaps']}")

        # Priority gaps
        print(f"\n🚨 High Priority Gaps:")
        self._print_priority_gaps()

        # Detailed gaps
        if self.gaps:
            print(f"\n📋 Detailed Gap Analysis:")
            for category, items in self.gaps.items():
                if items:
                    print(f"\n   {category.replace('_', ' ').title()} ({len(items)} issues):")
                    for item in items[:5]:  # Show first 5 of each category
                        if isinstance(item, dict):
                            print(f"      • {json.dumps(item, indent=8)}")
                        else:
                            print(f"      • {item}")
                    if len(items) > 5:
                        print(f"      ... and {len(items) - 5} more")

        print(f"\n✅ Next Steps:")
        self._print_recommendations()

        return {
            'stats': self.stats,
            'gaps': dict(self.gaps),
            'timestamp': self._get_timestamp()
        }

    def _print_priority_gaps(self):
        """Print high-priority gaps that need immediate attention."""
        priorities = []

        # High priority incomplete work
        if 'incomplete_work' in self.gaps:
            high_priority_todos = [item for item in self.gaps['incomplete_work'] if item['priority'] == 'high']
            if high_priority_todos:
                priorities.append(f"   • {len(high_priority_todos)} high-priority TODOs/FIXMEs")

        # Security issues
        if self.gaps.get('security'):
            priorities.append(f"   • {len(self.gaps['security'])} security configuration issues")

        # Missing critical docs
        if 'README.md' in self.gaps.get('missing_docs', []):
            priorities.append("   • Missing README.md")

        # Low test coverage
        if len(self.stats.get('missing_tests', [])) > 10:
            priorities.append(f"   • {len(self.stats['missing_tests'])} files without tests")

        if priorities:
            for priority in priorities:
                print(priority)
        else:
            print("   ✅ No critical gaps found!")

    def _print_recommendations(self):
        """Print actionable recommendations."""
        recommendations = []

        # Security first
        if self.gaps.get('security'):
            recommendations.append("   1. 🔒 Fix security issues (review .env, .gitignore, hardcoded secrets)")

        # Documentation
        if self.gaps.get('missing_docs') or self.gaps.get('insufficient_docs'):
            recommendations.append("   2. 📚 Complete documentation (README, API docs, CONTRIBUTING)")

        # Complete TODOs
        if self.stats['total_todos'] > 0:
            recommendations.append(f"   3. ✏️  Address {self.stats['total_todos']} TODO markers")

        # Improve tests
        if len(self.stats.get('missing_tests', [])) > 0:
            recommendations.append("   4. 🧪 Improve test coverage (add tests for uncovered files)")

        # Error handling
        if self.gaps.get('error_handling'):
            recommendations.append("   5. ⚠️  Add error handling to critical functions")

        # Database migrations
        if self.gaps.get('database'):
            recommendations.append("   6. 🗄️  Set up or fix database migrations")

        if recommendations:
            for rec in recommendations:
                print(rec)
        else:
            print("   🎉 Project looks production-ready!")

    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        from datetime import datetime
        return datetime.now().isoformat()


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python analyze_project_gaps.py <project_path>")
        print("\nExample:")
        print("  python analyze_project_gaps.py /path/to/my-project")
        print("  python analyze_project_gaps.py .")
        sys.exit(1)

    project_path = sys.argv[1]

    if not os.path.exists(project_path):
        print(f"❌ Error: Project path does not exist: {project_path}")
        sys.exit(1)

    analyzer = ProjectGapAnalyzer(project_path)
    report = analyzer.analyze()

    # Optionally save report to file
    if len(sys.argv) > 2 and sys.argv[2] == '--save':
        output_file = Path(project_path) / 'gap-analysis-report.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        print(f"\n💾 Report saved to: {output_file}")


if __name__ == '__main__':
    main()
