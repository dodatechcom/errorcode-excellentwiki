---
title: "[Solution] MySQL Incorrect Datetime Value - Fix Date Format Errors"
description: "Fix MySQL incorrect datetime value errors by using proper date formats, STR_TO_DATE, and enabling strict mode for data validation"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# MySQL Incorrect Datetime Value

This error occurs when MySQL receives a string that it cannot parse as a valid `DATE`, `DATETIME`, or `TIMESTAMP` value. The string may be in the wrong format, contain invalid dates, or use an unrecognized separator.

## What This Error Means

MySQL returns this error when a datetime conversion fails:

```
ERROR 1292 (22007): Incorrect datetime value: '2024-13-01' for column 'created_at' at row 1
```

In strict SQL mode, the statement fails. In non-strict mode, MySQL stores `0000-00-00 00:00:00` and generates a warning. The error can also appear in `WHERE` clauses when implicit conversion of a string to a date fails.

## Why It Happens

- The date string is in a format MySQL does not recognize (e.g., `01/13/2024` instead of `2024-01-13`)
- The date contains impossible values (month 13, day 32, February 30)
- The string contains non-date characters (like `2024-01-01T12:00:00`)
- The `NO_ZERO_DATE` SQL mode rejects zero dates
- The column expects `DATE` but receives a `DATETIME` string with a time component
- The application sends dates in a locale-specific format instead of ISO 8601
- A `WHERE` clause compares a date column to a non-date string

## How to Fix It

### 1. Use ISO 8601 Format

```sql
-- CORRECT: MySQL's native format
INSERT INTO events (created_at) VALUES ('2024-01-15 10:30:00');

-- CORRECT: date only
INSERT INTO events (event_date) VALUES ('2024-01-15');
```

### 2. Convert Non-Standard Formats

```sql
-- Convert MM/DD/YYYY to MySQL format
INSERT INTO events (created_at)
VALUES (STR_TO_DATE('01/15/2024', '%m/%d/%Y'));

-- Common format specifiers:
-- %Y = 4-digit year, %m = month (01-12), %d = day (01-31)
-- %H = hour (00-23), %i = minutes, %s = seconds
```

### 3. Fix WHERE Clause Comparisons

```sql
-- WRONG: string comparison may fail
SELECT * FROM events WHERE created_at = '01/15/2024';

-- CORRECT: use proper format
SELECT * FROM events WHERE created_at = '2024-01-15';

-- Or use DATE() to extract the date part
SELECT * FROM events WHERE DATE(created_at) = '2024-01-15';
```

### 4. Validate Before Inserting

```sql
-- Check if a string is a valid date
SELECT STR_TO_DATE('2024-01-15', '%Y-%m-%d') IS NOT NULL AS valid;
-- Returns 1 if valid, NULL if not
```

### 5. Handle NULL Dates

```sql
-- Use NULL instead of zero dates
INSERT INTO events (created_at) VALUES (NULL);

-- Or use a default
ALTER TABLE events
    ALTER COLUMN created_at SET DEFAULT CURRENT_TIMESTAMP;
```

## Common Mistakes

- Using `DATE()` function in `WHERE` clauses, which prevents index usage
- Not setting `sql_mode` to include `STRICT_TRANS_TABLES`, allowing invalid dates to be stored as zero dates
- Parsing dates in application code and passing them as strings instead of using parameterized queries
- Not accounting for timezone differences when converting date strings
- Using `TIMESTAMP` for dates before 1970 or after 2038 -- use `DATETIME` instead

## Related Pages

- [MySQL Data Too Long](/tools/mysql/mysql-data-too-long)
- [MySQL Column Does Not Exist](/tools/mysql/mysql-column-doesnt-exist)
- [MySQL InnoDB Error](/tools/mysql/mysql-innodb-error)
- [PostgreSQL Null Violation](/tools/postgresql/pg-null-violation)
