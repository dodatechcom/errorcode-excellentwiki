---
title: "InfluxDB Check Error"
description: "InfluxDB health check failure"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
InfluxDB health check returns unhealthy status.

## Common Causes
- Service not running
- Port conflict
- Memory exhaustion

## How to Fix
```bash
# Check service status
systemctl status influxdb

# Test health endpoint
curl -s http://localhost:8086/health
```

## Examples
```bash
# Restart service
systemctl restart influxdb
# Check logs
journalctl -u influxdb -n 50 --no-pager
```

