---
title: "[Solution] MariaDB Character Set Error — How to Fix"
description: "Fix MariaDB character set and collation errors including encoding mismatches, emoji support, and column-level charset conflicts"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Character Set Error

Character set errors occur when the client, connection, or database uses incompatible character encodings. This leads to data truncation, garbled text, and failed inserts of multi-byte characters.

## Why It Happens

- The client sends data in a different charset than the server expects
- The database was created with `latin1` but data is in `utf8mb4`
- Emoji and 4-byte Unicode cannot fit in `utf8` (3-byte max)
- Two tables with different collations are JOINed on a character column
- PHP, Python, or Java drivers default to `latin1`

## Common Error Messages

```
ERROR 1366 (HY007): Incorrect string value: '\xF0\x9F\x98\x80' for column 'bio' at row 1
```

```
ERROR 1267 (HY000): Illegal mix of collations (utf8mb4_unicode_ci,IMPLICIT) and
(latin1_swedish_ci,IMPLICIT) for operation '='
```

```
Warning: 1265 Data truncated for column 'name' at row 1
```

```
ERROR 1300 (HY000): Invalid utf8mb4 character string: 'F09F98'
```

## How to Fix It

### 1. Set Server-Wide Charset to utf8mb4

```ini
[mysqld]
character_set_server = utf8mb4
collation_server = utf8mb4_unicode_ci

[client]
default-character-set = utf8mb4
```

### 2. Fix Existing Database Charset

```sql
ALTER DATABASE mydb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE users CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE users MODIFY COLUMN name VARCHAR(255)
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. Fix Connection Charset

```sql
SET NAMES utf8mb4;

-- PHP: $pdo->exec("SET NAMES utf8mb4");
-- Python: cursor.execute("SET NAMES utf8mb4")
-- Java: jdbc:mariadb://host/db?characterEncoding=UTF-8&useUnicode=true
```

### 4. Fix Collation Mismatch in JOINs

```sql
SELECT * FROM t1 JOIN t2
  ON t1.name = CONVERT(t2.name USING utf8mb4) COLLATE utf8mb4_unicode_ci;

-- Or fix the table definition
ALTER TABLE t2 MODIFY COLUMN name VARCHAR(255)
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## Common Scenarios

- **Emoji insert fails**: Convert to `utf8mb4` with `utf8mb4_unicode_ci` collation.
- **Collation error after migration**: Convert all tables from `latin1` to `utf8mb4`.
- **Application displays garbled characters**: Set `SET NAMES utf8mb4` at connection time.

## Prevent It

- Always use `utf8mb4` instead of `utf8`
- Set `character_set_server = utf8mb4` in my.cnf
- Test emoji insertion: `INSERT INTO test (val) VALUES ('🚀');`

## Related Pages

- [MariaDB Schema Error](/tools/mariadb/mariadb-schema-error)
- [MariaDB Import Error](/tools/mariadb/mariadb-import-error)
- [MySQL Charset Error](/tools/mysql/mysql-charset-error)
