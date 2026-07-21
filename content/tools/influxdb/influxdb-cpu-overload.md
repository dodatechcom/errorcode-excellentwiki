---
title: "[Solution] InfluxDB CPU Overload Error — How to Fix"
description: "Fix InfluxDB CPU overload errors by optimizing queries, reducing write frequency, and tuning thread settings"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB CPU Overload Error

CPU overload errors occur when the InfluxDB server reaches sustained high CPU utilization, causing query timeouts and degraded write performance.

## Why It Happens

- Complex Flux queries performing full table scans
- Too many concurrent queries competing for CPU cycles
- Compaction and merge operations consuming excessive CPU
- Insufficient CPU cores for the workload
- Telegraf or other agents generating too many metrics

## Common Error Messages

```
runtime: scheduler: processor starvation
```

```
error: query timed out due to CPU saturation
```

```
WARN: HTTP request handler slow: took more than 10s
```

## How to Fix It

### 1. Limit Concurrent Queries

```bash
[http]
  max-connections = 100

[coordinator]
  max-concurrent-queries = 20
  query-timeout = "60s"
```

### 2. Optimize Expensive Queries

```bash
# Add time bounds to prevent full scans
influx -execute 'SELECT mean(value) FROM cpu WHERE time > now() - 1h GROUP BY time(5m)'
```

### 3. Monitor CPU Usage

```bash
top -bn1 | grep influxd
pidstat -p $(pgrep influxd) 1 5
```

### 4. Scale Vertically

```bash
# Check current CPU usage
mpstat -P ALL 1 3
# Upgrade instance if consistently above 80%
```

## Examples

```
$ top -bn1 | grep influxd
12345 influxd 85.3% cpu (8 out of 8 cores)
```

## Prevent It

- Set query-timeout to limit long-running queries
- Use continuous aggregates instead of ad-hoc queries
- Monitor CPU metrics and set alerts at 75% utilization

## Related Pages

- [InfluxDB Query Timeout](/tools/influxdb/influxdb-query-timeout)
- [InfluxDB Memory Error](/tools/influxdb/influxdb-memory-error)
- [InfluxDB OOM Error](/tools/influxdb/influxdb-oom-error)
