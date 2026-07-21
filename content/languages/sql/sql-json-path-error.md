---
title: "SQL JSON Path Expression Error"
description: "Fix SQL JSON path expression errors when querying JSON data with incorrect path syntax or missing keys."
languages: ["sql"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- JSON path syntax differs between MySQL, PostgreSQL, and SQL Server
- Using wrong accessor符号 for array vs object
- JSON path referencing non-existent key returns NULL not error
- Chained JSON functions with incompatible output types
- FOR JSON or JSON_OBJECT with invalid key names

## How to Fix

```sql
-- WRONG: MySQL JSON path with SQL Server syntax
SELECT JSON_VALUE(data, '$.name') FROM users;
-- MySQL uses JSON_EXTRACT

-- CORRECT: MySQL syntax
SELECT JSON_EXTRACT(data, '$.name') FROM users;
-- or shorthand
SELECT data->'$.name' FROM users;
```

```enrl
-- WRONG: PostgreSQL JSON operator with wrong type
SELECT data->>'name' FROM users WHERE data->'age' > 25;
-- ERROR: operator does not exist: text > integer

-- CORRECT: Cast appropriately
SELECT data->>'name' FROM users WHERE (data->>'age')::int > 25;
```

## Examples

```sql
-- Example 1: MySQL JSON extraction
SELECT
    JSON_EXTRACT(data, '$.name') AS name,
    JSON_EXTRACT(data, '$.address.city') AS city
FROM users;

-- Example 2: PostgreSQL JSON operators
SELECT
    data->>'name' AS name,
    data->'address'->>'city' AS city,
    data->'hobbies'->0 AS first_hobby
FROM users;

-- Example 3: JSON aggregation
SELECT JSON_OBJECTAGG(name, salary) AS salary_map
FROM employees;
```

## Related Errors

- [JSON error](sql-json-error) -- JSON parsing issues
- [SQL JSON error](sql-json-error) -- JSON data problems
