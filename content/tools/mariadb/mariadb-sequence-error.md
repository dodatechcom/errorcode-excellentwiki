---
title: "[Solution] MariaDB Sequence Error — How to Fix"
description: "Fix MariaDB sequence errors including AUTO_INCREMENT issues, custom sequence tables, and duplicate key problems in sequential ID generation"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Sequence Error

Sequence errors in MariaDB relate to AUTO_INCREMENT management, custom sequence tables for non-numeric IDs, and duplicate key issues when generating sequential identifiers.

## Why It Happens

- AUTO_INCREMENT counter is reset after DELETE or TRUNCATE
- Two sessions try to insert the same sequence value simultaneously
- The sequence table has a gap or is corrupted
- AUTO_INCREMENT reaches the maximum for the integer type
- A MyISAM table's AUTO_INCREMENT is lower than the max ID
- Custom sequence implementation uses non-atomic operations

## Common Error Messages

```
ERROR 1062 (23000): Duplicate entry '12345' for key 'PRIMARY'
```

```
ERROR 167 (HY000): Cannot setup serialized global variable name because of auto_increment
```

```
Warning: AUTO_INCREMENT: Attempt to start the auto_increment value at value '0'
has failed (number of attempts: 1)
```

```
ERROR 21 (HY000): Can't write; because of key constraint error
```

## How to Fix It

### 1. Reset AUTO_INCREMENT After DELETE

```sql
-- Check current AUTO_INCREMENT value
SHOW CREATE TABLE users;

-- Reset to max(id) + 1
ALTER TABLE users AUTO_INCREMENT = (SELECT IFNULL(MAX(id), 0) + 1 FROM users);

-- Or set a specific value
ALTER TABLE users AUTO_INCREMENT = 10001;
```

### 2. Fix Duplicate Key from Sequence Gap

```sql
-- Check for duplicate IDs
SELECT id, COUNT(*) FROM users GROUP BY id HAVING COUNT(*) > 1;

-- Find and fix gaps
SELECT @rownum := @rownum + 1 AS expected, u.id AS actual
FROM users u, (SELECT @rownum := 0) r
WHERE u.id != @rownum;

-- Reset AUTO_INCREMENT after fixing duplicates
ALTER TABLE users AUTO_INCREMENT = (SELECT IFNULL(MAX(id), 0) + 1 FROM users);
```

### 3. Use Atomic Sequence Generation

```sql
-- BAD: non-atomic sequence (race condition possible)
INSERT INTO sequences (name, current_val) VALUES ('order', current_val + 1);

-- GOOD: atomic sequence using LAST_INSERT_ID
UPDATE sequences SET current_val = LAST_INSERT_ID(current_val + 1) WHERE name = 'order';
SELECT LAST_INSERT_ID();

-- GOOD: MariaDB 10.3+ SEQUENCE object
CREATE SEQUENCE order_seq START WITH 1 INCREMENT BY 1;
SELECT NEXTVAL(order_seq);
```

### 4. Fix AUTO_INCREMENT on MyISAM Table

```sql
-- MyISAM stores AUTO_INCREMENT counter in the .MYI file
-- If the file is corrupted, the counter may be wrong
-- Fix: rebuild the table
ALTER TABLE myisam_table ENGINE = MyISAM;

-- Or use myisamchk
myisamchk --recover /var/lib/mysql/mydb/myisam_table
```

## Common Scenarios

- **AUTO_INCREMENT jumps after bulk DELETE**: MariaDB does not reuse deleted IDs by default. This is expected behavior, not an error.
- **Concurrent inserts cause duplicate keys**: Use AUTO_INCREMENT with InnoDB's gap locking for safe concurrent inserts.
- **Sequence table becomes a bottleneck**: Replace with SEQUENCE objects (MariaDB 10.3+) or application-level ID generation.

## Prevent It

- Use InnoDB for tables with AUTO_INCREMENT for automatic gap locking
- Use MariaDB SEQUENCE objects (10.3+) instead of custom sequence tables
- Monitor AUTO_INCREMENT values to detect approaching integer limits

## Related Pages

- [MariaDB Overflow Error](/tools/mariadb/mariadb-overflow-error)
- [MariaDB Schema Error](/tools/mariadb/mariadb-schema-error)
- [MySQL Sequence Error](/tools/mysql/mysql-sequence-error)
