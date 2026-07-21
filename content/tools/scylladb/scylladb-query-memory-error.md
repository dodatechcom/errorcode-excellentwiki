---
title: "[Solution] ScyllaDB Query Memory Limit Error — How to Fix"
description: "Fix ScyllaDB query memory limit errors when large queries exceed the configured per-query memory allocation"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Query Memory Limit Error

Query memory limit errors occur when a single CQL query consumes more memory than the per-query allocation limit, causing the query to be terminated.

## Why It Happens

- Query returns too many rows without LIMIT clause
- Large partition contains millions of cells
- SELECT * on a table with many columns
- Aggregation query operates on large dataset
- Paging is disabled for large result sets

## Common Error Messages

```
ReadTimeout: Query exceeded per-query memory limit of 4194304 bytes
```

```
error: query rejected: not enough memory to process request
```

```
QueryMemoryLimitExceeded: query requires more than allowed memory
```

## How to Fix It

### 1. Add LIMIT to Queries

```cql
SELECT * FROM mykeyspace.users WHERE user_id = 1 LIMIT 1000;
```

### 2. Select Only Required Columns

```cql
-- Bad: selects all columns
SELECT * FROM users WHERE user_id = 1;

-- Good: selects only needed columns
SELECT id, name, email FROM users WHERE user_id = 1;
```

### 3. Increase Query Memory Limit

```yaml
# In scylla.yaml
max_memory_for_unlimited_query: 52428800
```

### 4. Enable Automatic Paging

```python
# Python driver enables paging by default
statement = SimpleStatement("SELECT * FROM users", fetch_size=1000)
rows = session.execute(statement)
```

## Examples

```
ReadTimeout: Query exceeded memory limit for table users, 
partition key user_id, query size 8MB, limit 4MB
```

## Prevent It

- Always use LIMIT clause for read queries
- Use SELECT with specific columns instead of SELECT *
- Enable automatic paging in the client driver

## Related Pages

- [ScyllaDB Query Error](/tools/scylladb/scylladb-query-error)
- [ScyllaDB Query Timeout Error](/tools/scylladb/scylladb-query-timeout-error)
- [ScyllaDB Memory Error](/tools/scylladb/scylladb-memory-error)
