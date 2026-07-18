---
title: "[Solution] InfluxDB TICK Script Error — How to Fix"
description: "Fix InfluxDB TICK script errors including Kapacitor alert failures, Telegraf configuration issues, and Chronograf dashboard problems"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB TICK Script Error

TICK script errors in InfluxDB occur when using Kapacitor for alerting and processing, Telegraf for data collection, or Chronograf for visualization.

## Why It Happens

- The TICK script has syntax errors
- The script references non-existent measurements or fields
- The alert endpoint is unreachable
- The script logic causes infinite loops
- The script requires functions not available in the current Kapacitor version

## Common Error Messages

```
tick script error: invalid TICK script syntax
```

```
alert error: failed to send alert to endpoint
```

```
stream error: measurement not found
```

```
tick error: function not supported
```

## How to Fix It

### 1. Validate TICK Script

```bash
# Validate a TICK script
kapacitor define my_alert -type stream -tick /path/to/script.tick

# Check script status
kapacitor list
```

### 2. Fix TICK Script Syntax

```go
// GOOD: valid TICK script
stream
  |from()
    .measurement('cpu')
    .where(lambda: "host" == 'server01')
  |window()
    .period(5m)
    .every(1m)
  |mean('value')
  |alert()
    .crit(lambda: "mean" > 90.0)
    .httpPost('http://alert-endpoint:5000/alert')
```

### 3. Fix Alert Endpoint

```bash
# Test alert endpoint
curl -XPOST 'http://alert-endpoint:5000/alert' \
  -d '{"alert":"test","level":"crit"}'

# Check Kapacitor logs
journalctl -u kapacitor | grep -i alert
```

### 4. Fix TICK Script for Measurement

```go
// BAD: measurement does not exist
stream
  |from()
    .measurement('nonexistent')

// GOOD: verify measurement exists first
stream
  |from()
    .measurement('cpu')
    .database('mydb')
```

## Common Scenarios

- **Alert not firing**: Check if the measurement exists and the alert condition is correct.
- **TICK script syntax error**: Use Kapacitor's validate command to check syntax.
- **Alert endpoint unreachable**: Ensure the endpoint is running and accessible.

## Prevent It
- Test TICK scripts on staging before deploying
- Use Chronograf to create and manage TICK scripts
- Monitor Kapacitor logs for errors

## Related Pages

- [InfluxDB Task Error](/tools/influxdb/influxdb-task-error)
- [InfluxDB Monitor Error](/tools/influxdb/influxdb-monitor-error)
- [InfluxDB Telegraf Error](/tools/influxdb/influxdb-telegraf-error)
