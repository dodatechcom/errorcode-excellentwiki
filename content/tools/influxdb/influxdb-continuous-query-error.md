---
title: "[Solution] InfluxDB Continuous Query Error — How to Fix"
description: "Fix InfluxDB continuous query errors including CQ creation failures, execution issues, and CQ management problems"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Continuous Query Error

Continuous query errors in InfluxDB occur when CQs fail to create, execute, or produce the expected results. CQs automatically downsample data into new measurements.

## Why It Happens

- The CQ syntax is incorrect
- The source measurement does not exist
- The target measurement has a different schema
- The CQ execution interval is too frequent
- The CQ requires more memory than available
- The CQ is disabled or has errors in the last run

## Common Error Messages

```
error: continuous query already exists
```

```
continuous query error: source measurement not found
```

```
continuous query error: syntax error
```

```
continuous query error: execution timeout
```

## How to Fix It

### 1. Create Continuous Query

```influxql
-- Basic CQ for downsampling
CREATE CONTINUOUS QUERY "cq_cpu_1h" ON "mydb"
BEGIN
  SELECT mean("value") AS "mean_value"
  INTO "cpu_1h"
  FROM "cpu"
  GROUP BY time(1h), "host"
END
```

### 2. Check CQ Status

```influxql
SHOW CONTINUOUS QUERIES

-- Check CQ execution
SELECT * FROM "mydb"."cq_cpu_1h"
```

### 3. Fix CQ Syntax

```influxql
-- BAD: missing INTO clause
CREATE CONTINUOUS QUERY "cq_cpu" ON "mydb"
BEGIN
  SELECT mean("value") FROM "cpu" GROUP BY time(1h)
END

-- GOOD: include INTO clause
CREATE CONTINUOUS QUERY "cq_cpu" ON "mydb"
BEGIN
  SELECT mean("value") INTO "cpu_downsampled" FROM "cpu" GROUP BY time(1h)
END
```

### 4. Drop and Recreate CQ

```influxql
-- Drop existing CQ
DROP CONTINUOUS QUERY "cq_cpu_1h" ON "mydb"

-- Recreate with corrected syntax
CREATE CONTINUOUS QUERY "cq_cpu_1h" ON "mydb"
BEGIN
  SELECT mean("value") AS "mean_value"
  INTO "cpu_1h"
  FROM "cpu"
  GROUP BY time(1h), "host"
END
```

## Common Scenarios

- **CQ does not produce data**: Check if the source measurement exists and has data.
- **CQ is slow**: Increase the execution interval or simplify the query.
- **CQ syntax error**: Review the CQ syntax and fix errors.

## Prevent It

- Test CQs on a staging database before deploying
- Monitor CQ execution with `SHOW CONTINUOUS QUERIES`
- Document CQ purposes and retention policies

## Related Pages

- [InfluxDB Query Error](/tools/influxdb/influxdb-query-error)
- [InfluxDB Task Error](/tools/influxdb/influxdb-task-error)
- [InfluxDB Retention Error](/tools/influxdb/influxdb-retention-error)
