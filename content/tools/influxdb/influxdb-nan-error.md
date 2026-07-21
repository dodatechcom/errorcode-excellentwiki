---
title: "[Solution] InfluxDB NaN Value Error — How to Fix"
description: "Fix InfluxDB NaN and infinity value errors when computations produce invalid floating-point results"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB NaN Value Error

NaN value errors occur when Flux queries produce Not-a-Number or infinity results from operations like division by zero or invalid mathematical functions.

## Why It Happens

- Division by zero produces infinity or NaN
- Logarithm of zero or negative numbers
- Square root of negative numbers in Flux
- Aggregation of empty result sets
- Float overflow from extreme arithmetic

## Common Error Messages

```
error: value is NaN, cannot be stored
```

```
runtime error: NaN is not a valid field value
```

```
error: infinity is not representable in this type
```

```
partial write: field value is NaN or Inf, dropped=1
```

## How to Fix It

### 1. Filter NaN Values in Queries

```flux
from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => not (r._value != r._value))
  |> filter(fn: (r) => r._value > -1.0e+308 and r._value < 1.0e+308)
```

### 2. Handle Division by Zero

```flux
from(bucket: "mydb")
  |> range(start: -1h)
  |> map(fn: (r) => ({
    r with
    _value: if r._value != 0.0 then r.numerator / r._value else 0.0
  }))
```

### 3. Replace NaN Before Write

```python
import math

def sanitize_value(value):
    if math.isnan(value) or math.isinf(value):
        return 0.0
    return value
```

### 4. Configure NaN Handling

```bash
[data]
  index-version = "tsi1"
  wal-encode-buffer = 4096
```

## Examples

```
error @8:5-8:20: value is NaN, cannot be stored
```

Fix:

```flux
from(bucket: "mydb")
  |> filter(fn: (r) => r._value != 0.0)
  |> mean()
```

## Prevent It

- Add null/NaN checks in data collection pipelines
- Use default values for potentially empty aggregations
- Validate data before writing with line protocol

## Related Pages

- [InfluxDB Flux Math Error](/tools/influxdb/influxdb-flux-math-error)
- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
- [InfluxDB Flux Type Error](/tools/influxdb/influxdb-flux-type-error)
