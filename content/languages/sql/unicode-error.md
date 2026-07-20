---
title: "[Solution] Unicode Encoding Error"
description: "Fix 'Unicode encoding error' when character encoding issues cause data corruption or insertion failures."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "data-type, unicode, encoding"]
severity: "error"
---

# Unicode Encoding Error

## Error Message

```
ERROR 1365: Division by 0 / Incorrect string value: '\xF0\x9F\x98\x80' for column 'X' — The string contains characters that cannot be encoded in the column's character set.
```

## Common Causes

- Column uses a character set (like latin1) that does not support Unicode characters
- Emoji or multi-byte UTF-8 characters are being inserted into a non-UTF-8 column
- Connection character set does not match the database or table character set
- Data is being transferred between systems with different encodings

## Solutions

### Solution 1: Convert the table to UTF-8 encoding

Change the character set and collation to support Unicode.

```sql
-- MySQL: convert table to utf8mb4
ALTER TABLE users CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- MySQL: convert database
ALTER DATABASE mydb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- PostgreSQL: databases use UTF-8 by default, but check
SHOW server_encoding;

-- SQL Server: use NVARCHAR for Unicode
ALTER TABLE users ALTER COLUMN name NVARCHAR(200);
```

### Solution 2: Use NVARCHAR or TEXT for Unicode columns

Use Unicode-aware data types for columns that store international text or emoji.

```sql
-- MySQL: use utf8mb4 for columns with emoji
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(200) CHARACTER SET utf8mb4,
    bio TEXT CHARACTER SET utf8mb4
);

-- PostgreSQL: TEXT supports all Unicode natively
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    bio TEXT
);

-- SQL Server: use NVARCHAR for Unicode
CREATE TABLE users (
    id INT PRIMARY KEY,
    name NVARCHAR(200),
    bio NVARCHAR(MAX)
);
```

### Solution 3: Set connection character set correctly

Ensure the client connection uses the same encoding as the database.

```sql
-- MySQL: set connection charset
SET NAMES utf8mb4;

-- Or in connection string
-- jdbc:mysql://localhost/mydb?characterEncoding=UTF-8&connectionCollation=utf8mb4_unicode_ci

-- PostgreSQL: set client encoding
SET client_encoding TO 'UTF8';

-- SQL Server: set connection encoding
-- Use nvarchar parameters in queries
SELECT * FROM users WHERE name = N'Unicode Name 你好';
```

## Prevention Tips

- Always use utf8mb4 character set in MySQL for full Unicode support including emoji
- Use NVARCHAR in SQL Server whenever you need to store international text
- Set the connection character set to match the database to prevent encoding mismatches during data transfer

## Related Errors

- [String Truncation]({{< relref "/languages/sql/string-truncation.md" >}})
- [Data Type Mismatch]({{< relref "/languages/sql/data-type-mismatch.md" >}})
- [Unicode Error]({{< relref "/languages/sql/unicode-error.md" >}})
