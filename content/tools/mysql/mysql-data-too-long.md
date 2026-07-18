---
title: "[Solution] MySQL Data Too Long for Column - Fix Truncation Errors"
description: "Fix MySQL data too long for column errors by adjusting column size, using proper data validation, and enabling strict SQL mode"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# MySQL Data Too Long for Column

This error occurs when an `INSERT` or `UPDATE` statement tries to store a value that is longer than the column's defined length or type allows.

## What This Error Means

MySQL returns this error when data exceeds the column's capacity:

```
ERROR 1406 (22001): Data too long for column 'name' at row 1
```

In strict SQL mode, MySQL rejects the entire statement. In non-strict mode, the value is silently truncated and a warning is generated instead of an error.

The error also appears for numeric types:

```
ERROR 1264 (22003): Out of range value for column 'age' at row 1
```

## Why It Happens

- The column is defined as `VARCHAR(50)` but the application sends a 200-character string
- Binary data (like images) is stored in a `VARCHAR` column instead of `BLOB`
- A numeric value exceeds the range of `INT`, `BIGINT`, or `DECIMAL`
- The application does not validate input length before inserting
- Importing data from a system with different character encoding
- Multi-byte characters cause the byte length to exceed the column limit
- The column was created with insufficient size for the expected data

## How to Fix It

### 1. Check the Column Definition

```sql
-- Show the column's data type and max length
DESCRIBE users;

-- Get detailed column information
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, NUMERIC_PRECISION
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'mydb' AND TABLE_NAME = 'users';
```

### 2. Increase the Column Size

```sql
-- Increase VARCHAR length
ALTER TABLE users MODIFY COLUMN name VARCHAR(255);

-- For TEXT columns that need to hold more data
ALTER TABLE users MODIFY COLUMN bio TEXT;
```

### 3. Validate Data Length Before Inserting

```sql
-- Check the length of the data being inserted
SELECT LENGTH('your long string here');

-- Truncate in the query if needed
INSERT INTO users (name) VALUES (LEFT('your long string here', 255));
```

### 4. Enable Strict SQL Mode

```sql
-- Strict mode rejects truncated data instead of silently truncating
SET GLOBAL sql_mode = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- Or in my.cnf
[mysqld]
sql_mode = STRICT_TRANS_TABLES
```

### 5. Handle Multi-byte Characters

```sql
-- VARCHAR(50) stores 50 characters, not 50 bytes
-- But VARBINARY(50) stores 50 bytes
-- For multi-byte encodings, use CHARACTER SET

-- Check the column's character set
SELECT COLUMN_NAME, CHARACTER_SET_NAME, COLLATION_NAME
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'mydb' AND TABLE_NAME = 'users';
```

## Common Mistakes

- Assuming `VARCHAR(255)` means 255 bytes -- it means 255 characters (which can be up to 1020 bytes in utf8mb4)
- Not using strict SQL mode -- in non-strict mode, data is silently truncated without any indication
- Storing binary data in character columns -- use `BLOB` or `VARBINARY` instead
- Not accounting for multi-byte characters when calculating buffer sizes in application code
- Using `INT` for values that can exceed 2.1 billion -- use `BIGINT` instead

## Related Pages

- [MySQL Incorrect Datetime](/tools/mysql/mysql-incorrect-datetime)
- [MySQL Column Does Not Exist](/tools/mysql/mysql-column-doesnt-exist)
- [MySQL Duplicate Entry](/tools/mysql/mysql-duplicate-entry)
- [PostgreSQL Null Violation](/tools/postgresql/pg-null-violation)
