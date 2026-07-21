---
title: "[Solution] TiDB JSON Function Error — How to Fix"
description: "Fix TiDB JSON function errors when JSON data manipulation functions fail due to syntax or type issues"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB JSON Function Error

JSON function errors occur when TiDB's JSON data manipulation functions fail due to invalid JSON syntax, unsupported operations, or type mismatches.

## Why It Happens

- JSON path expression is malformed
- JSON document is not valid JSON
- Operation attempts to modify a JSON path that does not exist
- JSON type is incompatible with the requested function
- JSON document exceeds the maximum size limit

## Common Error Messages

```
ERROR 3156: Invalid JSON value for CAST
```

```
ERROR 3152: Invalid JSON path expression
```

```
error: JSON document exceeds maximum depth
```

## How to Fix It

### 1. Validate JSON Syntax

```sql
SELECT JSON_VALID('{"name": "Alice", "age": 30}');
```

### 2. Fix JSON Path Expression

```sql
-- Use correct path syntax
SELECT JSON_EXTRACT('{"a": {"b": 1}}', '$.a.b');

-- Use JSON_UNQUOTE for string values
SELECT JSON_UNQUOTE(JSON_EXTRACT(data, '$.name')) FROM mytable;
```

### 3. Use JSON Functions Correctly

```sql
-- Insert JSON data
INSERT INTO mytable (id, data) VALUES (1, '{"name": "Alice", "scores": [90, 85, 92]}');

-- Query JSON data
SELECT JSON_EXTRACT(data, '$.name') AS name FROM mytable;

-- Update JSON data
UPDATE mytable SET data = JSON_SET(data, '$.age', 31) WHERE id = 1;
```

### 4. Check JSON Size

```sql
SELECT LENGTH(JSON_QUOTE(data)) FROM mytable WHERE id = 1;
```

## Examples

```
mysql> SELECT JSON_EXTRACT('{"name": "Alice", "scores": [90, 85, 92]}', '$.scores[0]');
+------------------------------------------------------+
| JSON_EXTRACT('{"name": "Alice", "scores": [90, 85, 92]}', '$.scores[0]') |
+------------------------------------------------------+
| 90                                                   |
+------------------------------------------------------+
```

## Prevent It

- Validate JSON before inserting into the database
- Use consistent JSON path syntax
- Consider normalizing frequently queried JSON fields

## Related Pages

- [TiDB JSON Error](/tools/tidb/tidb-json-error)
- [TiDB Statement Error](/tools/tidb/tidb-statement-error)
- [TiDB Query Error](/tools/tidb/tidb-query-error)
