---
title: "[Solution] ScyllaDB Monitoring Error — How to Fix"
description: "Fix ScyllaDB monitoring errors by resolving Prometheus scraping issues, fixing Grafana dashboard failures, and recovering from alert rule problems"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Monitoring Error

ScyllaDB monitoring errors occur when the monitoring stack (Prometheus, Grafana, Scylla Monitoring) fails to collect or display metrics. Monitoring is essential for cluster health visibility.

## Why It Happens

- Prometheus cannot scrape ScyllaDB metrics endpoint
- Grafana dashboard shows no data
- Alert rules are misconfigured or firing incorrectly
- ScyllaDB monitoring agent is not running
- Metrics endpoint is not accessible
- Prometheus storage is full

## Common Error Messages

```
MonitoringError: Prometheus scrape failed
```

```
GrafanaError: Dashboard data source not available
```

```
AlertError: Alert rule evaluation failed
```

```
ConnectionError: Cannot reach metrics endpoint
```

## How to Fix It

### 1. Check Monitoring Stack Status

```bash
# Check Prometheus status
sudo systemctl status prometheus
curl http://localhost:9090/api/v1/targets

# Check Grafana status
sudo systemctl status grafana-server
curl http://localhost:3000/api/health

# Check ScyllaDB metrics endpoint
curl http://localhost:9180/metrics
```

### 2. Fix Prometheus Scraping

```yaml
# In prometheus.yml
scrape_configs:
  - job_name: 'scylla'
    static_configs:
      - targets: ['10.0.0.1:9180', '10.0.0.2:9180', '10.0.0.3:9180']
    scrape_interval: 15s
```

```bash
# Verify Prometheus can reach ScyllaDB
curl http://10.0.0.1:9180/metrics | head -20

# Check Prometheus targets status
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[].health'
```

### 3. Fix Grafana Dashboard

```bash
# Check Grafana data source
curl -u admin:admin http://localhost:3000/api/datasources

# Add Prometheus data source
curl -X POST http://localhost:3000/api/datasources \
  -H "Content-Type: application/json" \
  -u admin:admin \
  -d '{
    "name": "Prometheus",
    "type": "prometheus",
    "url": "http://localhost:9090",
    "access": "proxy"
  }'

# Import ScyllaDB dashboards
# Use dashboard IDs from ScyllaDB monitoring repository
```

### 4. Configure Alert Rules

```yaml
# In prometheus rules file
groups:
  - name: scylla_alerts
    rules:
      - alert: ScyllaNodeDown
        expr: scylla_node_info == 0
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "ScyllaDB node is down"

      - alert: ScyllaHighLatency
        expr: histogram_quantile(0.99, rate(scylla_query_latency_seconds_bucket[5m])) > 0.1
        for: 10m
        labels:
          severity: warning
```

## Common Scenarios

- **No metrics in Grafana**: Verify Prometheus is scraping ScyllaDB metrics endpoint.
- **Alerts not firing**: Check alert rule syntax and Prometheus alertmanager configuration.
- **Dashboard shows gaps**: Ensure Prometheus has sufficient storage and retention.

## Prevent It

- Use the official ScyllaDB Monitoring Stack for pre-configured dashboards
- Monitor the monitoring stack itself (Prometheus, Grafana health)
- Set up alerts for monitoring failures (meta-monitoring)

## Related Pages

- [ScyllaDB Nodetool Error](/tools/scylladb/scylladb-nodetool-error)
- [ScyllaDB JMX Error](/tools/scylladb/scylladb-jmx-error)
- [ScyllaDB Node Error](/tools/scylladb/scylladb-node-error)
