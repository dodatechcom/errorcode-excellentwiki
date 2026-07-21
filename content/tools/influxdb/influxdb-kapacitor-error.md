---
title: "[Solution] InfluxDB Kapacitor Error — How to Fix"
description: "Fix InfluxDB Kapacitor alert and task processing errors when TICKscript tasks fail to execute"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Kapacitor Error

Kapacitor errors occur when the TICKscript-based alerting and processing engine fails to execute tasks, write data back to InfluxDB, or deliver alert notifications.

## Why It Happens

- TICKscript contains syntax errors or invalid functions
- Kapacitor cannot connect to the InfluxDB instance
- Alert handlers are misconfigured
- Task window is larger than available data in InfluxDB
- Kapacitor is running out of memory processing high-cardinality streams

## Common Error Messages

```
ts: error: task failed: connection refused to InfluxDB
```

```
err: tick script parse error: unknown function "mean"
```

```
kapacitor: ERROR: alert handler failed to send notification
```

```
error: task execution exceeded memory limit
```

## How to Fix It

### 1. Validate TICKscript Syntax

```bash
kapacitor define -name cpu_alert -tick /path/to/cpu_alert.tick -dbrp mydb.autogen
```

### 2. Test InfluxDB Connection from Kapacitor

```bash
curl -s http://localhost:9092/ping
kapacitor show cpu_alert
```

### 3. Check Task Status

```bash
kapacitor list
kapacitor show cpu_alert
kapacitor logs -task cpu_alert
```

### 4. Fix TICKscript Errors

```tick
stream
    |from()
        .database('mydb')
        .measurement('cpu')
    |window()
        .period(5m)
        .every(1m)
    |mean('value')
    |alert()
        .crit(lambda: "mean" > 90)
        .log('/var/log/kapacitor/alerts.log')
```

## Examples

```
$ kapacitor list
ID         Type      Status    Executing
cpu_alert  stream    enabled   true
disk_crit  batch     error     false
```

## Prevent It

- Test TICKscripts with kapacitor define before enabling
- Monitor Kapacitor task execution metrics
- Set appropriate memory limits for complex tasks

## Related Pages

- [InfluxDB Telegraf Error](/tools/influxdb/influxdb-telegraf-error)
- [InfluxDB Task Error](/tools/influxdb/influxdb-task-error)
- [InfluxDB Notification Rule Error](/tools/influxdb/influxdb-notification-rule-error)
