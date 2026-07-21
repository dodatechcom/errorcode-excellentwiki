---
title: "[Solution] MySQL Key Generation Error"
description: "Fix MySQL key generation error when auto-increment or unique key generation fails during inserts"
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
---

# MySQL Key Generation Error

Auto-increment values are exhausted, duplicated, or the unique key generation mechanism encounters an error during INSERT operations.

## Common Causes

- AUTO_INCREMENT counter reaches the data type limit (INT MAX)
- Duplicate auto-increment value from a rollback or replication conflict
- UUID or GUID generation produces duplicate values
- Composite unique key has overlapping constraint values
- Table was altered to change AUTO_INCREMENT value incorrectly

## How to Fix

### Check Current AUTO_INCREMENT Value

```sql
-- Current auto-increment value
SHOW CREATE TABLE orders;

-- Via information schema
SELECT AUTO_INCREMENT
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME = 'orders'
  AND TABLE_SCHEMA = 'mydb';
```

### Reset AUTO_INCREMENT

```sql
-- Set to max(id) + 1
ALTER TABLE orders AUTO_INCREMENT = (
  SELECT IFNULL(MAX(id), 0) + 1 FROM orders
);

-- Or manually set a higher value
ALTER TABLE orders AUTO_INCREMENT = 1000000;
```

### Use BIGINT for Large Tables

```sql
-- INT max is ~2.1 billion, BIGINT is ~9.2 quintillion
ALTER TABLE orders MODIFY id BIGINT UNSIGNED AUTO_INCREMENT;
```

### Generate Unique Keys Application-Side

```sql
-- Use UUID for distributed systems
INSERT INTO orders (id, customer_id) VALUES (UUID(), 'user-42');

-- Or use ULID for sortable unique keys
INSERT INTO orders (id, customer_id) VALUES (UUID_SHORT(), 'user-42');
```

### Handle Duplicate Key Conflicts

```sql
-- Use INSERT IGNORE to skip duplicates
INSERT IGNORE INTO orders (order_code) VALUES ('ORD-001');

-- Or use ON DUPLICATE KEY UPDATE
INSERT INTO orders (order_code, total)
VALUES ('ORD-001', 100.00)
ON DUPLICATE KEY UPDATE total = VALUES(total);
```

## Examples

```
ERROR 1062 (23000): Duplicate entry '2147483647' for key
  'orders.PRIMARY' -- INT auto-increment exhausted

ERROR 1062 (23000): Duplicate entry 'ORD-001' for key
  'orders.uk_order_code'
```

## Related Errors

- [MySQL Duplicate Entry]({{< relref "/tools/mysql/mysql-duplicate-entry" >}}) -- duplicate keys
- [MySQL Out of Range]({{< relref "/tools/mysql/mysql-out-of-range" >}}) -- range overflow
- [MySQL Auto-Increment Error]({{< relref "/tools/mysql/mysql-innodb-error" >}}) -- InnoDB issues
