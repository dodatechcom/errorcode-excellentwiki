---
title: "InfluxDB Flux Date Error"
description: "Flux date/time operation error"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Flux date/time operations are producing errors.

## Common Causes
- Invalid date format
- Timezone mismatch
- Duration overflow

## How to Fix
```flux
import "date"

from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> hour(fn: (t) => t.hour)
```

## Examples
```flux
// Correct date usage
from(bucket: "mydb")
  |> range(start: -24h)
  |> filter(fn: (r) => date.hour(t: r._time) >= 9 and date.hour(t: r._time) <= 17)
```

