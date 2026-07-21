---
title: "SQL Wildcard LIKE Escaping Special Characters Error"
description: "Fix SQL LIKE clause errors when special characters like % _ [ are not properly escaped in pattern matching."
languages: ["sql"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Using % or _ in search string without escaping
- LIKE pattern with square brackets on non-SQL-Server databases
- Searching for literal % or _ without ESCAPE clause
- LIKE with NULL values always returns NULL
- Case sensitivity differences across databases

## How to Fix

```sql
-- WRONG: % in search string matches everything
SELECT * FROM products WHERE name LIKE '%100%';
-- Matches "100 widgets", "Widget 100", "100%", etc.

-- CORRECT: Escape special characters
SELECT * FROM products WHERE name LIKE '%100/%%' ESCAPE '/';
-- Matches only strings containing literal "100%"
```

```sql
-- WRONG: LIKE with NULL
SELECT * FROM users WHERE nickname LIKE '%test%';
-- Rows with NULL nickname are excluded

-- CORRECT: Handle NULLs
SELECT * FROM users
WHERE nickname LIKE '%test%' OR nickname IS NULL;
```

## Examples

```sql
-- Example 1: Search for literal underscore
SELECT * FROM codes WHERE code LIKE '%\_%' ESCAPE '\';

-- Example 2: SQL Server bracket escaping
SELECT * FROM products WHERE name LIKE '%[%]%%';
-- Matches "100%"

-- Example 3: Case-insensitive LIKE
SELECT * FROM users WHERE name LIKE '%smith%' COLLATE SQL_Latin1_General_CP1_CI_AS;
-- PostgreSQL: use ILIKE
SELECT * FROM users WHERE name ILIKE '%smith%';
```

## Related Errors

- [String truncation error](string-truncation) -- string size issues
- [Unicode error](unicode-error) -- character encoding problems
