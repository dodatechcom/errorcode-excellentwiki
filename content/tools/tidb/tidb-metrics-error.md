---
title: "[Solution] TiDB Metrics Error — How to Fix"
description: "Fix TiDB metrics errors by resolving Prometheus scraping issues, fixing Grafana dashboards, and handling monitoring endpoint problems"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Metrics Error

TiDB metrics errors occur when the monitoring stack fails to collect or display metrics. TiDB exposes metrics via HTTP endpoints on each component.

## Why It Happens

- Prometheus cannot scrape TiDB metrics
- Grafana dashboard shows no data
- Metrics endpoint is not accessible
- Monitoring components are down
- Metrics format changed between versions
- Too many metrics overwhelm monitoring

## Common Error Messages

```
MonitoringError: Prometheus scrape failed
```

```
ERROR: metrics endpoint unreachable
```

```
GrafanaError: no data for TiDB metrics
```

```
ERROR: monitoring component down
```

## How to Fix It

### 1. Check Metrics Endpoints

```bash
# TiDB metrics
curl http://tidb1:10080/metrics

# TiKV metrics
curl http://tikv1:20180/metrics

# PD metrics
curl http://pd1:2379/pd/api/v1/metrics

# TiCDC metrics
curl http://cdc1:8301/metrics
```

### 2. Configure Prometheus

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'tidb'
    static_configs:
      - targets: ['tidb1:10080', 'tidb2:10080']
    metrics_path: '/metrics'

  - job_name: 'tikv'
    static_configs:
      - targets: ['tikv1:20180', 'tikv2:20180']
    metrics_path: '/metrics'

  - job_name: 'pd'
    static_configs:
      - targets: ['pd1:2379', 'pd2:2379']
    metrics_path: '/pd/api/v1/metrics'
```

### 3. Configure Grafana

```bash
# Import TiDB Grafana dashboard
# Use official dashboard: https://grafana.com/grafana/dashboards/12513

# Key metrics to monitor:
# - tidb_server_connections
# - tidb_server_query_total
# - tikv_store_size
# - pd_region_count
```

### 4. Monitor TiDB Health

```bash
# Check component health
curl http://tidb1:10080/status
curl http://tikv1:20180/status
curl http://pd1:2379/pd/api/v1/cluster/status
```

## Common Scenarios

- **Prometheus no data**: Verify metrics_path and target addresses.
- **Grafana shows gaps**: Check Prometheus retention and scrape interval.
- **Metrics endpoint unreachable**: Check firewall rules for metrics ports.

## Prevent It

- Use official TiDB monitoring stack
- Monitor health endpoints with automated checks
- Set up alerts for component failures

## Related Pages

- [TiDB Connection Error](/tools/tidb/tidb-connection-error)
- [TiDB PD Error](/tools/tidb/tidb-pd-error)
- [TiDB TiKV Error](/tools/tidb/tidb-tikv-error)
