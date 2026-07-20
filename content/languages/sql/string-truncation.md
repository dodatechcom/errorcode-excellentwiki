---
title: "[Solution] String Data Right Truncation"
description: "Fix 'String data right truncation' when a value is too long for a VARCHAR column."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "data-type, string, truncation"]
severity: "error"
---

# String Data Right Truncation

## Error Message

```
ERROR 1406: Data too long for column 'X' at row 1 — The string value exceeds the maximum length defined for the column.
```

## Common Causes

- INSERT or UPDATE value is longer than the VARCHAR column's defined maximum length
- Character encoding differences cause the byte length to exceed the column size (e.g., UTF-8 multi-byte characters)
- Concatenation of multiple columns produces a string longer than the target column
- Data import from CSV or another source contains values that exceed the column definition

## Solutions

### Solution 1: Increase the column length

Alter the table to allow longer strings in the column.

```sql
-- MySQL: increase column length
ALTER TABLE users MODIFY COLUMN bio TEXT;

-- Or increase VARCHAR limit
ALTER TABLE users MODIFY COLUMN bio VARCHAR(2000);

-- PostgreSQL: increase column length
ALTER TABLE users ALTER COLUMN bio TYPE VARCHAR(2000);

-- SQL Server: increase column length
ALTER TABLE users ALTER COLUMN bio NVARCHAR(MAX);
```

### Solution 2: Truncate strings before inserting

Use substring functions to ensure values fit within the column length.

```sql
-- MySQL: truncate to column length
INSERT INTO users (name, bio)
SELECT name, LEFT(bio, 500) FROM staging_users;

-- PostgreSQL: use SUBSTRING
INSERT INTO users (name, bio)
SELECT name, SUBSTRING(bio FROM 1 FOR 500) FROM staging_users;

-- SQL Server: use LEFT or SUBSTRING
INSERT INTO users (name, bio)
SELECT name, LEFT(bio, 500) FROM staging_users;

-- Check for values that are too long
SELECT name, LENGTH(bio) as bio_length
FROM staging_users
WHERE LENGTH(bio) > 500;
```

### Solution 3: Use TEXT or CLOB for unlimited-length strings

For fields that can be very long, use the TEXT data type instead of VARCHAR.

```sql
-- MySQL: use TEXT type
ALTER TABLE users MODIFY COLUMN bio TEXT;

-- PostgreSQL: use TEXT type (unlimited length)
ALTER TABLE users ALTER COLUMN bio TYPE TEXT;

-- SQL Server: use NVARCHAR(MAX) or VARCHAR(MAX)
ALTER TABLE users ALTER COLUMN bio NVARCHAR(MAX);

-- Create table with appropriate types from the start
CREATE TABLE articles (
    id INT PRIMARY KEY,
    title VARCHAR(200),
    summary VARCHAR(1000),
    content TEXT
);
```

## Prevention Tips

- Account for multi-byte UTF-8 characters when defining VARCHAR lengths — a VARCHAR(255) column stores 255 characters, not bytes
- Use TEXT or CLOB types for fields that can have variable or very long content
- Validate string lengths in application code before inserting into the database

## Related Errors

- [Unicode Error]({{< relref "/languages/sql/unicode-error.md" >}})
- [Data Type Mismatch]({{< relref "/languages/sql/data-type-mismatch.md" >}})
- [Data Truncation]({{< relref "/languages/sql/data-truncation.md" >}})
