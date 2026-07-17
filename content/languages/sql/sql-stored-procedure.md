---
title: "[Solution] SQL Stored Procedure Error Fix"
description: "Fix 'Unknown stored procedure X' when calling a procedure that does not exist."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

This error occurs when a SQL CALL statement references a stored procedure that does not exist. The message reads: `Unknown stored procedure 'X'`.

## What This Error Means

The database cannot find a stored procedure with the specified name. This can be because the procedure was never created, was dropped, or the name is misspelled.

## Common Causes

- Procedure name is misspelled
- Procedure was dropped or never created
- Calling procedure from the wrong database
- Procedure requires specific privileges

## How to Fix

### Fix 1: Check existing procedures

```sql
SHOW PROCEDURE STATUS WHERE db = DATABASE();
-- or
SELECT routine_name, routine_type
FROM information_schema.routines
WHERE routine_type = 'PROCEDURE' AND routine_schema = DATABASE();
```

### Fix 2: Create the procedure

```sql
DELIMITER //

CREATE PROCEDURE get_user_orders(IN p_user_id INT)
BEGIN
    SELECT * FROM orders WHERE user_id = p_user_id;
END //

DELIMITER ;

-- Call it
CALL get_user_orders(42);
```

### Fix 3: Use fully qualified name

```sql
-- If procedure is in a different database
CALL my_database.get_user_orders(42);
```

## Examples

```sql
CALL process_payments();
-- ERROR 1305: PROCEDURE mydb.process_payments does not exist
```

## Related Errors

- [Trigger Error](trigger-error.md) — related programmatic SQL
- [Variable Error](variable-error.md) — unknown variable in procedure
