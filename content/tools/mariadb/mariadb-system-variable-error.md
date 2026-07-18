---
title: "[Solution] MariaDB System Variable Error — How to Fix"
description: "Fix MariaDB system variable errors including unknown variables, read-only restrictions, global vs session scope issues, and deprecated settings"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB System Variable Error

System variable errors occur when MariaDB encounters unknown variable names, attempts to modify read-only variables, or encounters deprecated settings that have been removed in newer versions.

## Why It Happens

- The variable name is misspelled or does not exist in this MariaDB version
- The variable is read-only and cannot be changed at runtime
- The value type is wrong (string for integer variable, etc.)
- The variable was deprecated and removed in the current version
- Setting a global variable without SUPER privilege
- The variable requires a restart to take effect but was set at runtime
- Conflicting variable settings between my.cnf and command line

## Common Error Messages

```
ERROR 1238 (HY000): Variable 'my_variable' is a read only variable
```

```
ERROR 1193 (HY000): Unknown system variable 'my_variable'
```

```
ERROR 1232 (42000): Incorrect argument type to variable 'my_variable'
```

```
[Warning] mysqld: variable 'my_variable' is deprecated. Use 'new_variable' instead.
```

## How to Fix It

### 1. Fix Unknown Variable Errors

```sql
-- Check if a variable exists
SHOW VARIABLES LIKE 'my_variable';

-- Search for similar variables
SHOW VARIABLES LIKE '%buffer%';

-- Check the MariaDB documentation for the correct name
SHOW VARIABLES LIKE 'innodb_buffer%';
```

### 2. Fix Read-Only Variable Errors

```sql
-- Check if a variable is read-only
SHOW VARIABLES LIKE 'my_variable';

-- For some read-only variables, they can only be set in my.cnf
-- Stop MariaDB, edit my.cnf, restart

-- For variables that can be set at runtime but only at global level
SET GLOBAL max_connections = 500;
-- This requires SUPER or SYSTEM_VARIABLES_ADMIN privilege
GRANT SUPER ON *.* TO 'admin_user'@'%';
```

### 3. Fix Value Type Errors

```sql
-- Check expected type
SHOW VARIABLES LIKE 'innodb_buffer_pool_size';

-- Set with correct type
SET GLOBAL innodb_buffer_pool_size = 4294967296;  -- BIGINT, bytes

-- For string variables
SET GLOBAL character_set_server = 'utf8mb4';

-- For boolean variables (use 0 or 1, not TRUE/FALSE)
SET GLOBAL local_infile = 1;
```

### 4. Fix Deprecated Variable Errors

```sql
-- Check for deprecated variables in the error log
-- Fix by replacing with the new variable name

-- Example: old variable name -> new variable name
-- old -> new
-- query_cache_size -> removed (use ProxySQL instead)
-- query_cache_type -> removed
-- key_buffer_size -> key_buffer_size (still valid for MyISAM)
```

```bash
# Find deprecated variables in the error log
grep -i "deprecated" /var/log/mysql/mariadb-error.log

# Common replacements in MariaDB 10.4+
# table_definition_cache -> table_definition_cache (still valid)
# thread_cache -> thread_cache_size (check the name)
```

### 5. Apply Variables That Require Restart

```sql
-- Check if a variable requires restart
SHOW VARIABLES LIKE 'innodb_buffer_pool_size';

-- Variables that require restart are marked as "No" in "Dynamic" column
-- of performance_schema.variables_info

-- To apply safely:
-- 1. Set in my.cnf
-- 2. Schedule a maintenance restart
-- 3. Or use SET PERSIST (MariaDB 10.5.9+)
SET PERSIST innodb_buffer_pool_size = 4294967296;
```

## Common Scenarios

- **Upgrade introduces new variables**: MariaDB 10.6 adds variables not present in 10.4. Update configuration files.
- **Configuration management tool sets wrong variable**: Ansible or Puppet templates reference old variable names. Update templates.
- **Runtime SET GLOBAL fails with permission error**: Grant SYSTEM_VARIABLES_ADMIN or use root account.

## Prevent It

- Review MariaDB release notes for deprecated variables before upgrading
- Use `SET PERSIST` (10.5.9+) for variables that should survive restarts
- Store variable configurations in a version-controlled configuration management tool

## Related Pages

- [MariaDB Config Error](/tools/mariadb/mariadb-config-error)
- [MariaDB InnoDB Error](/tools/mariadb/mariadb-innodb-error)
- [MySQL System Variable Error](/tools/mysql/mysql-system-variable-error)
