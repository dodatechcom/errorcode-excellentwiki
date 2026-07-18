---
title: "[Solution] InfluxDB Monitoring Error — How to Fix"
description: "Fix InfluxDB monitoring errors including monitoring agent failures, metric collection issues, and dashboard problems in Chronograf or Grafana"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Monitor Error

Monitoring errors in InfluxDB occur when the monitoring agent fails to collect system metrics, Chronograf dashboards show incorrect data, or alerting rules do not fire.

## Why It Happens

- The monitoring agent is not running or configured
- The internal metrics database is not receiving data
- Chronograf cannot connect to InfluxDB
- The monitoring queries are incorrect
- The alert thresholds are set incorrectly

## Common Error Messages

```
monitoring agent error: connection refused
```

```
failed to query monitoring data: database not found
```

```
alert rule error: invalid threshold
```

```
chronograf error: cannot connect to InfluxDB
```

## How to Fix It

### 1. Check Monitoring Configuration

```bash
# In influxdb.conf
[monitoring]
  enabled = true
  write-interval = "10s"
  enabled-storage-engine = true
```

### 2. Fix Internal Metrics Collection

```influxql
-- Check if internal metrics are being collected
SHOW DATABASES
SHOW MEASUREMENTS ON _internal

-- Query internal metrics
SELECT mean(queryDurationNs) FROM _internal.monitor."query" WHERE time > now() - 1h GROUP BY time(5m)
```

### 3. Fix Chronograf Connection

```bash
# Chronograf configuration
export INFLUXDB_URL=http://localhost:8086
export INFLUXDB_USERNAME=admin
export INFLUXDB_PASSWORD=password

# Test Chronograf connection
curl http://localhost:8086/ping
```

### 4. Fix Monitoring Alerts

```bash
# Create an alert rule in Chronograf
# Or use Kapacitor for custom alerts
kapacitor define cpu_alert -type stream -tick cpu_alert.tick
kapacitor enable cpu_alert
```

## Common Scenarios

- **No data in dashboards**: Ensure the monitoring agent is running and collecting data.
- **Alerts not firing**: Check alert thresholds and endpoint configuration.
- **Chronograf cannot connect**: Verify InfluxDB credentials and URL.

## Prevent It

- Set up monitoring for the monitoring system itself
- Test alert rules on staging before deploying
- Document the monitoring architecture and alert thresholds

## Related Pages

- [InfluxDB Connection Error](/tools/influxdb/influxdb-connection-error)
- [InfluxDB Auth Error](/tools/influxdb/influxdb-auth-error)
- [InfluxDB Telegraf Error](/tools/influxdb/influxdb-telegraf-error)
