---
title: "InfluxDB Graphite Error"
description: "Graphite input plugin failure"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
InfluxDB cannot receive Graphite data.

## Common Causes
- Graphite listener not enabled
- Protocol mismatch
- Template configuration error

## How to Fix
```yaml
# influxdb.conf Graphite settings
[[graphite]]
  enabled = true
  bind-address = ":2003"
  database = "graphite"
  protocol = "tcp"
```

## Examples
```bash
# Test Graphite input
echo "cpu.usage 0.5 $(date +%s)" | nc localhost 2003
# Check Graphite metrics
influx query 'from(bucket:"graphite") |> range(start:-5m) |> filter(fn:(r) => r._measurement == "cpu.usage")'
```

