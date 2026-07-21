---
title: "[Solution] MySQL JSON Type Error"
description: "Fix MySQL JSON type error when inserting or manipulating JSON data fails due to type mismatches or invalid syntax"
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
---

# MySQL JSON Type Error

JSON operations fail because the input is not valid JSON, the column type is not JSON, or the JSON path expression references a non-existent element.

## Common Causes

- Inserting a non-JSON string into a JSON column
- JSON path expression points to a missing key
- Attempting to CAST incompatible data to JSON
- JSON function receives NULL or invalid arguments
- Double-encoding: inserting JSON-escaped string into JSON column

## How to Fix

### Validate JSON Before Insert

```sql
-- MySQL validates JSON automatically, but check manually
SELECT JSON_VALID('{"name": "test"}');  -- returns 1
SELECT JSON_VALID('not json');          -- returns 0
```

### Insert Proper JSON

```sql
-- Correct: valid JSON string
INSERT INTO configs (settings) VALUES ('{"theme": "dark", "lang": "en"}');

-- Correct: using JSON function
INSERT INTO configs (settings) VALUES (JSON_OBJECT('theme', 'dark', 'lang', 'en'));
```

### Use JSON Extract Safely

```sql
-- Safe extraction with NULL fallback
SELECT
  JSON_UNQUOTE(JSON_EXTRACT(settings, '$.theme')) AS theme,
  JSON_UNQUOTE(JSON_EXTRACT(settings, '$.missing', '$.default')) AS fallback
FROM configs;

-- Shorthand syntax
SELECT settings->>'$.theme' FROM configs;
```

### Fix Double-Encoded JSON

```sql
-- Bad: JSON string is double-encoded
INSERT INTO configs (settings) VALUES ('"{\\"theme\\": \\"dark\\"}"');

-- Good: insert raw JSON
INSERT INTO configs (settings) VALUES ('{"theme": "dark"}');

-- Fix existing double-encoded data
UPDATE configs
SET settings = CAST(settings AS JSON);
```

### Handle JSON Path Errors

```sql
-- Use JSON_VALID and JSON_CONTAINS_PATH to check before extracting
SELECT
  CASE
    WHEN JSON_CONTAINS_PATH(settings, 'one', '$.theme')
    THEN settings->>'$.theme'
    ELSE 'default'
  END AS theme
FROM configs;
```

## Examples

```
ERROR 3140 (22032): Invalid JSON text:
  "Invalid value." at position 1 in value for column 'settings'.

ERROR 3141 (22032): Invalid JSON path expression at position 5
  in function json_extract for argument settings: "$.them"
```

## Related Errors

- [MySQL Invalid Input Syntax]({{< relref "/tools/mysql/mysql-syntax-error" >}}) -- syntax issues
- [MySQL Data Truncated]({{< relref "/tools/mysql/mysql-data-truncated" >}}) -- truncation
- [MySQL Subquery Return More]({{< relref "/tools/mysql/mysql-subquery-return-more" >}}) -- subquery issues
