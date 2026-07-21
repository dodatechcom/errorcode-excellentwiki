---
title: "[Solution] InfluxDB Backfill Error — How to Fix"
description: "Fix InfluxDB backfill errors when inserting historical data with duplicate timestamps or out-of-order writes"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Backfill Error

Backfill errors occur when inserting historical data into InfluxDB and the timestamps conflict with existing data or fall outside the retention policy window.

## Why It Happens

- Timestamps overlap with existing data points for the same series
- Target retention policy has already deleted data for that time range
- Batch insert size exceeds the maximum line protocol payload
- Clock synchronization issues between write clients
- Shards are already sealed for the target time window

## Common Error Messages

```
partial write: points beyond retention policy dropped=50
```

```
error: field type conflict with existing data
```

```
partial write: unable to parse line protocol: invalid timestamp
```

## How to Fix It

### 1. Adjust Retention Policy

```bash
influx -execute "ALTER RETENTION POLICY \"autogen\" ON \"mydb\" DURATION 525600h"
```

### 2. Use Force-Insert for Overlapping Data

```bash
curl -XPOST 'http://localhost:8086/api/v2/write?org=myorg&bucket=mydb&precision=ns' \
  -H 'Authorization: Token mytoken' \
  -d 'cpu,host=server01 value=0.64 1609459200000000001'
```

### 3. Batch Large Backfills

```bash
cat historical_data.csv | split -l 10000 - batch_ && \
for f in batch_*; do
  influx -import -path "$f" -precision ns -database mydb
  sleep 2
done
```

### 4. Create Extended Retention for Backfill

```bash
influx -execute 'CREATE RETENTION POLICY "backfill" ON "mydb" DURATION 8760h REPLICATION 1'
influx -import -path backfill_data.lp -precision ns -database mydb -retention backfill
```

## Examples

```
$ influx -import -path historical_data.lp -precision ns -database mydb
2024/01/15 10:30:00 ERROR: partial write: points beyond retention policy dropped=1250
```

## Prevent It

- Backfill data before retention policies expire old data
- Use rp:backfill routing for historical imports
- Validate timestamps in source data before writing

## Related Pages

- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
- [InfluxDB Retention Error](/tools/influxdb/influxdb-retention-error)
- [InfluxDB Line Protocol Error](/tools/influxdb/influxdb-line-protocol-error)
