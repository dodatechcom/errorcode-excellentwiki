---
title: "[Solution] SQL Unknown System Variable Fix"
description: "Fix 'Unknown system variable X' when referencing a non-existent or deprecated system variable."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["system-variable", "session", "global", "configuration"]
weight: 5
---

This error occurs when a SQL statement references a system variable that does not exist or is not recognized by the current database version. The message reads: `Unknown system variable 'X'`.

## What This Error Means

The database does not have a system variable with the specified name. This can happen when using deprecated variables, version-specific variables, or misspelled variable names.

## Common Causes

- Variable name is misspelled
- Variable was deprecated or removed in the current version
- Using GLOBAL instead of SESSION or vice versa
- Variable requires a specific plugin or extension

## How to Fix

### Fix 1: Check available variables

```sql
SHOW GLOBAL VARIABLES LIKE '%timeout%';
SHOW SESSION VARIABLES LIKE '%autocommit%';
```

### Fix 2: Use correct variable name

```sql
-- Wrong: deprecated variable
SET GLOBAL query_cache_size = 1048576;

-- Correct for MySQL 8.0+: removed, use performance_schema
SET SESSION max_connections = 100;
```

### Fix 3: Check version compatibility

```sql
-- See current version
SELECT VERSION();

-- Use variables appropriate for this version
SHOW VARIABLES LIKE 'innodb_%';
```

## Examples

```sql
SET GLOBAL storage_engine = InnoDB;
-- ERROR 1193: Unknown system variable 'storage_engine'
-- storage_engine was renamed to default_storage_engine
```

## Related Errors

- [Unknown Function](unknown-function.md) — function not recognized
- [Syntax Error](syntax-error.md) — malformed SQL
