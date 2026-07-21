---
title: "[Solution] MySQL Character Set Conversion Error"
description: "Fix MySQL character set conversion error when data contains bytes that are invalid in the target character encoding"
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
---

# MySQL Character Set Conversion Error

Data conversion between character sets fails because the source string contains byte sequences that are invalid in the target encoding. This causes truncation, replacement characters, or errors.

## Common Causes

- Storing UTF-8 data in a Latin1 column
- Mixed encodings in the same column (e.g., UTF-8 and GBK)
- Incorrect client character set configuration
- Binary data stored in a character column
- CONVERT() or CAST() between incompatible character sets
- Implicit conversion during JOIN between tables with different charsets

## How to Fix

### Set Correct Character Set

```sql
-- Set character set for the database
ALTER DATABASE mydb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Set for a table
ALTER TABLE orders CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Set for a column
ALTER TABLE orders MODIFY name VARCHAR(255)
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### Check Current Character Set

```sql
-- View character set settings
SHOW VARIABLES LIKE 'character_set%';
SHOW VARIABLES LIKE 'collation%';

-- View column character set
SELECT
  COLUMN_NAME,
  CHARACTER_SET_NAME,
  COLLATION_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'orders';
```

### Fix Mixed Encodings

```sql
-- Convert Latin1 column with UTF-8 data stored as bytes
UPDATE orders
SET name = CONVERT(CAST(name AS BINARY) USING utf8mb4)
WHERE name IS NOT NULL;
```

### Use Proper Conversion Functions

```sql
-- Safe conversion
SELECT CONVERT('café' USING utf8mb4);

-- Check if conversion would lose data
SELECT IF(
  CONVERT(CAST('café' AS BINARY) USING utf8mb4) = 'café',
  'safe',
  'data loss'
);
```

### Configure Client Connection

```sql
-- Set client character set
SET NAMES utf8mb4;

-- Or in connection string
-- jdbc:mysql://host/db?characterEncoding=UTF-8&useUnicode=true
```

## Examples

```
ERROR 1366 (HY000): Incorrect string value: '\xC3\xA9' for column
  'name' at row 1 -- UTF-8 bytes in Latin1 column

WARNING 1300 (HY000): Invalid utf8 character string: '\xE4\xBD\xA0\xE5\xA5\xBD'
```

## Related Errors

- [MySQL Collation Error]({{< relref "/tools/mysql/mysql-collation-error" >}}) -- collation issues
- [MySQL Character Set Error]({{< relref "/tools/mysql/mysql-character-set-error" >}}) -- charset issues
- [MySQL Data Truncated]({{< relref "/tools/mysql/mysql-data-truncated" >}}) -- truncation
