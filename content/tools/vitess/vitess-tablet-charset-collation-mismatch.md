---
title: "[Solution] Vitess Tablet Charset Collation Mismatch"
description: "Fix Vitess charset and collation mismatch errors between vtgate and tablet MySQL"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Charset Collation Mismatch

Charset collation mismatch errors occur when vtgate expects one character set but the tablet MySQL uses a different one.

## Common Causes

- Tablet MySQL character_set_server differs from vtgate setting
- Table created with utf8mb3 but queries use utf8mb4
- Connection charset not matching table collation
- VSchema charset rules misconfigured

## How to Fix

Set consistent charset:

```sql
SET GLOBAL character_set_server = 'utf8mb4';
SET GLOBAL collation_server = 'utf8mb4_unicode_ci';
```

Configure vtgate charset:

```bash
vtgate -mysql_server_collation utf8mb4_unicode_ci -normalize_queries=false
```

Check table charset:

```sql
SELECT TABLE_NAME, CCSA.CHARACTER_SET_NAME, CCSA.COLLATION_NAME
FROM information_schema.TABLE_CONSTRAINTS tc
JOIN information_schema.COLLATION_CHARACTER_SET_APPLICABILITY CCSA ON tc.CONSTRAINT_SCHEMA = CCSA.COLLATION_NAME;
```

## Examples

```sql
SHOW VARIABLES LIKE 'character_set%';
```
