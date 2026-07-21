---
title: "InfluxDB Continuous Query Error"
description: "Continuous query execution failure"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
A continuous query failed to execute or produce expected results.

## Common Causes
- Source measurement does not exist
- Flux syntax error in CQ definition
- Insufficient permissions

## How to Fix
```flux
// List continuous queries
import "influxdata/influxdb/schema"
schema.measurements(bucket: "mydb")

// Drop and recreate
drop("my-cq")
```

## Examples
```flux
// Check CQ status
option task = {name: "my-cq", every: 1h}
from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> mean()
  |> to(bucket: "mydb-downsampled")
```

