---
title: "[Solution] Linux grafana Dashboard Error — Fix"
description: "Fix Linux 'grafana: dashboard error' and dashboard failures. Resolve Grafana datasource issues, panel errors, and dashboard rendering problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["grafana", "dashboard-error", "datasource", "panel", "monitoring", "visualization"]
weight: 5
---

# Linux: grafana: dashboard error

The `grafana: dashboard error` message means Grafana encountered a problem loading, rendering, or querying a dashboard. This can appear as blank panels, "No data" messages, datasource connection failures, or dashboard JSON errors. The error typically indicates a problem with the datasource, query, or Grafana configuration.

## What This Error Means

Grafana dashboards contain panels that query datasources (Prometheus, Elasticsearch, InfluxDB, etc.). When a dashboard fails, it's usually because: the datasource is unreachable, the query has syntax errors, the dashboard JSON is corrupted, or Grafana's backend services are not functioning properly.

## Common Causes

- Datasource (Prometheus, Elasticsearch, etc.) unreachable
- Datasource URL or credentials incorrect
- Dashboard JSON syntax errors
- Query syntax errors in panels
- Grafana database corruption
- Insufficient permissions for the datasource
- Network connectivity issues between Grafana and datasource
- Grafana plugin missing or corrupted

## How to Fix

### 1. Check Grafana Service Status

```bash
# Check Grafana status
sudo systemctl status grafana-server

# Start Grafana if not running
sudo systemctl start grafana-server
sudo systemctl enable grafana-server

# Check Grafana logs
sudo journalctl -u grafana-server --since "10 minutes ago"
```

### 2. Verify Datasource Connectivity

```bash
# Check datasource configuration
curl -s http://admin:admin@localhost:3000/api/datasources | jq .

# Test datasource connection via API
curl -s http://admin:admin@localhost:3000/api/datasources/1/health | jq .

# Test Prometheus directly
curl http://prometheus:9090/api/v1/query?query=up

# Test Elasticsearch directly
curl http://elasticsearch:9200/_cluster/health
```

### 3. Fix Datasource Configuration

```bash
# Update datasource URL via API
curl -X PUT http://admin:admin@localhost:3000/api/datasources/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Prometheus","type":"prometheus","url":"http://prometheus:9090","access":"proxy"}'

# Or via grafana CLI
grafana-cli admin reset-admin-password newpassword
```

### 4. Check Dashboard JSON

```bash
# Export dashboard JSON
curl -s http://admin:admin@localhost:3000/api/dashboards/uid/<dashboard-uid> | jq .

# Validate JSON
echo '{"dashboard":{}}' | jq .

# Check for corrupted dashboards in the database
sudo sqlite3 /var/lib/grafana/grafana.db "SELECT id, title FROM dashboard;"
```

### 5. Fix Grafana Database

```bash
# Backup database first
sudo cp /var/lib/grafana/grafana.db /var/lib/grafana/grafana.db.backup

# Check database integrity
sudo sqlite3 /var/lib/grafana/grafana.db "PRAGMA integrity_check;"

# If corrupted, restore from backup
# Or recreate the database (loses dashboards)
```

### 6. Fix Permissions

```bash
# Check Grafana user permissions
ls -la /var/lib/grafana/
ls -la /var/log/grafana/

# Fix ownership
sudo chown -R grafana:grafana /var/lib/grafana/
sudo chown -R grafana:grafana /var/log/grafana/
sudo chown -R grafana:grafana /etc/grafana/
```

### 7. Check Grafana Plugins

```bash
# List installed plugins
grafana-cli plugins ls

# Install missing plugin
grafana-cli plugins install <plugin-name>

# Update all plugins
grafana-cli plugins update-all

# Restart Grafana after plugin changes
sudo systemctl restart grafana-server
```

## Examples

```bash
# Check Grafana status
$ sudo systemctl status grafana-server
● grafana-server.service - Grafana instance
     Active: active (running) since ...

# Check datasource health
$ curl -s http://admin:admin@localhost:3000/api/datasources/1/health
{"status":"ok","message":"Data source is healthy"}

# Check dashboard
$ curl -s http://admin:admin@localhost:3000/api/dashboards/uid/my-dashboard | jq '.dashboard.title'
"Server Metrics"

# Panels showing "No data" — check Prometheus
$ curl http://prometheus:9090/api/v1/query?query=up
{"status":"success","data":{"resultType":"vector","result":[]}}
# No targets are up — fix Prometheus targets
```

## Related Errors

- [Prometheus scrape error]({{< relref "/os/linux/linux-prometheus-error" >}}) — Metrics collection failures
- [Elasticsearch cluster error]({{< relref "/os/linux/linux-elasticsearch-error" >}}) — Data storage issues
- [Connection refused]({{< relref "/os/linux/connection-refused7" >}}) — Network connectivity issues
