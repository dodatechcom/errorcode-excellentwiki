---
title: "[Solution] ClickHouse Data Format Error — How to Fix"
description: "Fix ClickHouse data format errors including FORMAT clause issues, TSV/CSV parsing failures, JSON format problems, and input/output format mismatches"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse Data Format Error

Format errors in ClickHouse occur when data cannot be parsed due to incorrect FORMAT specification, malformed input data, or mismatch between the expected and actual data format.

## Why It Happens

- The FORMAT clause does not match the actual data format
- CSV data contains delimiters that conflict with the format
- JSON data has syntax errors or unexpected structure
- The `input_format_skip_unknown_fields` setting is not enabled
- Binary data is sent when text format is expected
- Date/datetime values are in the wrong format

## Common Error Messages

```
Code: 27. DB::Exception: Cannot parse input: expected ',' before
```

```
Code: 117. DB::Exception: Unknown input format 'TSVRaw'
```

```
Code: 62. DB::Exception: JSON parsing error near '...'
```

```
Code: 33. DB::Exception: Cannot read all data
```

## How to Fix It

### 1. Specify Correct FORMAT

```sql
-- For CSV data
INSERT INTO events FORMAT CSV
1,2024-01-15,click,page1

-- For JSON data
INSERT INTO events FORMAT JSONEachRow
{"id": 1, "date": "2024-01-15", "event": "click"}

-- For TabSeparated
INSERT INTO events FORMAT TabSeparated
1	2024-01-15	click	page1
```

### 2. Fix CSV Parsing Issues

```sql
-- Set CSV format settings
SET input_format_csv_delimiter = ',';
SET input_format_csv_skip_first_lines = 1;
SET input_format_csv_allow_single_quotes = 1;
SET input_format_csv_allow_double_quotes = 1;

-- For CSV with headers
INSERT INTO events FORMAT CSVWithNames
id,date,event,page
1,2024-01-15,click,page1
```

### 3. Fix JSON Format Issues

```sql
-- For JSON objects per line
INSERT INTO events FORMAT JSONEachRow
{"id": 1, "date": "2024-01-15", "event": "click"}
{"id": 2, "date": "2024-01-15", "event": "view"}

-- For JSON array
INSERT INTO events FORMAT JSON
[{"id": 1, "date": "2024-01-15", "event": "click"}]

-- Skip unknown fields
SET input_format_skip_unknown_fields = 1;
```

### 4. Fix Date Format Issues

```sql
-- ClickHouse expects ISO format by default
-- GOOD: 2024-01-15
-- BAD: 01/15/2024

-- For custom date formats
SELECT toDateTime('15/01/2024', '%d/%m/%Y');
SELECT toDate('15-01-2024', '%d-%m-%Y');
```

## Common Scenarios

- **CSV import fails with delimiter issues**: Set `input_format_csv_delimiter` to match the actual delimiter.
- **JSON import fails with unknown fields**: Enable `input_format_skip_unknown_fields`.
- **Date parsing fails**: Ensure dates are in ISO format or use `toDateTime` with format string.

## Prevent It

- Always test data import with a small sample first
- Use `FORMAT JSONEachRow` for JSON data as it is the most robust
- Document the expected data format for import scripts

## Related Pages

- [ClickHouse Query Error](/tools/clickhouse/clickhouse-query-error)
- [ClickHouse CSV Error](/tools/clickhouse/clickhouse-csv-error)
- [ClickHouse Import Error](/tools/clickhouse/clickhouse-import-error)
