---
title: "[Solution] MariaDB JSON Error — How to Fix"
description: "Fix MariaDB JSON function errors including invalid JSON syntax, path expression issues, and JSON column type conversion problems"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB JSON Error

JSON errors occur when using the JSON data type (MariaDB 10.2+) or JSON functions like `JSON_EXTRACT`, `JSON_SET`, and `JSON_SEARCH`. Errors result from invalid JSON syntax, incorrect path expressions, or version limitations.

## Why It Happens

- The JSON string is malformed (missing brackets, trailing commas)
- The JSON path expression is syntactically incorrect
- MariaDB version is older than 10.2
- A JSON path references a non-existent key
- `JSON_EXTRACT` returns NULL because path does not match
- Trying to use JSON as a key in JOIN without extracting first

## Common Error Messages

```
ERROR 3141 (22032): Invalid JSON text in argument 1 to function json_extract
```

```
ERROR 4161 (HY000): Unknown JSON path expression in the given string
```

```
ERROR 3156 (22001): Invalid JSON value for CAST to INT at row 1
```

```
ERROR 4044 (HY000): Not a valid JSON path expression
```

## How to Fix It

### 1. Validate JSON Before Inserting

```sql
SELECT JSON_VALID('{"name": "John", "age": 30}');  -- 1
SELECT JSON_VALID('{name: John}');  -- 0

DELIMITER //
CREATE TRIGGER validate_json BEFORE INSERT ON products
FOR EACH ROW
BEGIN
  IF NOT JSON_VALID(NEW.attributes) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid JSON';
  END IF;
END//
DELIMITER ;
```

### 2. Fix JSON Path Expressions

```sql
SELECT JSON_EXTRACT('{"a": {"b": 1}}', '$.a.b');
SELECT JSON_EXTRACT('[1, 2, 3]', '$[0]');
SELECT JSON_UNQUOTE(JSON_EXTRACT('{"name": "John"}', '$.name'));
SELECT '{"name": "John"}'->>'$.name';
```

### 3. Insert Valid JSON Data

```sql
INSERT INTO products (id, attributes) VALUES (1,
  JSON_OBJECT('color', 'red', 'size', 'L', 'weight', 1.5)
);
```

### 4. Query JSON Columns Efficiently

```sql
ALTER TABLE products ADD COLUMN color VARCHAR(50)
  GENERATED ALWAYS AS (JSON_UNQUOTE(JSON_EXTRACT(attributes, '$.color'))) VIRTUAL;
CREATE INDEX idx_color ON products (color);
SELECT * FROM products WHERE color = 'red';
```

## Common Scenarios

- **Migration from VARCHAR to JSON fails**: Clean data first with validation.
- **JSON_EXTRACT returns NULL**: Inspect structure with `JSON_KEYS`.
- **Application sends invalid JSON**: Fix serialization in app code.

## Prevent It

- Use `JSON_VALID()` in CHECK constraints
- Create virtual generated columns with indexes for frequent queries
- Test JSON functions on staging with realistic data

## Related Pages

- [MariaDB Schema Error](/tools/mariadb/mariadb-schema-error)
- [MariaDB Import Error](/tools/mariadb/mariadb-import-error)
- [MySQL JSON Error](/tools/mysql/mysql-json-error)
