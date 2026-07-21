---
title: "[Solution] InfluxDB Partial Write Error — How to Fix"
description: "Fix InfluxDB partial write errors when some points in a batch are rejected while others are accepted"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Partial Write Error

Partial write errors occur when InfluxDB accepts some data points from a batch but rejects others due to validation failures, type conflicts, or resource limits.

## Why It Happens

- Mixed field types within the same measurement
- Points exceed the retention policy window
- Series cardinality limit is reached mid-batch
- Some points have invalid timestamps
- Batch contains duplicate points for the same series

## Common Error Messages

```
partial write: points beyond retention policy dropped=5
```

```
partial write: field type conflict, input field "temp" is type string, already exists as type float
```

```
partial write: max series per database exceeded, dropped=3
```

```
partial write: unable to parse timestamp: invalid format
```

## How to Fix It

### 1. Check Partial Write Details

```bash
# Enable detailed error logging
curl -XPOST 'http://localhost:8086/api/v2/write?org=myorg&bucket=mydb' \
  -H 'Authorization: Token mytoken' \
  -H 'X-Debug-Mode: true' \
  -d 'cpu,host=s01 value=42'
```

### 2. Validate Data Before Writing

```python
def validate_point(point):
    if point["timestamp"] <= 0:
        return False
    if not isinstance(point["value"], (int, float)):
        return False
    return True
```

### 3. Separate Problematic Points

```bash
# Write good points first
curl -XPOST 'http://localhost:8086/api/v2/write?org=myorg&bucket=mydb' \
  -H 'Authorization: Token mytoken' \
  -d @good_points.lp

# Debug and fix bad points separately
curl -XPOST 'http://localhost:8086/api/v2/write?org=myorg&bucket=mydb' \
  -H 'Authorization: Token mytoken' \
  -d @fixed_points.lp
```

### 4. Monitor Write Rejection Rate

```bash
curl -s 'http://localhost:8086/debug/vars' | jq '.stats.partialWrite'
```

## Examples

```
HTTP/1.1 207 Multi-Status
{"error":"partial write: field type conflict dropped=2 points, successful=998 points"}
```

## Prevent It

- Validate data types before writing to InfluxDB
- Use schema validation in the data pipeline
- Monitor partial write metrics for early detection

## Related Pages

- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
- [InfluxDB Line Protocol Error](/tools/influxdb/influxdb-line-protocol-error)
- [InfluxDB Field Type Mismatch](/tools/influxdb/influxdb-field-type-mismatch)
