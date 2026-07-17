---
title: "[Solution] SQLite Out of Memory"
description: "Fix SQLite out of memory errors. Resolve memory allocation failures in SQLite operations."
tools: ["sqlite"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQLite Out of Memory

An out of memory error means SQLite could not allocate the memory needed for an operation. This typically happens with very large result sets, complex queries, or when system memory is exhausted.

## Common Causes

- A query returns millions of rows and tries to load them all into memory
- A large blob or text value exceeds available memory
- Multiple concurrent connections consume excessive memory
- The system is under memory pressure from other processes

## How to Fix

### Process Rows in Batches

```python
# WRONG: loads all rows into memory
rows = cursor.execute("SELECT * FROM big_table").fetchall()

# CORRECT: iterate row by row
for row in cursor.execute("SELECT * FROM big_table"):
    process(row)
```

### Use LIMIT for Large Queries

```sql
SELECT * FROM big_table LIMIT 10000 OFFSET 0;
-- Process in batches
SELECT * FROM big_table LIMIT 10000 OFFSET 10000;
```

### Increase Available Memory

```bash
# Check system memory
free -m

# Add swap space
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### Optimize Queries

```sql
-- Add indexes to reduce memory usage
CREATE INDEX idx_users_email ON users(email);

-- Use EXPLAIN to check query plan
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';
```

### Reduce Cache Size

```sql
PRAGMA cache_size = -2000;  -- 2MB instead of default
```

## Examples

```sql
-- Large result set
SELECT * FROM logs WHERE date > '2020-01-01';
-- Error: out of memory (returned 10M+ rows)
-- Fix: add LIMIT or use WHERE to narrow results

-- Large blob
INSERT INTO files (data) VALUES (readfile('huge-file.bin'));
-- Error: out of memory
-- Fix: stream data in chunks
```

## Related Errors

- [I/O Error]({{< relref "/tools/sqlite/io-error2" >}}) — disk I/O failure
- [Database Locked]({{< relref "/tools/sqlite/database-locked" >}}) — write lock contention
