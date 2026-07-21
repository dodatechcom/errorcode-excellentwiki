---
title: "SQL PIVOT Unpivot Column Name Error"
description: "Fix SQL PIVOT and UNPIVOT errors when column names contain spaces, special characters, or reserved words."
languages: ["sql"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Column names with spaces not properly quoted
- Reserved words used as column names in PIVOT
- FOR clause references wrong column type
- UNPIVOT produces NULL values for non-existent source combinations
- Multiple value columns in PIVOT create unexpected column structure

## How to Fix

```sql
-- WRONG: Unquoted column with space
SELECT * FROM sales
PIVOT (
    SUM(amount)
    FOR [Product Name] IN ([Widget A], [Widget B])  -- brackets needed
);

-- CORRECT: Use proper quoting
SELECT * FROM sales
PIVOT (
    SUM(amount)
    FOR [Product Name] IN ([Widget A], [Widget B])
);
```

```sql
-- WRONG: PIVOT on wrong data type
SELECT * FROM orders
PIVOT (
    COUNT(*)
    FOR order_date IN (Jan, Feb, Mar)
);
-- order_date is DATE, not a category

-- CORRECT: Transform first
SELECT * FROM (
    SELECT DATE_FORMAT(order_date, '%b') AS month, amount
    FROM orders
) src
PIVOT (
    SUM(amount)
    FOR month IN ('Jan', 'Feb', 'Mar')
);
```

## Examples

```sql
-- Example 1: Basic PIVOT (SQL Server)
SELECT * FROM quarterly_sales
PIVOT (
    SUM(revenue)
    FOR quarter IN ([Q1], [Q2], [Q3], [Q4])
) AS pivot_table;

-- Example 2: UNPIVOT (SQL Server)
SELECT product, period, revenue
FROM pivot_table
UNPIVOT (
    revenue FOR period IN ([Q1], [Q2], [Q3], [Q4])
) AS unpivot_table;

-- Example 3: Dynamic PIVOT with quoted columns
DECLARE @cols NVARCHAR(MAX)
SELECT @cols = STRING_AGG(QUOTENAME(month_name), ', ')
FROM (SELECT DISTINCT DATENAME(MONTH, order_date) AS month_name
      FROM orders) t;

DECLARE @sql NVARCHAR(MAX)
SET @sql = 'SELECT * FROM orders
            PIVOT (COUNT(*) FOR DATENAME(MONTH, order_date) IN (' + @cols + ')) p'
EXEC sp_executesql @sql;
```

## Related Errors

- [Pivot error](sql-pivot-error) -- PIVOT syntax issues
- [SQL XML error](sql-xml-error) -- XML-related pivot alternatives
