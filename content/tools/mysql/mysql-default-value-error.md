---
title: "[Solution] MySQL Default Value Expression Error"
description: "Fix MySQL default value expression error when column default values use expressions or functions that are not allowed"
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
---

# MySQL Default Value Expression Error

A column DEFAULT clause uses an expression or function that MySQL does not support in default definitions. The ALTER TABLE or CREATE TABLE statement fails.

## Common Causes

- Using a function that is not deterministic in DEFAULT
- Default expression references another column (before MySQL 8.0.13)
- BLOB, TEXT, or JSON columns with non-constant defaults
- Using NOW() before MySQL 8.0.13 (only CURRENT_TIMESTAMP was allowed)
- Stored functions cannot be used in DEFAULT expressions

## How to Fix

### Use Deterministic Expressions

```sql
-- MySQL 8.0.13+: deterministic expressions are allowed
CREATE TABLE orders (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  status VARCHAR(20) DEFAULT 'pending',
  total DECIMAL(10,2) DEFAULT (0.00),
  discount DECIMAL(10,2) DEFAULT (GREATEST(0, 0))
);
```

### Use CURRENT_TIMESTAMP for Timestamps

```sql
-- Allowed: CURRENT_TIMESTAMP for datetime/timestamp
CREATE TABLE events (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

### Set Default in Application Instead

```sql
-- For complex defaults, set in the application layer
CREATE TABLE orders (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  calculated_at DATETIME NULL  -- set by application
);
```

### Use Triggers for Complex Defaults

```sql
DELIMITER //
CREATE TRIGGER trg_orders_defaults
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
  IF NEW.priority IS NULL THEN
    SET NEW.priority = CASE
      WHEN NEW.total > 1000 THEN 'high'
      ELSE 'normal'
    END;
  END IF;
END //
DELIMITER ;
```

### Fix Column Type Issues

```sql
-- BLOB/TEXT cannot have literal defaults (before 8.0.13)
-- Use NULL or change column type
ALTER TABLE products MODIFY description TEXT NULL DEFAULT NULL;
```

## Examples

```
ERROR 1067 (42000): Invalid default value for 'created_at'

ERROR 3756 (HY000): The default value expression for column
  'priority' contains a disallowed function.
```

## Related Errors

- [MySQL Syntax Error]({{< relref "/tools/mysql/mysql-syntax-error" >}}) -- syntax issues
- [MySQL Column Doesn't Exist]({{< relref "/tools/mysql/mysql-column-doesnt-exist" >}}) -- column issues
- [MySQL Table Doesn't Exist]({{< relref "/tools/mysql/mysql-table-doesnt-exist" >}}) -- table issues
