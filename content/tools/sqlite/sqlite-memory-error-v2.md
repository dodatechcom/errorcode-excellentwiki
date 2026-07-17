---
title: "SQLite - out of memory (SQLITE_NOMEM)"
description: "SQLite fails to allocate memory during query execution or database operations"
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
tags: ["sqlite", "memory", "oom", "allocation", "large-query"]
weight: 5
---

SQLite "out of memory" (SQLITE_NOMEM) error occurs when the database engine cannot allocate sufficient memory for an operation. This typically happens with very large result sets, complex queries, or when the system is under memory pressure.

## Common Causes

- Query returning extremely large result sets
- Complex JOIN operations requiring excessive memory
- System running low on available memory
- Large BLOB values stored in the database
- Memory leak in application code holding many open connections

## How to Fix

1. Use pagination for large result sets:

```python
def fetch_paginated(conn, table, page_size=1000, offset=0):
    cursor = conn.execute(
        f"SELECT * FROM {table} LIMIT ? OFFSET ?",
        (page_size, offset)
    )
    return cursor.fetchall()
```

2. Use streaming cursors for large results:

```python
conn = sqlite3.connect('mydb.sqlite')
cursor = conn.execute("SELECT * FROM large_table")
for row in cursor:  # iterates one row at a time
    process_row(row)
```

3. Optimize queries to reduce memory:

```sql
-- Instead of loading all data, aggregate in SQL
SELECT category, COUNT(*), SUM(amount)
FROM orders
GROUP BY category;
```

4. Check available system memory:

```bash
free -h
cat /proc/meminfo
```

5. Limit concurrent connections:

```python
import sqlite3
# Use a single connection per thread
conn = sqlite3.connect('mydb.sqlite', check_same_thread=False)
```

6. Increase system memory or swap:

```bash
# Add swap file
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

## Examples

```python
import sqlite3
conn = sqlite3.connect('mydb.sqlite')
# Error: out of memory
rows = conn.execute("SELECT * FROM huge_table").fetchall()  # loads everything

# Fix: use iteration or pagination
cursor = conn.execute("SELECT * FROM huge_table")
for row in cursor:
    process(row)  # memory efficient
```

## Related Errors

- [I/O error]({{< relref "/tools/sqlite/sqlite-io-error" >}})
- [Corruption error]({{< relref "/tools/sqlite/sqlite-corruption-error-v2" >}})
