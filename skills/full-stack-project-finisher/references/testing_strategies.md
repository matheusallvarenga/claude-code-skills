# Testing Strategies

Comprehensive guide to testing strategies, best practices, and achieving high code coverage.

## Table of Contents

1. [Testing Pyramid](#testing-pyramid)
2. [Unit Testing](#unit-testing)
3. [Integration Testing](#integration-testing)
4. [End-to-End Testing](#end-to-end-testing)
5. [Test Coverage](#test-coverage)
6. [Testing Patterns](#testing-patterns)
7. [Mocking & Stubbing](#mocking--stubbing)
8. [Testing Best Practices](#testing-best-practices)
9. [CI/CD Integration](#cicd-integration)
10. [Tools & Frameworks](#tools--frameworks)

## Testing Pyramid

```
        /\
       /  \         E2E Tests (Few)
      /    \        - Test complete user flows
     /------\       - Slow, expensive, brittle
    /        \
   /   Integration Tests (Some)
  /    - Test module interactions
 /     - Medium speed, moderate cost
/______________________________\
         Unit Tests (Many)
    - Test individual functions
    - Fast, cheap, reliable
```

### Ideal Distribution

- **70%** Unit Tests
- **20%** Integration Tests
- **10%** E2E Tests

### Why This Distribution?

1. **Unit tests** are fast and pinpoint failures precisely
2. **Integration tests** catch component interaction issues
3. **E2E tests** validate real user scenarios but are slow and fragile

## Unit Testing

### What to Test

Test individual functions, classes, or methods in isolation.

### Characteristics

- **Fast**: Run in milliseconds
- **Isolated**: No external dependencies
- **Deterministic**: Same input = same output
- **Focused**: One concept per test

### Example (Jest/TypeScript)

```typescript
// users.service.ts
export class UsersService {
  validateEmail(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  hashPassword(password: string): string {
    // Simplified for example
    return Buffer.from(password).toString('base64');
  }
}

// users.service.test.ts
import { UsersService } from './users.service';

describe('UsersService', () => {
  let service: UsersService;

  beforeEach(() => {
    service = new UsersService();
  });

  describe('validateEmail', () => {
    it('should return true for valid email', () => {
      expect(service.validateEmail('user@example.com')).toBe(true);
    });

    it('should return false for email without @', () => {
      expect(service.validateEmail('userexample.com')).toBe(false);
    });

    it('should return false for email without domain', () => {
      expect(service.validateEmail('user@')).toBe(false);
    });

    it('should return false for empty string', () => {
      expect(service.validateEmail('')).toBe(false);
    });
  });

  describe('hashPassword', () => {
    it('should return hashed password', () => {
      const hashed = service.hashPassword('password123');
      expect(hashed).toBeDefined();
      expect(hashed).not.toBe('password123');
    });

    it('should return same hash for same password', () => {
      const hash1 = service.hashPassword('password123');
      const hash2 = service.hashPassword('password123');
      expect(hash1).toBe(hash2);
    });
  });
});
```

### Python Example (pytest)

```python
# calculator.py
class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b

    def divide(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# test_calculator.py
import pytest
from calculator import Calculator

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        assert self.calc.add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert self.calc.add(-2, -3) == -5

    def test_divide_normal(self):
        assert self.calc.divide(10, 2) == 5.0

    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)
```

### Unit Testing Best Practices

1. **AAA Pattern**: Arrange, Act, Assert
   ```typescript
   it('should create user with valid data', () => {
     // Arrange
     const userData = { email: 'test@example.com', username: 'testuser' };

     // Act
     const user = createUser(userData);

     // Assert
     expect(user.email).toBe('test@example.com');
     expect(user.id).toBeDefined();
   });
   ```

2. **One Assertion Per Test** (when possible)
3. **Test Edge Cases**
4. **Use Descriptive Test Names**
5. **Keep Tests Independent**

## Integration Testing

### What to Test

Test interactions between multiple modules, services, or layers.

### Characteristics

- **Medium Speed**: Slower than unit tests
- **External Dependencies**: Database, APIs, file system
- **Realistic**: Tests actual integrations
- **Focused Scope**: Test specific integration points

### Example (API + Database)

```typescript
// users.integration.test.ts
import request from 'supertest';
import { app } from '../app';
import { database } from '../database';

describe('Users API Integration Tests', () => {
  beforeAll(async () => {
    await database.connect();
  });

  afterAll(async () => {
    await database.disconnect();
  });

  beforeEach(async () => {
    await database.clearTable('users');
  });

  describe('POST /api/v1/users', () => {
    it('should create a new user', async () => {
      const userData = {
        email: 'test@example.com',
        username: 'testuser',
        password: 'password123'
      };

      const response = await request(app)
        .post('/api/v1/users')
        .send(userData)
        .expect(201);

      expect(response.body.data).toHaveProperty('id');
      expect(response.body.data.email).toBe(userData.email);
      expect(response.body.data).not.toHaveProperty('password');

      // Verify in database
      const userInDb = await database.query(
        'SELECT * FROM users WHERE email = $1',
        [userData.email]
      );
      expect(userInDb.rows).toHaveLength(1);
    });

    it('should return 400 for duplicate email', async () => {
      const userData = {
        email: 'test@example.com',
        username: 'testuser',
        password: 'password123'
      };

      // Create first user
      await request(app).post('/api/v1/users').send(userData);

      // Try to create duplicate
      const response = await request(app)
        .post('/api/v1/users')
        .send(userData)
        .expect(400);

      expect(response.body.error.code).toBe('DUPLICATE_EMAIL');
    });
  });

  describe('GET /api/v1/users/:id', () => {
    it('should retrieve user by id', async () => {
      // Create user
      const createResponse = await request(app)
        .post('/api/v1/users')
        .send({
          email: 'test@example.com',
          username: 'testuser',
          password: 'password123'
        });

      const userId = createResponse.body.data.id;

      // Get user
      const response = await request(app)
        .get(`/api/v1/users/${userId}`)
        .expect(200);

      expect(response.body.data.id).toBe(userId);
      expect(response.body.data.email).toBe('test@example.com');
    });

    it('should return 404 for non-existent user', async () => {
      await request(app)
        .get('/api/v1/users/550e8400-e29b-41d4-a716-446655440000')
        .expect(404);
    });
  });
});
```

### Integration Testing Strategies

1. **Test Database**: Use a separate test database
2. **Fixtures**: Create test data before tests
3. **Cleanup**: Reset state between tests
4. **Transactions**: Rollback after each test (faster)

```typescript
// Using transactions for faster tests
beforeEach(async () => {
  await database.query('BEGIN');
});

afterEach(async () => {
  await database.query('ROLLBACK');
});
```

## End-to-End Testing

### What to Test

Test complete user workflows through the entire application stack.

### Characteristics

- **Slow**: Takes seconds to minutes
- **Real Environment**: Browser, network, database
- **User Perspective**: Tests like a real user
- **Brittle**: Can break from UI changes

### Example (Playwright)

```typescript
// users.e2e.test.ts
import { test, expect } from '@playwright/test';

test.describe('User Registration Flow', () => {
  test('should register a new user successfully', async ({ page }) => {
    // Navigate to registration page
    await page.goto('http://localhost:3000/register');

    // Fill out form
    await page.fill('input[name="email"]', 'test@example.com');
    await page.fill('input[name="username"]', 'testuser');
    await page.fill('input[name="password"]', 'password123');
    await page.fill('input[name="confirmPassword"]', 'password123');

    // Submit form
    await page.click('button[type="submit"]');

    // Wait for redirect to dashboard
    await page.waitForURL('http://localhost:3000/dashboard');

    // Verify success message
    await expect(page.locator('.success-message')).toContainText(
      'Welcome, testuser!'
    );

    // Verify user is logged in
    await expect(page.locator('.user-menu')).toContainText('testuser');
  });

  test('should show error for invalid email', async ({ page }) => {
    await page.goto('http://localhost:3000/register');

    await page.fill('input[name="email"]', 'invalid-email');
    await page.fill('input[name="username"]', 'testuser');
    await page.fill('input[name="password"]', 'password123');

    await page.click('button[type="submit"]');

    // Should not redirect
    await expect(page).toHaveURL('http://localhost:3000/register');

    // Should show error
    await expect(page.locator('.error-message')).toContainText(
      'Invalid email format'
    );
  });
});

test.describe('Login and Post Creation', () => {
  test('should login and create a post', async ({ page }) => {
    // Login
    await page.goto('http://localhost:3000/login');
    await page.fill('input[name="email"]', 'existing@example.com');
    await page.fill('input[name="password"]', 'password123');
    await page.click('button[type="submit"]');

    // Navigate to create post
    await page.click('a[href="/posts/new"]');

    // Create post
    await page.fill('input[name="title"]', 'My Test Post');
    await page.fill('textarea[name="content"]', 'This is test content');
    await page.click('button[type="submit"]');

    // Verify post was created
    await page.waitForURL(/\/posts\/[a-f0-9-]+/);
    await expect(page.locator('h1')).toContainText('My Test Post');
    await expect(page.locator('.post-content')).toContainText(
      'This is test content'
    );
  });
});
```

### E2E Testing Best Practices

1. **Test Critical Paths Only**
2. **Use Data Test IDs**
   ```html
   <button data-testid="submit-button">Submit</button>
   ```
3. **Wait for Network Calls**
4. **Seed Test Data**
5. **Run in CI/CD**

## Test Coverage

### What is Coverage?

Percentage of code executed during tests.

### Coverage Metrics

1. **Line Coverage**: Lines executed
2. **Branch Coverage**: Decision paths taken
3. **Function Coverage**: Functions called
4. **Statement Coverage**: Statements executed

### Coverage Goals

- **Minimum**: 60%
- **Good**: 80%
- **Excellent**: 90%+

### Achieving High Coverage

```bash
# JavaScript/TypeScript (Jest)
npm test -- --coverage

# Python (pytest)
pytest --cov=app --cov-report=html

# View report
open coverage/index.html
```

### Example Coverage Report

```
File                | % Stmts | % Branch | % Funcs | % Lines |
--------------------|---------|----------|---------|---------|
users.service.ts    |   95.23 |    88.88 |     100 |   95.00 |
auth.service.ts     |   88.23 |    75.00 |   85.71 |   87.50 |
posts.service.ts    |   72.72 |    66.66 |   71.42 |   72.00 |
--------------------|---------|----------|---------|---------|
All files           |   85.39 |    76.84 |   85.71 |   84.83 |
```

### Focus on Critical Paths

Aim for 100% coverage on:
- Business logic
- Authentication/authorization
- Payment processing
- Data validation
- Security-critical code

Lower coverage acceptable for:
- UI components (covered by E2E)
- Configuration files
- Generated code

## Testing Patterns

### Test Doubles

1. **Dummy**: Placeholder, never used
2. **Stub**: Returns predefined responses
3. **Spy**: Records how it was called
4. **Mock**: Verifies behavior
5. **Fake**: Simplified working implementation

### Given-When-Then

```typescript
test('should apply discount to order total', () => {
  // Given: A user with premium membership
  const user = { id: '123', membership: 'premium' };
  const order = { items: [...], subtotal: 100 };

  // When: Discount is applied
  const total = applyDiscount(order, user);

  // Then: Total should be reduced by 20%
  expect(total).toBe(80);
});
```

### Test Data Builders

```typescript
class UserBuilder {
  private user: Partial<User> = {
    role: 'user',
    status: 'active'
  };

  withEmail(email: string): this {
    this.user.email = email;
    return this;
  }

  withRole(role: string): this {
    this.user.role = role;
    return this;
  }

  build(): User {
    return this.user as User;
  }
}

// Usage
const admin = new UserBuilder()
  .withEmail('admin@example.com')
  .withRole('admin')
  .build();
```

### Object Mother

```typescript
class TestUsers {
  static basicUser(): User {
    return {
      id: '123',
      email: 'user@example.com',
      role: 'user',
      status: 'active'
    };
  }

  static adminUser(): User {
    return {
      id: '456',
      email: 'admin@example.com',
      role: 'admin',
      status: 'active'
    };
  }

  static inactiveUser(): User {
    return {
      id: '789',
      email: 'inactive@example.com',
      role: 'user',
      status: 'inactive'
    };
  }
}

// Usage
const user = TestUsers.basicUser();
```

## Mocking & Stubbing

### Mocking External Services

```typescript
// users.service.ts
export class UsersService {
  constructor(
    private emailService: EmailService,
    private database: Database
  ) {}

  async createUser(userData: CreateUserDto): Promise<User> {
    const user = await this.database.insert('users', userData);
    await this.emailService.sendWelcomeEmail(user.email);
    return user;
  }
}

// users.service.test.ts
describe('UsersService', () => {
  let service: UsersService;
  let mockEmailService: jest.Mocked<EmailService>;
  let mockDatabase: jest.Mocked<Database>;

  beforeEach(() => {
    mockEmailService = {
      sendWelcomeEmail: jest.fn()
    } as any;

    mockDatabase = {
      insert: jest.fn()
    } as any;

    service = new UsersService(mockEmailService, mockDatabase);
  });

  it('should create user and send welcome email', async () => {
    const userData = { email: 'test@example.com', username: 'test' };
    const createdUser = { id: '123', ...userData };

    mockDatabase.insert.mockResolvedValue(createdUser);
    mockEmailService.sendWelcomeEmail.mockResolvedValue(undefined);

    const result = await service.createUser(userData);

    expect(mockDatabase.insert).toHaveBeenCalledWith('users', userData);
    expect(mockEmailService.sendWelcomeEmail).toHaveBeenCalledWith(
      userData.email
    );
    expect(result).toEqual(createdUser);
  });
});
```

### Stubbing HTTP Requests

```typescript
// Using MSW (Mock Service Worker)
import { rest } from 'msw';
import { setupServer } from 'msw/node';

const server = setupServer(
  rest.get('https://api.example.com/users', (req, res, ctx) => {
    return res(
      ctx.json({
        data: [
          { id: '1', name: 'User 1' },
          { id: '2', name: 'User 2' }
        ]
      })
    );
  })
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

it('should fetch users from API', async () => {
  const users = await fetchUsers();
  expect(users).toHaveLength(2);
});
```

## Testing Best Practices

### 1. Write Tests First (TDD)

```typescript
// 1. Write failing test
it('should validate email', () => {
  expect(validateEmail('test@example.com')).toBe(true);
});

// 2. Write minimal code to pass
function validateEmail(email: string): boolean {
  return email.includes('@');
}

// 3. Refactor
function validateEmail(email: string): boolean {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}
```

### 2. Keep Tests Simple

❌ Bad:
```typescript
it('should handle everything', () => {
  // 50 lines of test code
});
```

✅ Good:
```typescript
it('should create user', () => { ... });
it('should validate email', () => { ... });
it('should hash password', () => { ... });
```

### 3. Test Behavior, Not Implementation

❌ Bad (testing implementation):
```typescript
it('should call hashPassword with bcrypt', () => {
  expect(bcrypt.hash).toHaveBeenCalled();
});
```

✅ Good (testing behavior):
```typescript
it('should not store plain text password', () => {
  const user = createUser({ password: 'password123' });
  expect(user.password).not.toBe('password123');
});
```

### 4. Use Descriptive Test Names

❌ Bad:
```typescript
it('test1', () => { ... });
it('works', () => { ... });
```

✅ Good:
```typescript
it('should return 400 when email is invalid', () => { ... });
it('should create user with valid data', () => { ... });
```

### 5. Avoid Test Interdependence

Each test should run independently.

### 6. Clean Up After Tests

```typescript
afterEach(async () => {
  await database.clear();
  jest.clearAllMocks();
});
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:14
        env:
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm ci

      - name: Run unit tests
        run: npm run test:unit

      - name: Run integration tests
        run: npm run test:integration
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test

      - name: Generate coverage report
        run: npm run test:coverage

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
```

## Tools & Frameworks

### JavaScript/TypeScript

- **Jest**: Unit & integration testing
- **Vitest**: Modern, fast alternative to Jest
- **Playwright**: E2E testing
- **Cypress**: E2E testing (alternative)
- **Testing Library**: React/Vue component testing
- **Supertest**: HTTP API testing

### Python

- **pytest**: Unit & integration testing
- **unittest**: Built-in testing framework
- **Selenium**: E2E browser testing
- **Playwright**: E2E testing
- **requests-mock**: HTTP mocking

### Tools

- **Istanbul/nyc**: Code coverage
- **Codecov**: Coverage reporting
- **SonarQube**: Code quality analysis

## Resources

- [Jest Documentation](https://jestjs.io/)
- [Testing Library](https://testing-library.com/)
- [Playwright](https://playwright.dev/)
- [Martin Fowler's Testing Guide](https://martinfowler.com/testing/)
