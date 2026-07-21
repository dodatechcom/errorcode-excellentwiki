---
title: "[Solution] MariaDB Union Error"
description: "Fix MariaDB UNION errors when combining SELECT statements fails"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB UNION Error

UNION errors occur when MariaDB cannot combine results from multiple SELECT statements.

## Common Causes

- Column count mismatch between SELECT statements
- Column type incompatibility across SELECTs
- UNION ALL vs UNION (duplicate removal) confusion
- ORDER BY referencing non-existent column

## Common Error Messages

```
ERROR 1222 (21000): The used SELECT statements have a different number of columns
```

## How to Fix It

### 1. Match Column Count

```sql
SELECT id, name FROM users
UNION ALL
SELECT id, name FROM archived_users;
```

### 2. Use NULL for Missing Columns

```sql
SELECT id, name, email FROM users
UNION ALL
SELECT id, name, NULL AS email FROM old_users;
```

### 3. Use UNION with ORDER BY

```sql
(SELECT id, name FROM users ORDER BY name LIMIT 10)
UNION
(SELECT id, name FROM archived_users ORDER BY name LIMIT 10)
ORDER BY name;
```

## Examples

```sql
SELECT 'active' AS status, count(*) FROM users WHERE active = 1
UNION
SELECT 'inactive', count(*) FROM users WHERE active = 0;
```
