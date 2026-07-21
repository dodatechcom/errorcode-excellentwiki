---
title: "[Solution] InfluxDB Max Series Error — How to Fix"
description: "Fix InfluxDB max series limit exceeded errors when the number of time series exceeds the configured maximum"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Max Series Error

Max series errors occur when the number of unique time series in a database exceeds the configured maximum series limit per database.

## Why It Happens

- High-cardinality tag values create too many unique series
- Missing tag value normalization allows near-duplicate series
- Batch writes introduce inconsistent tag combinations
- Auto-generated unique identifiers used as tag values
- Debug or test data with random tag values

## Common Error Messages

```
partial write: max series per database exceeded, dropped=50
```

```
error: too many series: limit is 100000
```

```
partial write: series limit reached for database "mydb"
```

## How to Fix It

### 1. Check Current Series Count

```bash
influx -database mydb -execute 'SHOW SERIES CARDINALITY'
```

### 2. Increase Series Limit

```bash
[data]
  max-series-per-database = 1000000
```

### 3. Reduce Tag Cardinality

```bash
# Check which tags have high cardinality
influx -database mydb -execute 'SHOW TAG VALUES FROM "cpu" WITH KEY = "host"'
```

### 4. Drop High-Cardinality Series

```bash
# Drop measurement with too many series
influx -database mydb -execute 'DROP MEASUREMENT "high_card_debug"'
```

## Examples

```
$ influx -database mydb -execute 'SHOW SERIES CARDINALITY'
85423

# After adding debug data:
partial write: max series per database exceeded, dropped=15000
```

## Prevent It

- Avoid using high-cardinality values as tags
- Set max-series-per-database based on expected workload
- Monitor series cardinality with continuous queries

## Related Pages

- [InfluxDB Cardinality Error](/tools/influxdb/influxdb-cardinality-error)
- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
- [InfluxDB Memory Error](/tools/influxdb/influxdb-memory-error)
