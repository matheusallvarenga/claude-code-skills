# Full-Stack Project Finisher

A specialized skill designed to help developers take projects from 70% complete to production-ready. This skill excels at gap analysis, task decomposition, and providing actionable guidance to complete incomplete projects.

## Purpose

This skill addresses the common "Builder's Abundance" pattern - brilliant project starts that need help reaching completion. It provides:

- **Gap Analysis** - Identifies incomplete work, missing tests, documentation gaps
- **Task Decomposition** - Breaks large goals into actionable 2-hour sprints
- **Tech Stack Optimization** - Suggests best tools and patterns for specific needs
- **Database Design** - Helps design schemas with best practices
- **API Blueprint Generation** - Creates OpenAPI specs before coding
- **Testing Strategy** - Builds comprehensive test plans
- **Deployment Readiness** - Ensures production-ready deployments

## When to Use This Skill

Activate this skill when:

- Starting a new full-stack project that needs proper architecture
- A project is 50-80% complete but stalled
- You need to assess what's missing before deployment
- Designing databases or APIs for a new feature
- Planning testing strategy for better coverage
- Preparing a project for production deployment

## Core Capabilities

### 1. Project Gap Analysis

The skill can scan your project and identify:
- Incomplete features (TODOs, FIXMEs, commented code)
- Missing or inadequate tests
- Outdated or missing documentation
- Security vulnerabilities and configuration issues
- Missing error handling
- Database migration gaps
- Deployment blockers

**Usage:**
```bash
python scripts/analyze_project_gaps.py /path/to/project
```

### 2. Database Schema Design

Provides PostgreSQL-optimized schema designs with:
- Proper normalization and relationships
- Strategic indexing for performance
- Audit trail patterns
- Soft delete implementations
- UUID vs incremental ID guidance

**Usage:**
```bash
python scripts/generate_db_schema.py --requirements "requirements.txt" --output schema.sql
```

### 3. API Blueprint Generation

Creates OpenAPI 3.0 specifications including:
- RESTful endpoint design
- Request/response schemas
- Error handling patterns
- Authentication/authorization flows
- Rate limiting strategies

**Usage:**
```bash
python scripts/create_openapi_spec.py --endpoints "endpoints.yaml" --output api-spec.yaml
```

### 4. Test Coverage Analysis

Analyzes test coverage and suggests:
- Missing unit tests for critical functions
- Integration test scenarios
- E2E test flows
- Coverage improvement priorities

**Usage:**
```bash
python scripts/test_coverage_report.py /path/to/project
```

## Reference Documentation

The skill includes curated best practices documentation:

- **database_design_patterns.md** - PostgreSQL best practices, normalization, indexing strategies
- **api_design_patterns.md** - REST API standards, versioning, error handling
- **testing_strategies.md** - Testing pyramid, coverage goals, integration patterns
- **deployment_checklist.md** - Production readiness requirements

## Project Templates

Ready-to-use boilerplates for common stacks:

### Node.js + Express + PostgreSQL
```
assets/backend-templates/node-express-postgres/
├── src/
│   ├── config/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── middleware/
│   ├── services/
│   └── utils/
├── tests/
├── package.json
└── tsconfig.json
```

### Python + FastAPI + PostgreSQL
```
assets/backend-templates/fastapi-postgres/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   └── services/
├── tests/
└── requirements.txt
```

## CI/CD Templates

GitHub Actions workflows for:
- Automated testing on PR
- Code quality checks (linting, type checking)
- Database migrations
- Docker builds
- Deployment automation

## Tech Stack Expertise

This skill has deep knowledge of:

**Backend:**
- Node.js + TypeScript + Express
- Python + FastAPI
- PostgreSQL (schemas, indexes, queries, migrations)
- RESTful API design
- Authentication (JWT, OAuth2)

**Testing:**
- Jest/Vitest (JavaScript/TypeScript)
- pytest (Python)
- Integration testing patterns
- E2E testing with Playwright/Cypress
- Test coverage analysis

**DevOps:**
- Docker & docker-compose
- GitHub Actions CI/CD
- Environment configuration
- Deployment strategies
- Monitoring and logging

## Workflow Integration

This skill integrates seamlessly with:
- Your existing Claude Code setup
- Session-based workflow patterns
- Git-based development
- Documentation-driven development
- Notion (when integration enabled)

## Example Workflows

### Complete a Stalled Project

1. Run gap analysis: `python scripts/analyze_project_gaps.py .`
2. Review prioritized gaps
3. Create task breakdown for top 3 gaps
4. Implement fixes with proper tests
5. Re-run analysis to verify completion
6. Deploy with confidence

### Start a New Full-Stack Feature

1. Define feature requirements
2. Design database schema: `python scripts/generate_db_schema.py`
3. Create API specification: `python scripts/create_openapi_spec.py`
4. Implement backend endpoints
5. Write comprehensive tests
6. Run coverage analysis
7. Deploy to staging

### Prepare for Production

1. Run full project gap analysis
2. Review deployment checklist
3. Fix security and configuration issues
4. Ensure test coverage > 80%
5. Set up CI/CD pipeline
6. Create monitoring/logging
7. Deploy!

## Best Practices

When using this skill, follow these guidelines:

1. **Always Start with Analysis** - Understand what's missing before coding
2. **Design Before Implementation** - Schema and API specs first
3. **Test as You Build** - Don't leave testing for the end
4. **Document Decisions** - Keep ADRs (Architecture Decision Records)
5. **Incremental Progress** - 2-hour focused sprints work best
6. **Validate Frequently** - Re-run analysis after major changes

## Customization

You can customize this skill by:

- Adding project-specific patterns to references/
- Creating custom templates in assets/
- Extending scripts for your tech stack
- Adding team-specific best practices

## Support and Issues

For questions or issues with this skill:
- Review the reference documentation
- Check script help: `python scripts/<script>.py --help`
- Consult Claude Code documentation
- Open an issue in the skill repository

---

**Remember:** This skill is designed to help you finish projects, not start them. Use it when you have a clear vision but need help with execution and completion.
