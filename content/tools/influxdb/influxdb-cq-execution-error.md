---
title: "[Solution] InfluxDB CQ Execution Error — How to Fix"
description: "Fix InfluxDB continuous query execution errors when CQs fail to run or produce unexpected results"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB CQ Execution Error

Continuous query execution errors occur when pre-configured CQs fail to run at their scheduled intervals or produce incomplete results.

## Why It Happens

- Source measurement has no data in the CQ time window
- CQ interval is shorter than the data write frequency
- Target retention policy does not exist
- CQ references a measurement that was renamed or dropped
- Server restart causes CQ to miss execution windows

## Common Error Messages

```
error: continuous query failed: no data in time range
```

```
CQ error: target retention policy does not exist
```

```
continuous query "downsample_cpu" execution error
```

## How to Fix It

### 1. Verify CQ Status

```bash
influx -database mydb -execute 'SHOW CONTINUOUS QUERIES'
```

### 2. Check Target Retention Policy

```bash
influx -database mydb -execute 'SHOW RETENTION POLICIES ON "mydb"'
```

### 3. Recreate the CQ

```bash
influx -database mydb -execute 'DROP CONTINUOUS QUERY "downsample_cpu" ON "mydb"'
influx -database mydb -execute 'CREATE CONTINUOUS QUERY "downsample_cpu" ON "mydb" BEGIN SELECT mean("value") INTO "1h"."cpu_1h" FROM "cpu" WHERE time >= now() - 1h GROUP BY time(1h), "host" END'
```

### 4. Manually Backfill CQ Data

```bash
influx -database mydb -execute 'SELECT mean("value") INTO "1h"."cpu_1h" FROM "cpu" WHERE time >= now() - 24h GROUP BY time(1h), "host"'
```

## Examples

```
$ influx -database mydb -execute 'SHOW CONTINUOUS QUERIES'
name: mydb
name                query
downsample_cpu      CREATE CONTINUOUS QUERY "downsample_cpu" ON "mydb" BEGIN ... END
```

## Prevent It

- Monitor CQ execution with the monitor service
- Ensure target retention policies exist before creating CQs
- Set appropriate intervals based on data write frequency

## Related Pages

- [InfluxDB CQ Error](/tools/influxdb/influxdb-cq-error)
- [InfluxDB Task Error](/tools/influxdb/influxdb-task-error)
- [InfluxDB Retention Error](/tools/influxdb/influxdb-retention-error)
