---
title: "[Solution] MariaDB Trigger Error — How to Fix"
description: "Fix MariaDB trigger errors including syntax issues, permission requirements, OLD/NEW reference problems, and recursive trigger prevention"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Trigger Error

Trigger errors occur when a BEFORE or AFTER INSERT, UPDATE, or DELETE trigger fails during execution. This happens due to syntax errors, insufficient privileges, incorrect OLD/NEW references, or infinite recursive loops.

## Why It Happens

- The trigger body has a syntax error
- The trigger references a table that does not exist
- The user lacks the `TRIGGER` privilege
- A trigger modifies a table that has another trigger causing recursion
- OLD or NEW values are referenced when they should not be
- The trigger's DECLARE section has errors

## Common Error Messages

```
ERROR 1360 (HY000): Trigger already exists
```

```
ERROR 1142 (42000): TRIGGER command denied to user 'myuser'@'localhost' for table 'users'
```

```
ERROR 1442 (HY000): Can't update table 'users' in stored function/trigger because
it is already used by statement which invoked this stored function/trigger
```

```
ERROR 1054 (42S22): Unknown column 'NEW.col_name' in 'trigger body'
```

## How to Fix It

### 1. Fix Trigger Syntax

```sql
DELIMITER //
CREATE TRIGGER trg_before_insert BEFORE INSERT ON users
FOR EACH ROW
BEGIN
  SET NEW.created_at = NOW();
  SET NEW.updated_at = NOW();
END//
DELIMITER ;
```

### 2. Grant Trigger Privileges

```sql
SHOW GRANTS FOR 'myuser'@'localhost';
GRANT TRIGGER ON mydb.* TO 'myuser'@'localhost';
FLUSH PRIVILEGES;
```

### 3. Prevent Recursive Trigger Errors

```sql
CREATE TRIGGER trg_update_orders BEFORE UPDATE ON orders
FOR EACH ROW
BEGIN
  SET NEW.total = NEW.quantity * NEW.price;  -- no self-referencing UPDATE
END;
```

### 4. Fix "Can't Update Table Used in Trigger"

```sql
-- For BEFORE triggers, use SET to modify the row
CREATE TRIGGER trg_users BEFORE INSERT ON users FOR EACH ROW
BEGIN
  SET NEW.last_login = NOW();
END;

-- For AFTER triggers, write to a different table
CREATE TRIGGER trg_users AFTER INSERT ON users FOR EACH ROW
BEGIN
  INSERT INTO user_audit (id, action, action_time) VALUES (NEW.id, 'insert', NOW());
END;
```

## Common Scenarios

- **Trigger causes slow INSERT**: Rewrite to use batch UPDATE after INSERT instead.
- **After upgrade triggers fail**: Table was renamed. Drop and recreate trigger.
- **Permission error on trigger**: Grant TRIGGER privilege to application user.

## Prevent It

- Keep trigger logic simple
- Test triggers on staging with representative data
- Document all triggers in a central registry

## Related Pages

- [MariaDB Stored Proc Error](/tools/mariadb/mariadb-stored-proc-error)
- [MariaDB Schema Error](/tools/mariadb/mariadb-schema-error)
- [MySQL Trigger Error](/tools/mysql/mysql-trigger-error)
