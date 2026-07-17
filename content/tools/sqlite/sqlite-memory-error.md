---
title: "SQLite Out of Memory"
description: "SQLite operation fails due to insufficient memory."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
tags: ["sqlite", "memory", "oom", "allocation", "large-query"]
weight: 5
---

# SQLite Out of Memory

A SQLite out of memory error occurs when the database engine cannot allocate sufficient memory for an operation. This typically happens with large result sets or complex queries.

## Common Causes

- Very large result sets
- Complex JOIN operations on large tables
- Large BLOB data
- Insufficient system memory

## How to Fix

### Limit Query Results

```sql
SELECT * FROM large_table LIMIT 1000;
```

### Use Pagination

```sql
SELECT * FROM users ORDER BY id LIMIT 100 OFFSET 0;
SELECT * FROM users ORDER BY id LIMIT 100 OFFSET 100;
```

### Optimize Queries

```sql
-- Add indexes for WHERE clauses
CREATE INDEX idx_email ON users(email);

-- Use EXPLAIN to check query plan
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';
```

### Close Unused Connections

```python
import sqlite3
conn = sqlite3.connect('mydb.sqlite')
# Use and close
conn.close()
```

### Check Memory Usage

```bash
# Monitor SQLite memory usage
sqlite3 mydb.sqlite "PRAGMA memory_used;"
```

## Examples

```python
import sqlite3
conn = sqlite3.connect('mydb.sqlite')
cursor = conn.execute('SELECT * FROM huge_table')
# sqlite3.MemoryError: out of memory

# Fix: use pagination
cursor = conn.execute('SELECT * FROM huge_table LIMIT 1000')
```

## Related Errors

- [Connection Error]({{< relref "/tools/sqlite/sqlite-connection-error" >}}) — connection failure
- [Constraint Error]({{< relref "/tools/sqlite/constraint-error" >}}) — constraint violation
