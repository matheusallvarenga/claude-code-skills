# Deployment Checklist

Complete checklist to ensure your application is production-ready before deployment.

## Table of Contents

1. [Pre-Deployment](#pre-deployment)
2. [Security](#security)
3. [Performance](#performance)
4. [Monitoring & Logging](#monitoring--logging)
5. [Database](#database)
6. [Infrastructure](#infrastructure)
7. [Documentation](#documentation)
8. [Testing](#testing)
9. [Deployment Process](#deployment-process)
10. [Post-Deployment](#post-deployment)

---

## Pre-Deployment

### Code Quality

- [ ] All code reviewed and approved
- [ ] No TODO or FIXME comments in critical paths
- [ ] Code follows project style guide
- [ ] All linting errors resolved
- [ ] Type checking passes (TypeScript/mypy/etc.)
- [ ] No console.log or print statements in production code
- [ ] Dead code removed
- [ ] Dependencies updated to stable versions
- [ ] No security vulnerabilities in dependencies (`npm audit`, `pip-audit`)

### Configuration

- [ ] Environment variables documented
- [ ] `.env.example` file created and up-to-date
- [ ] `.env` file NOT committed to version control
- [ ] `.gitignore` properly configured
- [ ] All sensitive data stored in environment variables or secrets manager
- [ ] Different configurations for dev/staging/production
- [ ] Feature flags configured correctly
- [ ] API endpoints point to production URLs
- [ ] Database connection strings correct for production

---

## Security

### Authentication & Authorization

- [ ] Passwords hashed with bcrypt/argon2 (not MD5 or SHA1)
- [ ] JWT tokens expire after reasonable time (15min - 1 hour)
- [ ] Refresh tokens implemented
- [ ] Password reset flow secure (time-limited tokens)
- [ ] Account lockout after failed login attempts
- [ ] Role-based access control (RBAC) implemented
- [ ] No hardcoded credentials anywhere

### API Security

- [ ] HTTPS enabled and enforced (redirect HTTP to HTTPS)
- [ ] CORS configured properly (not `*` in production)
- [ ] Rate limiting implemented
- [ ] Input validation on all endpoints
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS protection (sanitize user input)
- [ ] CSRF protection for state-changing operations
- [ ] API authentication required where needed
- [ ] Sensitive data not exposed in error messages

### Headers & Certificates

- [ ] Security headers configured:
  ```
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  X-XSS-Protection: 1; mode=block
  Content-Security-Policy: default-src 'self'
  Referrer-Policy: no-referrer
  ```
- [ ] SSL/TLS certificate valid and not expiring soon
- [ ] Certificate auto-renewal configured (Let's Encrypt)
- [ ] TLS 1.2+ only (disable TLS 1.0 and 1.1)

### Data Protection

- [ ] Sensitive data encrypted at rest
- [ ] Sensitive data encrypted in transit (HTTPS)
- [ ] PII (Personally Identifiable Information) properly handled
- [ ] GDPR compliance (if applicable)
- [ ] Data retention policy implemented
- [ ] Backup encryption enabled
- [ ] File upload validation (type, size, content)
- [ ] No sensitive data in logs
- [ ] Database credentials rotated regularly

---

## Performance

### Backend Optimization

- [ ] Database queries optimized (no N+1 queries)
- [ ] Indexes created for frequently queried columns
- [ ] Slow query logging enabled and monitored
- [ ] Connection pooling configured
- [ ] Caching strategy implemented (Redis/Memcached)
- [ ] Response compression enabled (gzip/brotli)
- [ ] Pagination implemented for large datasets
- [ ] Heavy operations moved to background jobs
- [ ] API response times < 200ms for common endpoints

### Frontend Optimization

- [ ] Bundle size optimized (code splitting, tree shaking)
- [ ] Images optimized and lazy-loaded
- [ ] CDN configured for static assets
- [ ] Browser caching configured
- [ ] Lighthouse score > 90
- [ ] Critical CSS inlined
- [ ] JavaScript minified and compressed
- [ ] Unused JavaScript removed

### Scalability

- [ ] Horizontal scaling possible (stateless application)
- [ ] Load balancer configured
- [ ] Auto-scaling rules defined
- [ ] Database read replicas (if needed)
- [ ] Queue system for async tasks (Bull, Celery, etc.)
- [ ] CDN for static content

---

## Monitoring & Logging

### Application Monitoring

- [ ] Error tracking configured (Sentry, Rollbar, etc.)
- [ ] Application Performance Monitoring (APM) set up (New Relic, DataDog)
- [ ] Uptime monitoring configured (Pingdom, UptimeRobot)
- [ ] Custom metrics tracked (business KPIs)
- [ ] Alerting rules configured
- [ ] On-call rotation established

### Logging

- [ ] Structured logging implemented (JSON format)
- [ ] Log levels properly set (debug/info/warn/error)
- [ ] Centralized logging (ELK, Splunk, CloudWatch)
- [ ] Request/response logging (without sensitive data)
- [ ] Error stack traces captured
- [ ] Log retention policy defined
- [ ] Logs searchable and filterable
- [ ] Correlation IDs for request tracking

### Health Checks

- [ ] `/health` endpoint implemented
- [ ] `/health/db` for database connectivity
- [ ] `/health/redis` for cache connectivity
- [ ] `/metrics` endpoint for Prometheus (if using)
- [ ] Health checks integrated with load balancer
- [ ] Kubernetes liveness probe configured (if using K8s)
- [ ] Kubernetes readiness probe configured (if using K8s)

---

## Database

### Schema & Migrations

- [ ] All migrations tested
- [ ] Migrations are reversible (down migrations)
- [ ] Migration order documented
- [ ] Schema changes backward compatible
- [ ] No breaking changes to existing data
- [ ] Foreign key constraints in place
- [ ] Indexes created for performance

### Backups & Recovery

- [ ] Automated backups configured
- [ ] Backup frequency appropriate (daily/hourly)
- [ ] Backup retention policy defined
- [ ] Backups tested and restorable
- [ ] Point-in-time recovery (PITR) enabled
- [ ] Disaster recovery plan documented
- [ ] RTO (Recovery Time Objective) defined
- [ ] RPO (Recovery Point Objective) defined

### Performance

- [ ] Slow query log enabled
- [ ] Query performance profiled
- [ ] Indexes optimized
- [ ] Unused indexes removed
- [ ] Connection pool size configured
- [ ] Database monitoring enabled
- [ ] Query timeout configured

---

## Infrastructure

### Server Configuration

- [ ] Server timezone set to UTC
- [ ] Server time synchronized (NTP)
- [ ] Firewall rules configured
- [ ] SSH access restricted (key-based, no password)
- [ ] Unnecessary services disabled
- [ ] System updates automated
- [ ] Fail2ban or similar configured

### Container/Orchestration

- [ ] Docker images optimized (multi-stage builds)
- [ ] Container security scanned (Trivy, Snyk)
- [ ] Resource limits defined (CPU, memory)
- [ ] Health checks configured
- [ ] Secrets managed properly (not in Dockerfile)
- [ ] Image registry secure and private
- [ ] Container restart policy configured

### DNS & Networking

- [ ] DNS records configured
- [ ] TTL values appropriate
- [ ] CDN configured
- [ ] DDoS protection enabled
- [ ] WebSocket support (if needed)
- [ ] IPv6 support (if applicable)

---

## Documentation

### Technical Documentation

- [ ] README.md comprehensive
- [ ] Architecture diagram created
- [ ] API documentation complete (OpenAPI/Swagger)
- [ ] Environment variables documented
- [ ] Setup instructions clear
- [ ] Troubleshooting guide available
- [ ] Runbooks for common operations

### Operational Documentation

- [ ] Deployment process documented
- [ ] Rollback procedure documented
- [ ] Incident response plan
- [ ] On-call procedures
- [ ] Escalation paths defined
- [ ] Maintenance windows scheduled
- [ ] Change management process

### End-User Documentation

- [ ] User guide created
- [ ] FAQ section
- [ ] Known issues documented
- [ ] Support contact information
- [ ] Terms of Service
- [ ] Privacy Policy

---

## Testing

### Test Coverage

- [ ] Unit tests passing (>80% coverage)
- [ ] Integration tests passing
- [ ] E2E tests passing
- [ ] Load testing completed
- [ ] Security testing (OWASP Top 10)
- [ ] Penetration testing (for critical systems)
- [ ] Accessibility testing (WCAG compliance)

### Staging Environment

- [ ] Staging environment mirrors production
- [ ] All features tested in staging
- [ ] Database migrations tested in staging
- [ ] Performance tested in staging
- [ ] Third-party integrations tested
- [ ] Email/SMS delivery tested

---

## Deployment Process

### Pre-Deployment

- [ ] Deployment plan created
- [ ] Team notified of deployment
- [ ] Maintenance window scheduled (if downtime expected)
- [ ] Rollback plan ready
- [ ] Database backup taken immediately before deployment
- [ ] Feature flags disabled (if releasing behind flags)

### Deployment Steps

- [ ] Code tagged with version number
- [ ] Build artifacts created
- [ ] Environment variables updated
- [ ] Database migrations run
- [ ] Application deployed
- [ ] Cache cleared
- [ ] CDN cache invalidated (if needed)
- [ ] Health checks passing
- [ ] Smoke tests run

### Zero-Downtime Deployment

- [ ] Rolling deployment strategy
- [ ] Blue-green deployment configured
- [ ] Canary releases possible
- [ ] Database migrations backward compatible
- [ ] Old and new versions can run simultaneously

---

## Post-Deployment

### Verification

- [ ] Application accessible at production URL
- [ ] All critical features tested manually
- [ ] Smoke tests automated and passing
- [ ] Error rates normal in monitoring
- [ ] Response times normal
- [ ] Database connections healthy
- [ ] Cache hit rates normal
- [ ] Background jobs processing

### Monitoring

- [ ] Monitor error rates for 2-4 hours
- [ ] Monitor performance metrics
- [ ] Check log aggregation for errors
- [ ] Verify alerts working correctly
- [ ] Review user feedback channels
- [ ] Monitor server resources (CPU, memory, disk)

### Communication

- [ ] Stakeholders notified of successful deployment
- [ ] Status page updated
- [ ] Release notes published
- [ ] Changelog updated
- [ ] Social media announcement (if applicable)

### Rollback Plan

If issues detected:

1. [ ] Assess severity of issue
2. [ ] Decide: fix forward or rollback?
3. [ ] If rollback:
   - [ ] Deploy previous version
   - [ ] Restore database backup (if needed)
   - [ ] Verify rollback successful
   - [ ] Notify stakeholders
4. [ ] If fix forward:
   - [ ] Create hotfix
   - [ ] Test hotfix
   - [ ] Deploy hotfix
   - [ ] Verify fix successful

---

## Compliance & Legal

- [ ] GDPR compliance (if handling EU data)
- [ ] CCPA compliance (if handling CA data)
- [ ] HIPAA compliance (if healthcare data)
- [ ] PCI-DSS compliance (if handling payments)
- [ ] Terms of Service reviewed by legal
- [ ] Privacy Policy reviewed by legal
- [ ] Cookie consent implemented (if applicable)
- [ ] Data processing agreements signed

---

## Production-Ready Checklist Summary

### Critical (Must Have)

- ✅ HTTPS enabled
- ✅ Environment variables configured
- ✅ Database backups automated
- ✅ Error tracking configured
- ✅ Health checks implemented
- ✅ Logs centralized
- ✅ Authentication secure
- ✅ Rate limiting enabled
- ✅ All tests passing

### Important (Should Have)

- ✅ Monitoring and alerting
- ✅ CDN configured
- ✅ Caching strategy
- ✅ API documentation
- ✅ Rollback plan
- ✅ Load testing completed
- ✅ Security headers configured

### Nice to Have

- ✅ Auto-scaling
- ✅ Blue-green deployments
- ✅ Feature flags
- ✅ A/B testing framework
- ✅ Performance budgets

---

## Quick Reference Commands

### Check SSL Certificate
```bash
openssl s_client -connect example.com:443 -servername example.com < /dev/null | openssl x509 -noout -dates
```

### Test Database Connection
```bash
psql -h your-db-host -U username -d database_name -c "SELECT 1;"
```

### Check Open Ports
```bash
nmap -p- your-server-ip
```

### Test Rate Limiting
```bash
for i in {1..100}; do curl https://api.example.com/endpoint; done
```

### Check Response Headers
```bash
curl -I https://example.com
```

### Test Load Balancer
```bash
for i in {1..10}; do curl https://api.example.com/health; done
```

### Monitor Real-Time Logs
```bash
tail -f /var/log/app/production.log | jq .
```

---

## Tools & Resources

### Security
- [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/)
- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/)
- [SecurityHeaders.com](https://securityheaders.com/)

### Performance
- [WebPageTest](https://www.webpagetest.org/)
- [Google Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [GTmetrix](https://gtmetrix.com/)

### Monitoring
- [Sentry](https://sentry.io/)
- [DataDog](https://www.datadoghq.com/)
- [New Relic](https://newrelic.com/)
- [Prometheus](https://prometheus.io/)

### Deployment
- [GitHub Actions](https://github.com/features/actions)
- [GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
- [AWS CodePipeline](https://aws.amazon.com/codepipeline/)
- [Vercel](https://vercel.com/)
- [Railway](https://railway.app/)

---

## Emergency Contacts

Before deployment, ensure team has:

- [ ] On-call engineer contact
- [ ] Database administrator contact
- [ ] Infrastructure team contact
- [ ] Product manager contact
- [ ] Communication plan for incidents

---

**Remember:** It's better to delay deployment than to deploy something not ready for production!
