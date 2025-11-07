# Full-Stack Project Finisher

A comprehensive Claude Code skill designed to help developers take projects from 70% complete to production-ready. This skill provides tools, scripts, and best practices documentation to identify gaps, design systems, and finish incomplete projects.

## Overview

This skill addresses the common "Builder's Abundance" pattern - many excellent project starts that need help reaching completion. It's designed for developers who are brilliant at architecture and design but need assistance with the execution phase.

## Features

### 🔍 Gap Analysis
- Scans projects for incomplete work (TODOs, FIXMEs)
- Identifies missing tests and documentation
- Detects security issues and configuration problems
- Analyzes code complexity and suggests priorities

### 🗄️ Database Design
- Generates PostgreSQL schemas with best practices
- Includes proper normalization, indexes, and constraints
- Implements audit trails and soft deletes
- Provides migration-ready SQL

### 🌐 API Blueprint Generation
- Creates OpenAPI 3.0 specifications
- Implements RESTful design patterns
- Includes authentication, pagination, and error handling
- Generates complete CRUD endpoints

### 🧪 Test Coverage Analysis
- Identifies files without tests
- Calculates coverage ratios
- Suggests test priorities based on complexity
- Validates test quality

### 📚 Best Practices Documentation
- Database design patterns
- API design standards
- Testing strategies
- Deployment checklists

## Installation

### Using Claude Code

1. Install the skill:
   ```bash
   # Copy the skill to your Claude Code directory
   cp -r . ~/.claude/skills/full-stack-project-finisher
   ```

2. Verify installation:
   ```bash
   ls ~/.claude/skills/full-stack-project-finisher
   ```

3. Invoke the skill in Claude Code:
   ```
   Use the full-stack-project-finisher skill to analyze my project
   ```

### Manual Setup

If using the scripts independently:

```bash
# Clone the repository
git clone https://github.com/yourusername/full-stack-project-finisher.git
cd full-stack-project-finisher

# Make scripts executable
chmod +x scripts/*.py

# Run a script
python3 scripts/analyze_project_gaps.py /path/to/your/project
```

## Usage

### Analyzing Project Gaps

```bash
python3 scripts/analyze_project_gaps.py /path/to/project

# Save report to file
python3 scripts/analyze_project_gaps.py /path/to/project --save
```

**Output:**
- Total files scanned
- Files with TODOs/FIXMEs
- Test coverage ratio
- Security issues found
- Prioritized action items

### Generating Database Schema

```bash
# Create sample requirements file
python3 scripts/generate_db_schema.py --create-sample requirements.yaml

# Edit requirements.yaml to define your schema

# Generate schema
python3 scripts/generate_db_schema.py -r requirements.yaml -o schema.sql
```

**Features:**
- UUID or SERIAL primary keys
- Audit trail columns (created_at, updated_at)
- Soft delete support
- Foreign key relationships
- Strategic indexes
- Check constraints

### Creating API Specification

```bash
# Generate sample OpenAPI spec
python3 scripts/create_openapi_spec.py --sample -o api-spec.yaml

# View in Swagger Editor
# Upload api-spec.yaml to https://editor.swagger.io/
```

**Includes:**
- Complete CRUD endpoints
- Authentication flows
- Pagination and filtering
- Error responses
- Request/response schemas

### Analyzing Test Coverage

```bash
python3 scripts/test_coverage_report.py /path/to/project

# Save detailed report
python3 scripts/test_coverage_report.py /path/to/project --save
```

**Provides:**
- Coverage statistics
- Missing test suggestions prioritized by complexity
- Test quality issues
- Actionable recommendations

## Best Practices Documentation

### [Database Design Patterns](references/database_design_patterns.md)
- Normalization strategies
- Indexing best practices
- UUID vs SERIAL primary keys
- Audit trails and soft deletes
- Performance optimization
- Common patterns and anti-patterns

### [API Design Patterns](references/api_design_patterns.md)
- RESTful principles
- URL structure and naming conventions
- HTTP methods and status codes
- Authentication and authorization
- Versioning strategies
- Rate limiting and caching

### [Testing Strategies](references/testing_strategies.md)
- Testing pyramid
- Unit, integration, and E2E testing
- Test coverage goals
- Mocking and stubbing
- CI/CD integration
- Tools and frameworks

### [Deployment Checklist](references/deployment_checklist.md)
- Pre-deployment verification
- Security configuration
- Performance optimization
- Monitoring and logging
- Database readiness
- Post-deployment validation

## Project Templates

### CI/CD Pipeline
- GitHub Actions workflow for Node.js + PostgreSQL
- Automated testing (unit, integration, E2E)
- Security audits
- Docker image builds
- Deployment automation

Location: `assets/ci-cd-templates/github-actions-nodejs.yml`

### Docker Development Environment
- PostgreSQL database
- Redis caching
- Database management UI (Adminer)
- Redis management UI
- Email testing (Mailhog)

Location: `assets/docker-compose.example.yml`

### Environment Configuration
- Complete .env.example template
- Database configuration
- Authentication settings
- External API integrations
- Feature flags

Location: `assets/.env.example`

## Example Workflows

### 1. Complete a Stalled Project

```bash
# Step 1: Analyze gaps
python3 scripts/analyze_project_gaps.py .

# Step 2: Review prioritized gaps
# (Critical TODOs, security issues, missing tests)

# Step 3: Create task breakdown
# Focus on top 3 critical gaps

# Step 4: Implement fixes with tests

# Step 5: Re-run analysis
python3 scripts/analyze_project_gaps.py . --save

# Step 6: Deploy with confidence
```

### 2. Start a New Feature

```bash
# Step 1: Design database schema
python3 scripts/generate_db_schema.py --create-sample feature-schema.yaml
# Edit feature-schema.yaml
python3 scripts/generate_db_schema.py -r feature-schema.yaml -o feature.sql

# Step 2: Create API specification
python3 scripts/create_openapi_spec.py --sample -o feature-api.yaml
# Customize feature-api.yaml

# Step 3: Implement feature

# Step 4: Write tests

# Step 5: Check coverage
python3 scripts/test_coverage_report.py .

# Step 6: Deploy
```

### 3. Prepare for Production

```bash
# Step 1: Run full analysis
python3 scripts/analyze_project_gaps.py . --save

# Step 2: Review deployment checklist
cat references/deployment_checklist.md

# Step 3: Fix security issues
# (Review gap analysis security section)

# Step 4: Ensure test coverage > 80%
python3 scripts/test_coverage_report.py .

# Step 5: Set up CI/CD
cp assets/ci-cd-templates/github-actions-nodejs.yml .github/workflows/

# Step 6: Deploy!
```

## Tech Stack Expertise

This skill has deep knowledge of:

**Backend:**
- Node.js + TypeScript + Express
- Python + FastAPI
- PostgreSQL (schemas, indexes, queries, migrations)
- RESTful API design
- JWT authentication

**Testing:**
- Jest/Vitest (JavaScript/TypeScript)
- pytest (Python)
- Playwright/Cypress (E2E)
- Integration testing patterns

**DevOps:**
- Docker & docker-compose
- GitHub Actions CI/CD
- Environment configuration
- Deployment strategies

## Requirements

### Python Scripts
- Python 3.8+
- No external dependencies for basic scripts
- Optional: `pyyaml` for YAML support

```bash
pip install pyyaml
```

### Development
- Node.js 18+ (for templates)
- PostgreSQL 14+ (for database work)
- Docker (for containerized development)

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Update documentation
5. Submit a pull request

## License

MIT License - feel free to use this skill in your projects.

## Credits

Created as part of the Claude Code skill ecosystem to help developers finish what they start.

---

## Quick Start

```bash
# 1. Analyze your project
python3 scripts/analyze_project_gaps.py .

# 2. Generate database schema
python3 scripts/generate_db_schema.py --sample

# 3. Create API specification
python3 scripts/create_openapi_spec.py --sample -o api.yaml

# 4. Check test coverage
python3 scripts/test_coverage_report.py .

# 5. Review best practices
cat references/deployment_checklist.md
```

---

**Remember:** This skill is designed to help you finish projects, not start them. Use it when you have a clear vision but need help with execution and completion.