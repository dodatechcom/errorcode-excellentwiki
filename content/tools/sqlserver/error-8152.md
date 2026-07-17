---
title: "[Solution] SQL Server Error 8152: String or Binary Data Would Be Truncated"
description: "Fix SQL Server Error 8152 truncation errors. Resolve data too long for column issues."
tools: ["sqlserver"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Error 8152: String or Binary Data Would Be Truncated

Error 8152 occurs when an INSERT or UPDATE tries to store data that exceeds the defined size of the target column. SQL Server blocks the operation to prevent data loss.

## Common Causes

- The source data is longer than the column's defined size
- Multi-byte character encoding requires more bytes than expected
- The column size was defined too small for the expected data
- Implicit conversion from a larger type causes expansion

## How to Fix

### Find the Truncated Column

```sql
-- SQL Server 2019+ has detailed truncation errors
-- Enable: ALTER DATABASE SCOPED CONFIGURATION SET VERBOSE_TRUNCATION_WARNINGS = ON;

-- Check column sizes
SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'your_table';
```

### Widen the Column

```sql
ALTER TABLE users ALTER COLUMN email NVARCHAR(500);
```

### Truncate Data Before Insert

```sql
INSERT INTO users (name, email)
VALUES ('Alice', LEFT('very_long_email@example.com', 100));
```

### Use TRY_PARSE for Safe Conversion

```sql
-- Check data length before insert
SELECT LEN(email), * FROM users_import WHERE LEN(email) > 100;
```

### Use NVARCHAR Instead of VARCHAR for Unicode

```sql
-- VARCHAR(100) = 100 bytes max
-- NVARCHAR(100) = 100 characters = up to 400 bytes in UTF-8
ALTER TABLE users ALTER COLUMN name NVARCHAR(200);
```

## Examples

```sql
-- Value too long for column
INSERT INTO users (email) VALUES ('this_is_a_very_long_email_address@domain.com');
-- Error 8152: String or binary data would be truncated

-- Fix: ALTER TABLE users ALTER COLUMN email VARCHAR(100);

-- Implicit conversion expands data
INSERT INTO logs (message) VALUES (CAST(large_text AS NVARCHAR(MAX)));
-- Error 8152 if target is VARCHAR(500)
```

## Related Errors

- [Error 547]({{< relref "/tools/sqlserver/error-547" >}}) — CHECK constraint failed
- [Error 1205]({{< relref "/tools/sqlserver/error-1205" >}}) — deadlock victim
