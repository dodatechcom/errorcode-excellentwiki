---
title: "[Solution] TiDB JSON Error — How to Fix"
description: "Fix TiDB JSON errors by resolving JSON function failures, fixing JSON data type issues, and handling JSON query problems"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB JSON Error

TiDB JSON errors occur when using JSON data types, JSON functions, or JSON path expressions. TiDB supports MySQL-compatible JSON operations.

## Why It Happens

- JSON document is malformed
- JSON path expression is invalid
- JSON function is not supported
- JSON data type is too large
- JSON indexing is not configured
- JSON extract returns null unexpectedly

## Common Error Messages

```
ERROR: invalid JSON document
```

```
ERROR: invalid JSON path expression
```

```
ERROR: JSON function not supported
```

```
ERROR: JSON data too large
```

## How to Fix It

### 1. Store JSON Data Correctly

```sql
-- Create table with JSON column
CREATE TABLE events (
  id SERIAL PRIMARY KEY,
  data JSONB NOT NULL
);

-- Insert JSON data
INSERT INTO events (data) VALUES ('{"type": "login", "user": "alice"}');

-- Use JSONB for better performance
-- JSONB is indexed and faster for queries
```

### 2. Query JSON Data

```sql
-- Extract JSON values
SELECT data->>'type' AS event_type FROM events;

-- Filter by JSON values
SELECT * FROM events WHERE data->>'type' = 'login';

-- Use JSON_EXTRACT
SELECT JSON_EXTRACT(data, '$.user') FROM events;

-- Use JSON_CONTAINS
SELECT * FROM events WHERE JSON_CONTAINS(data->'$.tags', '"important"');
```

### 3. Create JSON Indexes

```sql
-- Create index on JSON column
CREATE INDEX idx_event_type ON events ((data->>'type'));

-- Create composite index
CREATE INDEX idx_event_user_type ON events ((data->>'user'), (data->>'type'));
```

### 4. Fix JSON Issues

```sql
-- Validate JSON before insert
INSERT INTO events (data) VALUES (JSON_VALID('{"valid": true}'));

-- Use JSON_PRETTY for debugging
SELECT JSON_PRETTY(data) FROM events;

-- Use JSON_TYPE to check type
SELECT JSON_TYPE(data) FROM events;
```

## Common Scenarios

- **JSON query is slow**: Create appropriate indexes on JSON paths.
- **JSON path returns null**: Check path syntax and data structure.
- **JSON function not supported**: Check TiDB documentation for supported functions.

## Prevent It

- Use JSONB instead of JSON for better performance
- Create indexes on frequently queried JSON paths
- Validate JSON data before insertion

## Related Pages

- [TiDB Query Error](/tools/tidb/tidb-query-error)
- [TiDB DDL Error](/tools/tidb/tidb-ddl-error)
- [TiDB DML Error](/tools/tidb/tidb-dml-error)
