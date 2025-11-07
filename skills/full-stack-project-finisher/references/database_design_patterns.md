# Database Design Patterns

Best practices for PostgreSQL database schema design, optimization, and maintenance.

## Table of Contents

1. [Core Principles](#core-principles)
2. [Primary Keys](#primary-keys)
3. [Normalization](#normalization)
4. [Indexes](#indexes)
5. [Relationships](#relationships)
6. [Audit Trails](#audit-trails)
7. [Soft Deletes](#soft-deletes)
8. [Performance Optimization](#performance-optimization)
9. [Common Patterns](#common-patterns)
10. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)

## Core Principles

### 1. Design for Scalability

- Use UUIDs for distributed systems
- Plan for horizontal scaling from day one
- Avoid database-level auto-incrementing IDs in distributed environments
- Consider partitioning strategies for large tables

### 2. Maintain Data Integrity

- Use foreign key constraints
- Implement check constraints for business rules
- Use NOT NULL where appropriate
- Set proper cascade rules (CASCADE, SET NULL, RESTRICT)

### 3. Optimize for Queries

- Index based on actual query patterns
- Avoid over-indexing (each index has write cost)
- Use covering indexes when possible
- Monitor slow query logs

## Primary Keys

### UUID vs Serial IDs

**Use UUIDs when:**
- Building distributed systems
- Merging data from multiple sources
- Need offline ID generation
- Want to hide database size from users

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    -- other columns
);
```

**Use SERIAL when:**
- Single database instance
- Need ordered IDs
- Want smaller index size
- Human-readable IDs are important

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    -- other columns
);
```

**Best Practice:** Use UUIDs for new projects unless you have specific reasons to use SERIAL.

## Normalization

### Normal Forms

**1NF (First Normal Form):**
- Eliminate repeating groups
- Each column contains atomic values

❌ Bad:
```sql
CREATE TABLE orders (
    id UUID PRIMARY KEY,
    products TEXT -- "Product1, Product2, Product3"
);
```

✅ Good:
```sql
CREATE TABLE orders (
    id UUID PRIMARY KEY
);

CREATE TABLE order_items (
    id UUID PRIMARY KEY,
    order_id UUID REFERENCES orders(id),
    product_id UUID REFERENCES products(id)
);
```

**2NF (Second Normal Form):**
- Meet 1NF requirements
- Remove partial dependencies

**3NF (Third Normal Form):**
- Meet 2NF requirements
- Remove transitive dependencies

### When to Denormalize

Denormalize strategically for:
- Read-heavy operations (caching computed values)
- Reporting tables
- Full-text search columns
- Frequently accessed aggregations

```sql
-- Denormalized for performance
CREATE TABLE posts (
    id UUID PRIMARY KEY,
    title TEXT NOT NULL,
    user_id UUID REFERENCES users(id),
    comment_count INTEGER DEFAULT 0, -- Denormalized
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Update with trigger
CREATE OR REPLACE FUNCTION update_post_comment_count()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE posts
    SET comment_count = (
        SELECT COUNT(*) FROM comments WHERE post_id = NEW.post_id
    )
    WHERE id = NEW.post_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_comment_count
AFTER INSERT OR DELETE ON comments
FOR EACH ROW EXECUTE FUNCTION update_post_comment_count();
```

## Indexes

### B-Tree Indexes (Default)

Best for:
- Equality comparisons (`=`)
- Range queries (`<`, `>`, `BETWEEN`)
- Sorting (`ORDER BY`)
- Pattern matching (`LIKE 'prefix%'`)

```sql
-- Single column index
CREATE INDEX idx_users_email ON users(email);

-- Multi-column index (order matters!)
CREATE INDEX idx_orders_user_created ON orders(user_id, created_at DESC);

-- Partial index (filtered)
CREATE INDEX idx_active_users ON users(email) WHERE deleted_at IS NULL;

-- Covering index (include columns)
CREATE INDEX idx_users_email_covering ON users(email) INCLUDE (full_name, role);
```

### Hash Indexes

Best for exact equality comparisons:

```sql
CREATE INDEX idx_users_uuid ON users USING HASH(id);
```

### GIN Indexes

Best for:
- JSONB columns
- Array columns
- Full-text search

```sql
-- JSONB
CREATE INDEX idx_users_metadata ON users USING GIN(metadata);

-- Arrays
CREATE INDEX idx_posts_tags ON posts USING GIN(tags);

-- Full-text search
CREATE INDEX idx_posts_search ON posts USING GIN(to_tsvector('english', title || ' ' || content));
```

### GiST Indexes

Best for:
- Range types
- Geometric types
- Full-text search (alternative to GIN)

```sql
CREATE INDEX idx_events_date_range ON events USING GIST(date_range);
```

### Index Best Practices

1. **Index Foreign Keys:** Always index foreign key columns
   ```sql
   ALTER TABLE posts ADD FOREIGN KEY (user_id) REFERENCES users(id);
   CREATE INDEX idx_posts_user_id ON posts(user_id);
   ```

2. **Index Query Filters:** Index columns used in WHERE clauses
   ```sql
   -- For: SELECT * FROM posts WHERE status = 'published' AND created_at > NOW() - INTERVAL '7 days'
   CREATE INDEX idx_posts_status_created ON posts(status, created_at);
   ```

3. **Use Partial Indexes:** Filter out irrelevant rows
   ```sql
   CREATE INDEX idx_pending_orders ON orders(created_at)
   WHERE status = 'pending';
   ```

4. **Monitor Index Usage:**
   ```sql
   -- Check unused indexes
   SELECT schemaname, tablename, indexname, idx_scan
   FROM pg_stat_user_indexes
   WHERE idx_scan = 0
   AND indexrelname NOT LIKE 'pg_toast%';
   ```

## Relationships

### One-to-Many

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4()
);

CREATE TABLE posts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title TEXT NOT NULL
);

CREATE INDEX idx_posts_user_id ON posts(user_id);
```

### Many-to-Many

```sql
CREATE TABLE students (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4()
);

CREATE TABLE courses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4()
);

-- Junction table
CREATE TABLE enrollments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    student_id UUID NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    enrolled_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(student_id, course_id)
);

CREATE INDEX idx_enrollments_student ON enrollments(student_id);
CREATE INDEX idx_enrollments_course ON enrollments(course_id);
```

### One-to-One

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4()
);

CREATE TABLE user_profiles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID UNIQUE NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    bio TEXT,
    avatar_url TEXT
);
```

### Self-Referencing

```sql
-- Hierarchical data (comments with replies)
CREATE TABLE comments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    post_id UUID NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
    parent_comment_id UUID REFERENCES comments(id) ON DELETE CASCADE,
    content TEXT NOT NULL
);

CREATE INDEX idx_comments_parent ON comments(parent_comment_id)
WHERE parent_comment_id IS NOT NULL;
```

## Audit Trails

### Standard Audit Columns

```sql
CREATE TABLE posts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title TEXT NOT NULL,

    -- Audit columns
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL,
    created_by UUID REFERENCES users(id),
    updated_by UUID REFERENCES users(id)
);

-- Auto-update trigger
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_posts_timestamp
BEFORE UPDATE ON posts
FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
```

### Full Audit Log Table

```sql
CREATE TABLE audit_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    table_name TEXT NOT NULL,
    record_id UUID NOT NULL,
    action TEXT NOT NULL CHECK (action IN ('INSERT', 'UPDATE', 'DELETE')),
    old_data JSONB,
    new_data JSONB,
    changed_by UUID REFERENCES users(id),
    changed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_audit_logs_table_record ON audit_logs(table_name, record_id);
CREATE INDEX idx_audit_logs_changed_at ON audit_logs(changed_at);
```

## Soft Deletes

### Implementation

```sql
CREATE TABLE posts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title TEXT NOT NULL,
    deleted_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index for active records
CREATE INDEX idx_posts_active ON posts(id)
WHERE deleted_at IS NULL;

-- Soft delete function
CREATE OR REPLACE FUNCTION soft_delete_post(post_id UUID)
RETURNS VOID AS $$
BEGIN
    UPDATE posts
    SET deleted_at = NOW()
    WHERE id = post_id AND deleted_at IS NULL;
END;
$$ LANGUAGE plpgsql;
```

### Querying Active Records

```sql
-- Always filter by deleted_at
SELECT * FROM posts WHERE deleted_at IS NULL;

-- Or create a view
CREATE VIEW active_posts AS
SELECT * FROM posts WHERE deleted_at IS NULL;
```

### Pros and Cons

**Pros:**
- Recover accidentally deleted data
- Maintain referential integrity
- Audit trail of deletions

**Cons:**
- Query complexity
- Index overhead
- Storage cost
- UNIQUE constraints need careful handling

## Performance Optimization

### Connection Pooling

Use connection pooling (PgBouncer, database built-in) for optimal performance.

### Prepared Statements

```sql
-- Faster repeated queries
PREPARE get_user AS
SELECT * FROM users WHERE email = $1;

EXECUTE get_user('user@example.com');
```

### Avoid N+1 Queries

❌ Bad (N+1):
```sql
-- Query 1: Get posts
SELECT * FROM posts LIMIT 10;

-- Query 2-11: Get author for each post (10 times!)
SELECT * FROM users WHERE id = ?;
```

✅ Good (2 queries):
```sql
-- Query 1: Get posts
SELECT * FROM posts LIMIT 10;

-- Query 2: Get all authors at once
SELECT * FROM users WHERE id IN (?, ?, ?, ...);
```

✅ Better (1 query with JOIN):
```sql
SELECT posts.*, users.username, users.email
FROM posts
JOIN users ON posts.user_id = users.id
LIMIT 10;
```

### Batch Operations

```sql
-- Instead of multiple INSERTs
INSERT INTO users (email, username) VALUES
    ('user1@example.com', 'user1'),
    ('user2@example.com', 'user2'),
    ('user3@example.com', 'user3');

-- Use COPY for very large datasets
COPY users (email, username) FROM '/path/to/data.csv' CSV HEADER;
```

### Materialized Views

For expensive queries:

```sql
CREATE MATERIALIZED VIEW user_statistics AS
SELECT
    users.id,
    users.username,
    COUNT(DISTINCT posts.id) AS post_count,
    COUNT(DISTINCT comments.id) AS comment_count
FROM users
LEFT JOIN posts ON posts.user_id = users.id
LEFT JOIN comments ON comments.user_id = users.id
GROUP BY users.id, users.username;

-- Create index on materialized view
CREATE INDEX idx_user_stats_username ON user_statistics(username);

-- Refresh periodically
REFRESH MATERIALIZED VIEW CONCURRENTLY user_statistics;
```

## Common Patterns

### Enum vs Lookup Table

**Use ENUM for:**
- Static, rarely changing values
- Small value sets (< 10 values)

```sql
CREATE TYPE user_role AS ENUM ('admin', 'user', 'guest');

CREATE TABLE users (
    id UUID PRIMARY KEY,
    role user_role NOT NULL DEFAULT 'user'
);
```

**Use Lookup Table for:**
- Frequently changing values
- Need additional metadata
- Internationalization

```sql
CREATE TABLE roles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    permissions JSONB
);

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    role_id UUID NOT NULL REFERENCES roles(id)
);
```

### Versioning Records

```sql
CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    document_number INTEGER NOT NULL,
    version INTEGER NOT NULL DEFAULT 1,
    title TEXT NOT NULL,
    content TEXT,
    is_current BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(document_number, version)
);

CREATE INDEX idx_documents_current ON documents(document_number)
WHERE is_current = TRUE;
```

### Polymorphic Associations

```sql
-- Taggable items (posts, images, videos)
CREATE TABLE tags (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE taggings (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tag_id UUID NOT NULL REFERENCES tags(id),
    taggable_type TEXT NOT NULL, -- 'post', 'image', 'video'
    taggable_id UUID NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_taggings_taggable ON taggings(taggable_type, taggable_id);
CREATE INDEX idx_taggings_tag ON taggings(tag_id);
```

## Anti-Patterns to Avoid

### 1. Entity-Attribute-Value (EAV)

❌ Avoid:
```sql
CREATE TABLE object_attributes (
    object_id UUID,
    attribute_name TEXT,
    attribute_value TEXT
);
```

✅ Use JSONB instead:
```sql
CREATE TABLE objects (
    id UUID PRIMARY KEY,
    attributes JSONB
);
```

### 2. Storing Comma-Separated Values

❌ Avoid:
```sql
tags TEXT -- "tag1,tag2,tag3"
```

✅ Use arrays or junction tables:
```sql
tags TEXT[] -- ARRAY['tag1', 'tag2', 'tag3']
```

### 3. Using FLOAT for Money

❌ Avoid:
```sql
price FLOAT
```

✅ Use NUMERIC:
```sql
price NUMERIC(10, 2) -- 10 digits, 2 decimal places
```

### 4. Generic "data" or "value" Columns

Avoid overly generic columns that obscure meaning.

### 5. Not Using Transactions

Always use transactions for multi-step operations:

```sql
BEGIN;
    INSERT INTO orders (user_id, total) VALUES (?, ?) RETURNING id;
    INSERT INTO order_items (order_id, product_id, quantity) VALUES (?, ?, ?);
    UPDATE products SET stock = stock - ? WHERE id = ?;
COMMIT;
```

## Resources

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Use The Index, Luke](https://use-the-index-luke.com/)
- [Postgres Performance Tips](https://wiki.postgresql.org/wiki/Performance_Optimization)
