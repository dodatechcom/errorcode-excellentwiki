---
title: "[Solution] MariaDB Stored Procedure Error"
description: "Fix MariaDB stored procedure errors when procedure creation or execution fails"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Stored Procedure Error

Stored procedure errors occur when MariaDB encounters issues creating or executing stored procedures.

## Common Causes

- SQL syntax error in procedure body
- Missing delimiter for procedure definition
- Variable scope conflict with parameters
- Procedure references dropped table

## Common Error Messages

```
ERROR 1064 (42000): You have an error in your SQL syntax
```

## How to Fix It

### 1. Check Procedure Definition

```sql
SHOW CREATE PROCEDURE my_proc;
```

### 2. Use Correct Delimiter

```sql
DELIMITER //
CREATE PROCEDURE my_proc(IN param INT)
BEGIN
  SELECT * FROM my_table WHERE id = param;
END //
DELIMITER ;
```

### 3. Fix Variable Scope

```sql
CREATE PROCEDURE my_proc()
BEGIN
  DECLARE local_var INT DEFAULT 0;
  SET local_var = local_var + 1;
  SELECT local_var;
END;
```

## Examples

```sql
CALL my_proc(42);
```
