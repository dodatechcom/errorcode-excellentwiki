---
title: "[Solution] SQL Stored Procedure Not Found Error Fix"
description: "Fix 'stored procedure not found' in SQL. Troubleshoot missing procedures, schema issues, and permission errors in databases."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQL Stored Procedure Not Found Error Fix

The `stored procedure not found` error occurs when calling a procedure that does not exist, has been dropped, or is in a different schema.

## What This Error Means

Stored procedures are precompiled SQL code stored in the database. When you call a procedure that the database cannot locate, it throws this error. This is similar to calling a function that does not exist.

A typical error:

```
ERROR: procedure sales.update_inventory(character varying) does not exist
```

## Why It Happens

Common causes include:

- **Procedure was dropped** — The procedure no longer exists.
- **Wrong schema** — Procedure exists in a different schema.
- **Typo in procedure name** — Misspelled name or wrong case.
- **Missing parameters** — Wrong number or type of arguments.
- **Database migration incomplete** — Procedure was not created in target environment.

## How to Fix It

### Fix 1: Check if procedure exists

```sql
-- PostgreSQL
SELECT routine_name, routine_schema 
FROM information_schema.routines 
WHERE routine_type = 'PROCEDURE' 
AND routine_name = 'update_inventory';

-- SQL Server
SELECT name FROM sys.procedures WHERE name = 'update_inventory';

-- MySQL
SHOW PROCEDURE STATUS WHERE Name = 'update_inventory';
```

### Fix 2: Create the procedure

```sql
-- RIGHT: Create procedure with correct signature
CREATE OR REPLACE PROCEDURE update_inventory(
    product_id VARCHAR(50),
    quantity INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE inventory 
    SET stock = stock - quantity 
    WHERE id = product_id;
END;
$$;
```

### Fix 3: Use correct schema and name

```sql
-- WRONG: Missing schema
CALL update_inventory('P001', 5);

-- RIGHT: Include schema
CALL public.update_inventory('P001', 5);
```

### Fix 4: Match parameter types exactly

```sql
-- WRONG: Type mismatch
CALL update_inventory(1, 5);  -- Expects VARCHAR, not INT

-- RIGHT: Correct types
CALL update_inventory('1', 5);
```

### Fix 5: Grant execute permission

```sql
-- Grant permission to call procedure
GRANT EXECUTE ON PROCEDURE update_inventory(VARCHAR, INT) TO app_user;
```

## Common Mistakes

- **Case sensitivity** — Some databases treat `Update_Inventory` and `update_inventory` differently.
- **Not checking schema** — Procedures live in specific schemas.
- **Assuming procedures auto-update** — They must be re-created after schema changes.

## Related Pages

- [SQL View Error](sql-view-error) — View does not exist issues
- [SQL Trigger Error](sql-trigger-error) — Trigger execution issues
- [SQL Cursor Error](sql-cursor-error) — Cursor operation issues
