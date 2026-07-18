---
title: "[Solution] YugabyteDB Monitoring Error — How to Fix"
description: "Fix YugabyteDB monitoring errors by resolving Prometheus scraping issues, fixing Grafana dashboards, and configuring health check endpoints"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Monitoring Error

YugabyteDB monitoring errors occur when the monitoring stack fails to collect or display metrics. YugabyteDB exposes metrics via HTTP endpoints on each node.

## Why It Happens

- Metrics endpoint is not accessible
- Prometheus cannot scrape YugabyteDB metrics
- Grafana dashboard shows no data
- Health check endpoint returns errors
- Metrics format has changed between versions
- Too many metrics overwhelm monitoring system

## Common Error Messages

```
MonitoringError: Prometheus scrape failed
```

```
ERROR: metrics endpoint unreachable
```

```
ERROR: health check failed
```

```
GrafanaError: no data for YugabyteDB metrics
```

## How to Fix It

### 1. Check Metrics Endpoints

```bash
# TServer metrics
curl http://yb-tserver-1:9000/metrics

# Master metrics
curl http://yb-master-1:7000/metrics

# Health check
curl http://yb-tserver-1:9000/healthz
curl http://yb-master-1:7000/healthz

# Prometheus format
curl http://yb-tserver-1:9000/prometheus-metrics
```

### 2. Configure Prometheus

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'yugabyte-tserver'
    static_configs:
      - targets: ['yb-tserver-1:9000', 'yb-tserver-2:9000', 'yb-tserver-3:9000']
    metrics_path: '/prometheus-metrics'
    scrape_interval: 15s

  - job_name: 'yugabyte-master'
    static_configs:
      - targets: ['yb-master-1:7000', 'yb-master-2:7000', 'yb-master-3:7000']
    metrics_path: '/prometheus-metrics'
    scrape_interval: 15s
```

### 3. Configure Grafana Dashboard

```bash
# Import YugabyteDB Grafana dashboard
# Use official dashboard: https://grafana.com/grafana/dashboards/12513

# Or create custom dashboard
# Key metrics:
# - yugabyte_tserver_total_tablets
# - yugabyte_tserver_total_rpc_latency
# - yugabyte_cluster_active_connections
```

### 4. Monitor Health

```bash
# Check cluster health
curl http://yb-master-1:7000/cluster-config | jq '.tablet_servers'

# Check node health
for node in yb-tserver-1 yb-tserver-2 yb-tserver-3; do
  echo "$node: $(curl -s http://$node:9000/healthz)"
done
```

## Common Scenarios

- **Metrics endpoint unreachable**: Check firewall rules for port 9000/7000.
- **Prometheus no data**: Verify metrics_path and target addresses.
- **Grafana shows gaps**: Check Prometheus retention and scrape interval.

## Prevent It

- Use official YugabyteDB monitoring stack
- Monitor health endpoints with automated checks
- Set up alerts for node failures and high latency

## Related Pages

- [YugabyteDB TServer Error](/tools/yugabyte/yugabyte-tserver-error)
- [YugabyteDB Master Error](/tools/yugabyte/yugabyte-master-error)
- [YugabyteDB Config Error](/tools/yugabyte/yugabyte-gflag-error)
