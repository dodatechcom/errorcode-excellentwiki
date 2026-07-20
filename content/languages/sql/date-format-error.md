---
title: "[Solution] Invalid Date Format"
description: "Fix 'Invalid date format' when a date string does not match the expected format."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "data-type, date, format"]
severity: "error"
---

# Invalid Date Format

## Error Message

```
ERROR 1292: Incorrect date value: '2026/03/15' for column 'X' — The date string does not conform to the expected date format.
```

## Common Causes

- Date string uses a non-standard format that the database cannot parse (e.g., MM/DD/YYYY instead of YYYY-MM-DD)
- Date string contains invalid values like month 13 or day 32
- Time zone differences cause date interpretation issues
- Using string functions on date columns causes implicit conversion errors

## Solutions

### Solution 1: Use the ISO 8601 date format (YYYY-MM-DD)

Standard date format is universally supported across databases.

```sql
-- Wrong: non-standard date format
INSERT INTO events (event_date) VALUES ('03/15/2026');
INSERT INTO events (event_date) VALUES ('15-03-2026');

-- Correct: ISO 8601 format
INSERT INTO events (event_date) VALUES ('2026-03-15');

-- Correct: with time component
INSERT INTO events (event_datetime) VALUES ('2026-03-15 14:30:00');

-- PostgreSQL: with timezone
INSERT INTO events (event_datetime) VALUES ('2026-03-15T14:30:00+08:00');
```

### Solution 2: Use STR_TO_DATE or CONVERT to parse non-standard formats

Convert date strings from external sources to the correct format.

```sql
-- MySQL: parse MM/DD/YYYY format
INSERT INTO events (event_date)
VALUES (STR_TO_DATE('03/15/2026', '%m/%d/%Y'));

-- MySQL: parse with time
INSERT INTO events (event_datetime)
VALUES (STR_TO_DATE('03/15/2026 2:30 PM', '%m/%d/%Y %h:%i %p'));

-- SQL Server: parse non-standard format
INSERT INTO events (event_date)
VALUES (CONVERT(DATE, '03/15/2026', 101));

-- PostgreSQL: use TO_DATE
INSERT INTO events (event_date)
VALUES (TO_DATE('03/15/2026', 'MM/DD/YYYY'));
```

### Solution 3: Use DATE or DATETIME functions for date arithmetic

Use built-in date functions instead of string manipulation for date operations.

```sql
-- Correct: use date functions
SELECT * FROM events
WHERE event_date = CURDATE(); -- MySQL

SELECT * FROM events
WHERE event_date = CURRENT_DATE; -- PostgreSQL

-- Correct: date arithmetic
SELECT * FROM events
WHERE event_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY); -- MySQL

SELECT * FROM events
WHERE event_date >= CURRENT_DATE - INTERVAL '30 days'; -- PostgreSQL

-- Correct: extract components
SELECT YEAR(event_date), MONTH(event_date), DAY(event_date)
FROM events;
```

## Prevention Tips

- Always store dates in ISO 8601 format (YYYY-MM-DD) for maximum portability across databases
- Use DATE, TIME, and TIMESTAMP data types instead of strings for storing date and time values
- Set the database timezone appropriately and use UTC for storage to avoid timezone confusion

## Related Errors

- [Data Type Mismatch]({{< relref "/languages/sql/data-type-mismatch.md" >}})
- [Null Value Error]({{< relref "/languages/sql/null-value-error.md" >}})
- [Unicode Error]({{< relref "/languages/sql/unicode-error.md" >}})
