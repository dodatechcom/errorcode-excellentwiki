---
title: "[Solution] MariaDB Character Set Error"
description: "Fix MariaDB character set errors when encoding mismatches cause data corruption"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Character Set Error

Character set errors occur when MariaDB encounters encoding mismatches between connection and storage.

## Common Causes

- Client sending data in different charset than server
- Table created with wrong character set
- Implicit conversion losing data
- Binary data stored in text column

## Common Error Messages

```
ERROR 1366 (HY000): Incorrect string value
```

## How to Fix It

### 1. Check Character Set

```sql
SHOW VARIABLES LIKE 'character_set%';
```

### 2. Convert Table Character Set

```sql
ALTER TABLE my_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. Set Connection Charset

```sql
SET NAMES utf8mb4;
```

## Examples

```sql
SELECT TABLE_NAME, CCSA.CHARACTER_SET_NAME, CCSA.COLLATION_NAME
FROM information_schema.TABLE_CONSTRAINTS tc
JOIN information_schema.COLLATION_CHARACTER_SET_APPLICABILITY CCSA
ON tc.CONSTRAINT_SCHEMA = CCSA.COLLATION_NAME;
```
