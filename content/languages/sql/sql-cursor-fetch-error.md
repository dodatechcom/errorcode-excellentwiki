---
title: "SQL Stored Procedure Cursor Error"
description: "Fix SQL stored procedure cursor errors when declaring, opening, or fetching from cursors incorrectly."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Cursor declared but not opened before FETCH
- FETCH before OPEN or after CLOSE
- Cursor not deallocated after use causing resource leak
- SELECT in cursor is not deterministic (no ORDER BY)
- Using cursor for operations that can be done with set-based logic

## How to Fix

```sql
-- WRONG: FETCH before OPEN
DECLARE cur CURSOR FOR SELECT id FROM employees;
FETCH NEXT FROM cur INTO @id;  -- ERROR: cursor not open

-- CORRECT: Open before fetch
DECLARE cur CURSOR FOR SELECT id FROM employees;
OPEN cur;
FETCH NEXT FROM cur INTO @id;
WHILE @@FETCH_STATUS = 0
BEGIN
    -- process @id
    FETCH NEXT FROM cur INTO @id;
END
CLOSE cur;
DEALLOCATE cur;
```

```sql
-- WRONG: Missing DEALLOCATE
DECLARE cur CURSOR FOR SELECT * FROM orders;
OPEN cur;
-- ... process ...
CLOSE cur;
-- Forgot DEALLOCATE -- resource leak!

-- CORRECT: Always deallocate
CLOSE cur;
DEALLOCATE cur;
```

## Examples

```sql
-- Example 1: Basic cursor pattern (SQL Server)
DECLARE @name VARCHAR(100)
DECLARE cur CURSOR FOR SELECT name FROM customers
OPEN cur
FETCH NEXT FROM cur INTO @name
WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT @name
    FETCH NEXT FROM cur INTO @name
END
CLOSE cur
DEALLOCATE cur

-- Example 2: Cursor with update
DECLARE @emp_id INT, @salary DECIMAL(10,2)
DECLARE sal_cur CURSOR FOR
    SELECT id, salary FROM employees WHERE dept_id = 5
FOR UPDATE OF salary
OPEN sal_cur
FETCH NEXT FROM sal_cur INTO @emp_id, @salary
WHILE @@FETCH_STATUS = 0
BEGIN
    UPDATE employees SET salary = @salary * 1.05
    WHERE CURRENT OF sal_cur
    FETCH NEXT FROM sal_cur INTO @emp_id, @salary
END
CLOSE sal_cur
DEALLOCATE sal_cur

-- Example 3: Avoid cursor with set-based approach
-- Instead of cursor, use:
UPDATE employees SET salary = salary * 1.05 WHERE dept_id = 5;
```

## Related Errors

- [Cursor error](sql-cursor-error) -- cursor-related issues
- [Stored procedure error](sql-stored-procedure) -- SP definition problems
