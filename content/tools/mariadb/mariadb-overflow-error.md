---
title: "[Solution] MariaDB Overflow Error — How to Fix"
description: "Fix MariaDB integer overflow and DECIMAL truncation errors by adjusting column types, checking data ranges, and handling numeric conversions"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Overflow Error

An overflow error occurs when a numeric value exceeds the maximum or minimum value that a column data type can hold. This includes integer types (TINYINT, INT, BIGINT) and fixed-point types (DECIMAL).

## Why It Happens

- The column data type is too small for the values being inserted
- Arithmetic operations produce results that exceed the type's range
- `INSERT IGNORE` silently truncates data instead of erroring
- The application casts or converts values incorrectly
- Auto-increment reaches the maximum value for the integer type

## Common Error Messages

```
ERROR 1406 (22001): Data too long for column 'id' at row 1
```

```
ERROR 1690 (22003): BIGINT value is out of range in '(`a` + `b`)'
```

```
ERROR 1264 (22003): Out of range value for column 'quantity' at row 1
```

```
Warning: Data truncated for column 'score' at row 1
```

## How to Fix It

### 1. Increase the Column Data Type

```sql
ALTER TABLE mytable MODIFY COLUMN id BIGINT UNSIGNED;
ALTER TABLE mytable MODIFY COLUMN score INT;
ALTER TABLE mytable MODIFY COLUMN price DECIMAL(12,2);
```

### 2. Use UNSIGNED for Non-Negative Values

```sql
ALTER TABLE mytable MODIFY COLUMN counter INT UNSIGNED;
ALTER TABLE mytable MODIFY COLUMN big_id BIGINT UNSIGNED;
```

### 3. Fix Arithmetic Overflow

```sql
-- Cast to BIGINT before arithmetic
SELECT CAST(a AS BIGINT) + CAST(b AS BIGINT) FROM mytable;

-- Or use wider types from the start
ALTER TABLE mytable MODIFY COLUMN a BIGINT, MODIFY COLUMN b BIGINT;
```

### 4. Handle DECIMAL Truncation

```sql
ALTER TABLE mytable MODIFY COLUMN amount DECIMAL(18,4);
SET SESSION sql_mode = 'STRICT_ALL_TABLES';
```

## Common Scenarios

- **Auto-increment overflow**: INT UNSIGNED reaches 4,294,967,295. Change to BIGINT UNSIGNED.
- **Large financial calculations**: Summing many DECIMAL(10,2) values overflows. Use DECIMAL(18,4).
- **Importing CSV with oversized values**: Widen the column before importing.

## Prevent It

- Use `BIGINT` for primary keys in high-volume tables
- Use `STRICT_ALL_TABLES` SQL mode for early error detection
- Test import scripts with worst-case values before production

## Related Pages

- [MariaDB Schema Error](/tools/mariadb/mariadb-schema-error)
- [MariaDB Import Error](/tools/mariadb/mariadb-import-error)
- [MySQL Overflow Error](/tools/mysql/mysql-overflow-error)
