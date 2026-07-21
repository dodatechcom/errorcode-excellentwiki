---
title: "[Solution] InfluxDB Dashboard Error — How to Fix"
description: "Fix InfluxDB dashboard loading errors by clearing browser cache, verifying API tokens, and checking Grafana connectivity"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Dashboard Error

Dashboard errors occur when the InfluxDB UI or connected dashboard tools like Grafana fail to load, render, or update visualizations.

## Why It Happens

- API token lacks read permissions for the dashboard data
- Browser cache contains stale dashboard configuration
- Dashboard queries exceed the default query timeout
- Grafana cannot reach the InfluxDB endpoint
- Dashboard JSON contains invalid query syntax

## Common Error Messages

```
error: dashboard failed to load: unauthorized
```

```
Grafana: InfluxDB Flux query error: unauthorized access
```

```
{"error":"failed to fetch dashboard: connection refused"}
```

## How to Fix It

### 1. Verify API Token Permissions

```bash
influx auth list --org myorg
influx auth create --org myorg --read-bucket mydb --description "dashboard-read"
```

### 2. Clear Browser Cache

```bash
# Hard refresh in browser
Ctrl+Shift+R

# Or clear InfluxDB UI cache
curl -XDELETE 'http://localhost:8086/cache'
```

### 3. Test Dashboard Queries

```bash
curl -XPOST 'http://localhost:8086/api/v2/query?org=myorg' \
  -H 'Authorization: Token mytoken' \
  -H 'Content-Type: application/vnd.flux' \
  -d 'from(bucket:"mydb") |> range(start:-1h) |> mean()'
```

### 4. Check Grafana Datasource

```bash
# Test InfluxDB connection from Grafana
curl -XGET 'http://grafana:3000/api/datasources/1/health' \
  -H 'Authorization: Bearer admin-api-key'
```

## Examples

```
Grafana Error: InfluxDB Flux: unauthorized access
Token: mydashboardtoken lacks read permission on bucket mydb
```

## Prevent It

- Use read-only tokens for dashboard access
- Set up datasource health checks in Grafana
- Regularly validate dashboard queries against current schema

## Related Pages

- [InfluxDB Auth Error](/tools/influxdb/influxdb-auth-error)
- [InfluxDB Query Error](/tools/influxdb/influxdb-query-error)
- [InfluxDB Connection Error](/tools/influxdb/influxdb-connection-error)
