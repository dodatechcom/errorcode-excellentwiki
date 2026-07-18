---
title: "[Solution] SQL Invalid JSON In JSON Function Error Fix"
description: "Fix 'invalid JSON' errors in SQL JSON functions. Resolve malformed JSON strings and JSON parsing issues in database queries."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQL Invalid JSON In JSON Function Error Fix

The `invalid JSON` error occurs when a JSON function receives a string that is not valid JSON, causing parsing to fail.

## What This Error Means

SQL JSON functions (JSON_EXTRACT, JSONB_PARSE, json_extract, etc.) require properly formatted JSON input. Malformed strings with missing quotes, trailing commas, or unescaped characters cause parse errors.

A typical error:

```
ERROR: invalid input syntax for type json
DETAIL: Token "hello" is invalid.
```

## Why It Happens

Common causes include:

- **Trailing commas** — `{"a": 1,}` is invalid JSON.
- **Unquoted keys** — `{name: "test"}` instead of `{"name": "test"}`.
- **Single quotes** — `{'key': 'value'}` instead of `{"key": "value"}`.
- **Unescaped characters** — Newlines or tabs inside strings.
- **Empty strings** — Passing empty string to JSON function.
- **Non-JSON data** — Column contains plain text, not JSON.

## How to Fix It

### Fix 1: Validate JSON before parsing

```sql
-- RIGHT: Check validity first
SELECT * FROM events
WHERE json_data::text IS NOT NULL
AND json_data::text ~ '^[\[{]';
```

### Fix 2: Fix common JSON issues in data

```sql
-- Remove trailing commas using replace
SELECT json_column::jsonb 
FROM (
    SELECT REPLACE(REPLACE(data, ',}', '}'), ',]', ']') AS data
    FROM raw_events
) sub;
```

### Fix 3: Use proper JSON syntax

```sql
-- WRONG: Invalid JSON
SELECT '{"name": "test",}'::json;

-- RIGHT: Valid JSON
SELECT '{"name": "test"}'::json;

-- WRONG: Single quotes
SELECT "{'key': 'value'}"::json;

-- RIGHT: Double quotes
SELECT '{"key": "value"}'::json;
```

### Fix 4: Handle NULL and empty values

```sql
-- RIGHT: Check before parsing
SELECT CASE 
    WHEN json_column IS NULL THEN NULL
    WHEN json_column = '' THEN NULL
    ELSE json_column::jsonb
END
FROM my_table;
```

### Fix 5: Use JSON functions safely

```sql
-- RIGHT: Use jsonb functions for better error handling
-- PostgreSQL
SELECT jsonb_extract_path_text(data, 'key')
FROM events
WHERE jsonb_typeof(data) = 'object';

-- MySQL
SELECT JSON_EXTRACT(data, '$.key')
FROM events
WHERE JSON_VALID(data);
```

## Common Mistakes

- **Assuming all data is valid JSON** — Always validate before parsing.
- **Using text functions to manipulate JSON** — Use JSON-specific functions.
- **Not handling encoding issues** — UTF-8 BOM or encoding errors break JSON parsing.

## Related Pages

- [SQL XML Error](sql-xml-error) — XML parsing issues
- [SQL View Error](sql-view-error) — View-related issues
- [SQL Constraint Error](sql-constraint-error) — Constraint violations
