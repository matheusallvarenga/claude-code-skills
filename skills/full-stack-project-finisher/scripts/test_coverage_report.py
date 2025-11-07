#!/usr/bin/env python3
"""
Test Coverage Report Generator
Analyzes test coverage and suggests missing tests for better quality assurance.
Works with multiple testing frameworks and provides actionable insights.
"""
import os
import sys
import re
import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple


class TestCoverageAnalyzer:
    """Analyzes test coverage and suggests improvements."""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path).resolve()
        self.source_files = []
        self.test_files = []
        self.coverage_data = defaultdict(dict)

        # Testing patterns
        self.test_patterns = {'test', 'spec', '__tests__', 'tests', '.test.', '.spec.'}
        self.test_extensions = {'.test.js', '.test.ts', '.test.jsx', '.test.tsx',
                                '.spec.js', '.spec.ts', '.spec.jsx', '.spec.tsx',
                                '_test.py', '_test.go', '.test.rb'}

        # Code extensions
        self.code_extensions = {'.js', '.ts', '.jsx', '.tsx', '.py', '.java', '.go', '.rs', '.rb'}

        # Directories to skip
        self.skip_dirs = {'node_modules', 'venv', 'env', '.git', 'dist', 'build', '__pycache__',
                          '.next', 'coverage', 'out', 'target'}

        # Patterns for finding testable code
        self.function_pattern = re.compile(
            r'(?:export\s+)?(?:async\s+)?(?:function|def|fn|func)\s+(\w+)|'
            r'(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s+)?\(|'
            r'(\w+)\s*:\s*(?:async\s+)?\(',
            re.MULTILINE
        )
        self.class_pattern = re.compile(r'class\s+(\w+)', re.MULTILINE)
        self.method_pattern = re.compile(
            r'(?:async\s+)?(\w+)\s*\([^)]*\)\s*{|'
            r'def\s+(\w+)\s*\(',
            re.MULTILINE
        )

    def analyze(self) -> Dict:
        """Run complete test coverage analysis."""
        print(f"🧪 Analyzing test coverage: {self.project_path}")
        print("=" * 80)

        self._identify_files()
        self._analyze_coverage()
        self._suggest_missing_tests()
        self._check_test_quality()

        return self._generate_report()

    def _identify_files(self):
        """Identify source and test files."""
        print("\n📂 Identifying source and test files...")

        for root, dirs, files in os.walk(self.project_path):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if d not in self.skip_dirs]

            for file in files:
                file_path = Path(root) / file

                # Check if it's a code file
                if file_path.suffix not in self.code_extensions:
                    continue

                # Check if it's a test file
                is_test = (
                    any(pattern in str(file_path).lower() for pattern in self.test_patterns) or
                    any(file.endswith(ext) for ext in self.test_extensions)
                )

                if is_test:
                    self.test_files.append(file_path)
                else:
                    # Exclude config files
                    if not any(skip in file.lower() for skip in ['config', 'setup', '.config.']):
                        self.source_files.append(file_path)

        print(f"   📄 Source files: {len(self.source_files)}")
        print(f"   🧪 Test files: {len(self.test_files)}")

    def _analyze_coverage(self):
        """Analyze which source files have corresponding tests."""
        print("\n🔍 Analyzing test coverage...")

        for source_file in self.source_files:
            relative_path = source_file.relative_to(self.project_path)
            self.coverage_data[str(relative_path)] = {
                'has_test': False,
                'test_files': [],
                'functions': [],
                'classes': [],
                'complexity': 'low'
            }

            # Extract functions and classes
            try:
                with open(source_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                    # Find functions
                    functions = []
                    for match in self.function_pattern.finditer(content):
                        func_name = match.group(1) or match.group(2) or match.group(3)
                        if func_name and not func_name.startswith('_'):
                            functions.append(func_name)

                    # Find classes
                    classes = [match.group(1) for match in self.class_pattern.finditer(content)]

                    self.coverage_data[str(relative_path)]['functions'] = functions
                    self.coverage_data[str(relative_path)]['classes'] = classes

                    # Estimate complexity
                    complexity = self._estimate_complexity(content)
                    self.coverage_data[str(relative_path)]['complexity'] = complexity

            except Exception as e:
                print(f"   ⚠️  Error reading {relative_path}: {e}")

            # Find corresponding test files
            source_name = source_file.stem
            for test_file in self.test_files:
                test_name = test_file.stem
                # Remove test suffixes
                test_name_clean = re.sub(r'\.(test|spec)$', '', test_name)
                test_name_clean = re.sub(r'_(test|spec)$', '', test_name_clean)

                if source_name in test_name or test_name_clean in source_name:
                    self.coverage_data[str(relative_path)]['has_test'] = True
                    self.coverage_data[str(relative_path)]['test_files'].append(
                        str(test_file.relative_to(self.project_path))
                    )

    def _estimate_complexity(self, content: str) -> str:
        """Estimate code complexity based on control structures."""
        control_structures = len(re.findall(
            r'\b(if|else|elif|for|while|switch|case|try|catch|except)\b',
            content
        ))

        functions = len(self.function_pattern.findall(content))
        classes = len(self.class_pattern.findall(content))

        # Simple heuristic
        score = control_structures + (functions * 2) + (classes * 3)

        if score < 10:
            return 'low'
        elif score < 30:
            return 'medium'
        else:
            return 'high'

    def _suggest_missing_tests(self):
        """Suggest tests for uncovered code."""
        print("\n💡 Suggesting missing tests...")

        self.suggestions = []

        for file_path, data in self.coverage_data.items():
            if not data['has_test']:
                priority = self._calculate_priority(data)

                suggestion = {
                    'file': file_path,
                    'priority': priority,
                    'complexity': data['complexity'],
                    'functions': data['functions'][:5],  # Show first 5
                    'classes': data['classes'],
                    'reason': self._get_priority_reason(data, priority)
                }

                self.suggestions.append(suggestion)

        # Sort by priority
        priority_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
        self.suggestions.sort(key=lambda x: priority_order[x['priority']])

    def _calculate_priority(self, data: Dict) -> str:
        """Calculate test priority for a file."""
        complexity = data['complexity']
        num_functions = len(data['functions'])
        num_classes = len(data['classes'])

        # Critical: High complexity with classes or many functions
        if complexity == 'high' or (num_classes > 0 and num_functions > 3):
            return 'critical'

        # High: Medium complexity with classes or several functions
        if complexity == 'medium' or num_classes > 0 or num_functions > 5:
            return 'high'

        # Medium: Some functions
        if num_functions > 2:
            return 'medium'

        # Low: Simple files
        return 'low'

    def _get_priority_reason(self, data: Dict, priority: str) -> str:
        """Get human-readable reason for priority."""
        reasons = []

        if data['complexity'] == 'high':
            reasons.append("high complexity")

        if len(data['classes']) > 0:
            reasons.append(f"{len(data['classes'])} class(es)")

        if len(data['functions']) > 5:
            reasons.append(f"{len(data['functions'])} functions")

        if not reasons:
            return "Standard testing recommended"

        return f"Contains {', '.join(reasons)}"

    def _check_test_quality(self):
        """Check quality of existing tests."""
        print("\n📊 Checking test quality...")

        self.test_quality = {
            'total_tests': len(self.test_files),
            'test_patterns': defaultdict(int),
            'issues': []
        }

        for test_file in self.test_files:
            try:
                with open(test_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                    # Count test patterns
                    describe_count = len(re.findall(r'\bdescribe\(', content))
                    it_count = len(re.findall(r'\b(?:it|test)\(', content))
                    expect_count = len(re.findall(r'\bexpect\(', content))
                    assert_count = len(re.findall(r'\bassert', content))

                    self.test_quality['test_patterns']['describe'] += describe_count
                    self.test_quality['test_patterns']['it/test'] += it_count
                    self.test_quality['test_patterns']['expect'] += expect_count
                    self.test_quality['test_patterns']['assert'] += assert_count

                    # Check for test quality issues
                    if it_count == 0 and assert_count == 0:
                        self.test_quality['issues'].append({
                            'file': str(test_file.relative_to(self.project_path)),
                            'issue': 'No test cases found',
                            'severity': 'high'
                        })

                    if it_count > 0 and expect_count == 0 and assert_count == 0:
                        self.test_quality['issues'].append({
                            'file': str(test_file.relative_to(self.project_path)),
                            'issue': 'Tests without assertions',
                            'severity': 'high'
                        })

                    # Check for only tests (no implementation)
                    if len(content) < 100:
                        self.test_quality['issues'].append({
                            'file': str(test_file.relative_to(self.project_path)),
                            'issue': 'Very short test file (< 100 chars)',
                            'severity': 'medium'
                        })

            except Exception as e:
                print(f"   ⚠️  Error reading test file {test_file}: {e}")

    def _generate_report(self) -> Dict:
        """Generate final coverage report."""
        print("\n" + "=" * 80)
        print("📊 TEST COVERAGE REPORT")
        print("=" * 80)

        # Calculate statistics
        total_files = len(self.source_files)
        covered_files = sum(1 for data in self.coverage_data.values() if data['has_test'])
        coverage_ratio = (covered_files / total_files * 100) if total_files > 0 else 0

        # Print statistics
        print(f"\n📈 Coverage Statistics:")
        print(f"   Total source files: {total_files}")
        print(f"   Files with tests: {covered_files}")
        print(f"   Files without tests: {total_files - covered_files}")
        print(f"   Coverage ratio: {coverage_ratio:.1f}%")

        # Coverage level assessment
        print(f"\n🎯 Coverage Level: ", end='')
        if coverage_ratio >= 80:
            print("🟢 Excellent (≥80%)")
        elif coverage_ratio >= 60:
            print("🟡 Good (60-79%)")
        elif coverage_ratio >= 40:
            print("🟠 Fair (40-59%)")
        else:
            print("🔴 Needs Improvement (<40%)")

        # Print test quality
        print(f"\n🧪 Test Quality:")
        print(f"   Total test files: {self.test_quality['total_tests']}")
        print(f"   Test cases: {self.test_quality['test_patterns']['it/test']}")
        print(f"   Assertions: {self.test_quality['test_patterns']['expect'] + self.test_quality['test_patterns']['assert']}")

        if self.test_quality['issues']:
            print(f"\n⚠️  Test Quality Issues ({len(self.test_quality['issues'])} found):")
            for issue in self.test_quality['issues'][:5]:
                print(f"      • {issue['file']}: {issue['issue']} [{issue['severity']}]")
            if len(self.test_quality['issues']) > 5:
                print(f"      ... and {len(self.test_quality['issues']) - 5} more")

        # Print missing test suggestions
        if self.suggestions:
            print(f"\n💡 Missing Test Suggestions (Top 10):")

            # Group by priority
            by_priority = defaultdict(list)
            for suggestion in self.suggestions:
                by_priority[suggestion['priority']].append(suggestion)

            for priority in ['critical', 'high', 'medium', 'low']:
                if by_priority[priority]:
                    emoji = {'critical': '🔴', 'high': '🟠', 'medium': '🟡', 'low': '⚪'}
                    print(f"\n   {emoji[priority]} {priority.upper()} Priority:")

                    for suggestion in by_priority[priority][:10]:
                        print(f"      • {suggestion['file']}")
                        print(f"        Reason: {suggestion['reason']}")
                        if suggestion['functions']:
                            funcs_str = ', '.join(suggestion['functions'][:3])
                            print(f"        Functions: {funcs_str}{'...' if len(suggestion['functions']) > 3 else ''}")

        # Recommendations
        print(f"\n✅ Recommendations:")
        self._print_recommendations(coverage_ratio)

        return {
            'coverage': {
                'total_files': total_files,
                'covered_files': covered_files,
                'coverage_ratio': f"{coverage_ratio:.1f}%"
            },
            'test_quality': dict(self.test_quality),
            'suggestions': self.suggestions,
            'timestamp': self._get_timestamp()
        }

    def _print_recommendations(self, coverage_ratio: float):
        """Print actionable recommendations."""
        recommendations = []

        if coverage_ratio < 40:
            recommendations.append("   1. 🎯 Start with critical priority files (high complexity, multiple classes)")
            recommendations.append("   2. 📝 Set a goal of 60% coverage as first milestone")
            recommendations.append("   3. 🧪 Focus on unit tests for individual functions first")
        elif coverage_ratio < 60:
            recommendations.append("   1. 🎯 Address high priority files next")
            recommendations.append("   2. 📝 Aim for 80% coverage target")
            recommendations.append("   3. 🔗 Add integration tests for critical workflows")
        elif coverage_ratio < 80:
            recommendations.append("   1. 🎯 Address remaining medium priority files")
            recommendations.append("   2. 🧪 Add edge case tests to existing test suites")
            recommendations.append("   3. 📊 Set up coverage tracking in CI/CD")
        else:
            recommendations.append("   1. ✨ Excellent coverage! Maintain it with CI/CD checks")
            recommendations.append("   2. 🔗 Consider adding E2E tests for critical user flows")
            recommendations.append("   3. 🧪 Review test quality issues if any")

        if self.test_quality['issues']:
            recommendations.append(f"   {len(recommendations) + 1}. ⚠️  Fix {len(self.test_quality['issues'])} test quality issues")

        for rec in recommendations:
            print(rec)

    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        from datetime import datetime
        return datetime.now().isoformat()


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python test_coverage_report.py <project_path>")
        print("\nExample:")
        print("  python test_coverage_report.py /path/to/my-project")
        print("  python test_coverage_report.py .")
        sys.exit(1)

    project_path = sys.argv[1]

    if not os.path.exists(project_path):
        print(f"❌ Error: Project path does not exist: {project_path}")
        sys.exit(1)

    analyzer = TestCoverageAnalyzer(project_path)
    report = analyzer.analyze()

    # Optionally save report to file
    if len(sys.argv) > 2 and sys.argv[2] == '--save':
        output_file = Path(project_path) / 'test-coverage-report.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        print(f"\n💾 Report saved to: {output_file}")


if __name__ == '__main__':
    main()
