---
title: "InfluxDB Field Type Mismatch"
description: "Field type conflict between writes"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
A field is being written with different data types across points.

## Common Causes
- Mixed data types in source system
- Incorrect type casting
- Schema evolution not handled

## How to Fix
```bash
# Check field types
influx query 'from(bucket:"mydb") |> range(start:-1h) |> filter(fn:(r) => r._field == "myfield") |> distinct(column: "_field")'

# Delete points with wrong type
influx delete --org myorg --bucket mydb --start 2023-01-01T00:00:00Z --stop 2023-12-31T23:59:59Z --predicate '_measurement="cpu" AND _field="myfield"'
```

## Examples
```javascript
// Ensure consistent types
point.fields.value = Number(point.fields.value) // Always write as number
```

