---
title: "[Solution] PostgreSQL Configuration Parameter Error"
description: "Fix PostgreSQL configuration parameter errors. Resolve invalid parameter names or values in postgresql.conf."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
---

# PostgreSQL Configuration Parameter Error

ERROR: unrecognized configuration parameter

This error occurs when PostgreSQL encounters an unknown or deprecated parameter name in the configuration file or during a SET command.

## Common Causes

- Typo in parameter name in postgresql.conf
- Using a parameter from a different PostgreSQL major version
- Custom GUC parameters require a module prefix

## How to Fix

1. Verify the parameter exists in your PostgreSQL version:

```sql
SELECT name, setting FROM pg_settings WHERE name LIKE '%work_mem%';
```

2. Check the configuration file for typos:

```bash
grep -n 'parameter_name' /etc/postgresql/*/main/postgresql.conf
```

3. For extension-specific parameters, use the correct prefix:

```sql
-- Wrong
SET custom_param = 'value';

-- Correct (with extension prefix)
SET myextension.custom_param = 'value';
```

## Examples

```sql
-- Reset a parameter to its default
RESET work_mem;

-- Show current value of a parameter
SHOW shared_buffers;

-- Set a parameter with unit
SET maintenance_work_mem = '512MB';
```
