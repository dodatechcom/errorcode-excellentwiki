---
title: "InfluxDB UDP Error"
description: "UDP listener failure"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
InfluxDB UDP listener cannot receive data.

## Common Causes
- UDP port not configured
- Firewall blocking UDP
- Buffer overflow

## How to Fix
```yaml
# influxdb.conf UDP settings
[[udp]]
  enabled = true
  bind-address = ":8089"
  database = "udp"
  buffer-size = 1000
```

## Examples
```bash
# Test UDP reception
echo "cpu,host=server1 value=0.5" | nc -u localhost 8089
# Check UDP stats
netstat -ulnp | grep 8089
```

