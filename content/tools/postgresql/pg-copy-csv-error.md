---
title: "[Solution] PostgreSQL COPY CSV Format Error"
description: "Fix PostgreSQL COPY CSV format errors. Resolve delimiter and quoting issues when importing CSV data."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
---

# PostgreSQL COPY CSV Format Error

ERROR: missing data for column / extra data after last expected column

This error occurs when the CSV data does not match the expected column structure of the target table during a COPY operation.

## Common Causes

- CSV file contains a different number of columns than the table
- Delimiter character conflicts with data values in the CSV
- Quote character not properly escaping embedded delimiters
- Header row present when HEADER option is not specified

## How to Fix

1. Count columns in the CSV and compare to table definition:

```bash
head -1 data.csv | awk -F',' '{print NF}'
psql -c "\d target_table"
```

2. Use correct COPY options for your CSV format:

```sql
COPY users FROM '/data/users.csv'
WITH (
  FORMAT CSV,
  HEADER true,
  DELIMITER ',',
  QUOTE '"',
  ESCAPE '"'
);
```

3. Handle NULL values explicitly:

```sql
COPY users FROM '/data/users.csv'
WITH (
  FORMAT CSV,
  HEADER true,
  NULL ''
);
```

## Examples

```bash
# Preview CSV structure
head -3 data.csv

# Import with explicit column list
psql -c "\copy users(name, email) FROM 'data.csv' WITH CSV HEADER"
```
