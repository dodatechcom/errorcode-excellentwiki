---
title: "[Solution] InfluxDB Column Type Error — How to Fix"
description: "Fix InfluxDB column type mismatch errors when field values have inconsistent types across writes"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Column Type Error

Column type errors occur when InfluxDB encounters a field value with a different data type than what is already stored for that field in the same measurement.

## Why It Happens

- A field was previously stored as an integer but new data sends a string
- Boolean and integer values are mixed in the same field
- Tag values are accidentally written as field values
- Data pipeline changes the value type without schema awareness
- JSON deserialization produces a different type than expected

## Common Error Messages

```
partial write: field type conflict, input field "value" on measurement "cpu" is type float, already exists as type integer
```

```
error: field type mismatch with existing data
```

## How to Fix It

### 1. Identify Conflicting Fields

```bash
influx -database mydb -execute 'SHOW FIELD KEYS ON "mydb" "cpu"'
```

### 2. Drop and Recreate Measurement

```bash
influx -database mydb -execute 'DROP MEASUREMENT "cpu"'
```

### 3. Cast Values in Client Code

```python
value = float(raw_value)
```

### 4. Validate Data Pipeline Types

```bash
influx -database mydb -execute 'SHOW FIELD KEYS ON "mydb" "cpu"'
```

## Examples

```
partial write: field type conflict, input field "usage" on measurement "cpu" is type string, already exists as type integer rejected=1
```

## Prevent It

- Enforce schema validation in data collection pipelines
- Use typed protocols like Protocol Buffers for data ingestion
- Document field types for each measurement

## Related Pages

- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
- [InfluxDB Field Type Mismatch](/tools/influxdb/influxdb-field-type-mismatch)
- [InfluxDB Line Protocol Error](/tools/influxdb/influxdb-line-protocol-error)
