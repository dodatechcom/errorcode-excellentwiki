---
title: "[Solution] TiDB DML Execution Error — How to Fix"
description: "Fix TiDB DML execution errors when INSERT, UPDATE, DELETE operations fail due to constraint or data issues"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB DML Execution Error

DML execution errors occur when Data Manipulation Language operations fail due to constraint violations, data type mismatches, or transaction conflicts.

## Why It Happens

- Unique constraint violation on primary key or unique index
- Foreign key constraint violation (if enabled)
- Data type mismatch between value and column definition
- Transaction conflict with concurrent modifications
- Row size exceeds the maximum allowed limit

## Common Error Messages

```
ERROR 1062: Duplicate entry '123' for key 'PRIMARY'
```

```
ERROR 1406: Data too long for column 'name'
```

```
ERROR 8028: Information schema is changed during the transaction
```

```
ERROR 1105: unknown column in field list
```

## How to Fix It

### 1. Check Constraint Violations

```sql
-- Check for duplicate keys
SELECT id, COUNT(*) FROM mytable GROUP BY id HAVING COUNT(*) > 1;
```

### 2. Fix Data Type Mismatches

```sql
-- Check column definition
SHOW CREATE TABLE mytable;
DESCRIBE mytable;
```

### 3. Use INSERT IGNORE or ON DUPLICATE KEY

```sql
INSERT IGNORE INTO mytable (id, name) VALUES (1, 'Alice');
INSERT INTO mytable (id, name) VALUES (1, 'Alice') ON DUPLICATE KEY UPDATE name = 'Alice Updated';
```

### 4. Handle Transaction Conflicts

```python
import mysql.connector
import time

max_retries = 3
for attempt in range(max_retries):
    try:
        cursor.execute("UPDATE orders SET status = 'processed' WHERE id = 100")
        connection.commit()
        break
    except mysql.connector.IntegrityError:
        if attempt < max_retries - 1:
            connection.rollback()
            time.sleep(0.1)
            continue
        raise
```

## Examples

```
mysql> INSERT INTO users (id, name) VALUES (1, 'Alice');
ERROR 1062: Duplicate entry '1' for key 'users.PRIMARY'

mysql> INSERT INTO users (id, name) VALUES (2, 'Alice');
Query OK, 1 row affected
```

## Prevent It

- Validate data types before inserting
- Handle duplicate key errors in application code
- Use appropriate INSERT strategies for concurrent writes

## Related Pages

- [TiDB DML Error](/tools/tidb/tidb-dml-error)
- [TiDB Transaction Error](/tools/tidb/tidb-transaction-error)
- [TiDB Lock Error](/tools/tidb/tidb-lock-error)
