---
title: "[Solution] SQL Unknown Stored Procedure Error Fix"
description: "Fix SQL stored procedure errors when calling a procedure that doesn't exist."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQL Unknown Stored Procedure Error Fix

A SQL stored procedure error occurs when you try to call a stored procedure that doesn't exist in the current database.

## What This Error Means

The database cannot find the specified stored procedure. This happens when the procedure hasn't been created, was dropped, or you're querying the wrong database.

## Common Causes

- Procedure not created yet
- Wrong database selected
- Procedure was dropped
- Typo in procedure name
- Missing schema prefix

## How to Fix

### 1. Check if procedure exists

```sql
-- CORRECT: Verify procedure exists
SHOW PROCEDURE STATUS WHERE Db = DATABASE();
SELECT * FROM information_schema.ROUTINES
WHERE ROUTINE_TYPE = 'PROCEDURE' AND ROUTINE_SCHEMA = DATABASE();
```

### 2. Create the stored procedure

```sql
-- CORRECT: Create procedure
DELIMITER //
CREATE PROCEDURE GetUser(IN userId INT)
BEGIN
    SELECT * FROM users WHERE id = userId;
END //
DELIMITER ;

-- Call it
CALL GetUser(1);
```

### 3. Use correct database

```sql
-- CORRECT: Specify database
CALL mydb.GetUser(1);
-- Or
USE mydb;
CALL GetUser(1);
```

### 4. Check procedure parameters

```sql
-- CORRECT: Match parameter types
-- If procedure expects INT, don't pass string
CALL GetUser(1);  -- Correct
-- CALL GetUser('abc');  -- Wrong type
```

## Related Errors

- [SQL Table Not Found](sql-table-not-found-v2) — table missing
- [SQL Access Denied](sql-access-denied-v2) — permission errors
- [SQL Syntax Error](sql-syntax-error-v2) — syntax issues
