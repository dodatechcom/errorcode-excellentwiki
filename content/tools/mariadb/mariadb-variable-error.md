---
title: "[Solution] MariaDB Variable Error"
description: "Fix MariaDB system variable errors when SET or SHOW VARIABLE operations fail"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Variable Error

Variable errors occur when MariaDB cannot read or write system variables correctly.

## Common Causes

- Variable does not exist in MariaDB version
- Variable value out of allowed range
- Read-only variable attempted to be modified
- Variable scope issue (global vs session)

## Common Error Messages

```
ERROR 1238 (HY000): Variable is a NON SESSION variable
```

## How to Fix It

### 1. Check Variable Scope

```sql
SHOW GLOBAL VARIABLES LIKE 'max_connections';
SHOW SESSION VARIABLES LIKE 'autocommit';
```

### 2. Set Variable Correctly

```sql
SET GLOBAL max_connections = 500;
SET SESSION wait_timeout = 28800;
```

### 3. Check Variable Value

```sql
SELECT @@global.max_connections;
SELECT @@session.wait_timeout;
```

## Examples

```sql
SHOW VARIABLES WHERE Variable_name LIKE '%timeout%' ORDER BY Variable_name;
```
