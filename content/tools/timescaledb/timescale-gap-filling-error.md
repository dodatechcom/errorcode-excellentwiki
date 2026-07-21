---
title: "[Solution] TimescaleDB Gap Filling Error — How to Fix"
description: "Fix TimescaleDB gap filling errors by resolving timebucket_gapfill failures, fixing missing data interpolation, and handling locf issues"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Gap Filling Error

TimescaleDB gap filling errors occur when using the time_bucket_gapfill function or locf/nocb interpolation functions that fail due to incorrect parameters or incompatible data.

## Why It Happens

- start or finish parameters are missing or NULL
- time_bucket interval is zero or negative
- Gapfill is used on a non-time-series query
- locf function receives NULL-only groups
- Data type mismatch between time column and gapfill parameters
- Gapfill window is too large causing memory issues

## Common Error Messages

```
ERROR: time_bucket_gapfill requires start and finish
```

```
ERROR: gapfill interval must be positive
```

```
ERROR: locf received no data for group
```

```
ERROR: insufficient memory for gapfill
```

## How to Fix It

### 1. Use Correct Gapfill Syntax

```sql
-- Correct time_bucket_gapfill usage
SELECT
  time_bucket_gapfill('1 hour', time,
    start => '2024-01-01 00:00:00'::TIMESTAMPTZ,
    finish => '2024-01-01 23:59:59'::TIMESTAMPTZ
  ) AS bucket,
  AVG(value) AS avg_value
FROM sensor_data
WHERE time >= '2024-01-01'::TIMESTAMPTZ
  AND time < '2024-01-02'::TIMESTAMPTZ
GROUP BY bucket ORDER BY bucket;
```

### 2. Fix locf Usage

```sql
-- locf carries last value forward into gaps
SELECT
  time_bucket_gapfill('1 hour', time,
    start => '2024-01-01'::TIMESTAMPTZ,
    finish => '2024-01-02'::TIMESTAMPTZ
  ) AS bucket,
  locf(AVG(value)) AS filled_value
FROM sensor_data
WHERE device_id = 1
  AND time >= '2024-01-01'::TIMESTAMPTZ
  AND time < '2024-01-02'::TIMESTAMPTZ
GROUP BY bucket ORDER BY bucket;
```

### 3. Handle nocb (No Carry Backward)

```sql
-- nocb prevents carrying values backward from the future
SELECT
  time_bucket_gapfill('15 minutes', time,
    start => '2024-01-01'::TIMESTAMPTZ,
    finish => '2024-01-02'::TIMESTAMPTZ
  ) AS bucket,
  locf(AVG(value), 0, nocb) AS filled_value
FROM sensor_data
WHERE device_id = 1
GROUP BY bucket ORDER BY bucket;
```

### 4. Optimize Memory for Large Gapfill Windows

```sql
-- Reduce the gapfill window to avoid memory issues
-- Instead of filling a month at once, use smaller windows
SELECT
  time_bucket_gapfill('1 hour', time,
    start => '2024-01-01'::TIMESTAMPTZ,
    finish => '2024-01-01 23:59:59'::TIMESTAMPTZ
  ) AS bucket,
  AVG(value) AS avg_value
FROM sensor_data
WHERE time >= '2024-01-01'::TIMESTAMPTZ
  AND time < '2024-01-02'::TIMESTAMPTZ
GROUP BY bucket ORDER BY bucket;
```

## Common Scenarios

- **Gapfill returns no rows**: Ensure start and finish parameters cover the desired range.
- **locf fills with NULL**: There must be at least one non-NULL value before the gap.
- **Gapfill uses too much memory**: Reduce the time range or bucket interval.

## Prevent It

- Always include start and finish parameters in time_bucket_gapfill
- Use WHERE clause to limit the time range before gapfill
- Test with small time ranges before applying to large datasets

## Related Pages

- [TimescaleDB Query Error](/tools/timescaledb/timescale-query-error)
- [TimescaleDB Functions Error](/tools/timescaledb/timescale-functions-error)
- [TimescaleDB Time Bucket Error](/tools/timescaledb/timescale-time-bucket-error)
