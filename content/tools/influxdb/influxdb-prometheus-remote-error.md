---
title: "[Solution] InfluxDB Prometheus Remote Write Error — How to Fix"
description: "Fix InfluxDB Prometheus remote write errors when metrics cannot be forwarded to InfluxDB as a remote endpoint"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Prometheus Remote Write Error

Prometheus remote write errors occur when Prometheus cannot send metrics to InfluxDB using the remote write protocol, typically due to authentication, schema, or protocol incompatibilities.

## Why It Happens

- InfluxDB endpoint does not support Prometheus remote write format
- Authentication token is invalid or missing
- Metric labels exceed InfluxDB tag cardinality limits
- Remote write queue is full due to InfluxDB being slow
- TLS certificate validation fails

## Common Error Messages

```
remote write: HTTP status code 401, expected 200
```

```
remote write: queue is full, dropping samples
```

```
remote write: failed to send batch: connection refused
```

```
prometheus remote write: schema conversion error
```

## How to Fix It

### 1. Configure InfluxDB for Prometheus Write

```bash
# InfluxDB v2 supports Prometheus remote write
curl -XPOST 'http://localhost:8086/api/v2/write?org=myorg&bucket=metrics&precision=s' \
  -H 'Authorization: Token prometheus_token' \
  -H 'Content-Type: application/x-protobuf' \
  -d @prometheus_payload
```

### 2. Configure Prometheus Remote Write

```yaml
# prometheus.yml
remote_write:
  - url: "http://influxdb:8086/api/v2/write?org=myorg&bucket=metrics&precision=s"
    bearer_token: "my-influxdb-token"
    queue_config:
      max_samples_per_send: 5000
      batch_send_deadline: 5s
```

### 3. Fix Queue Overflow

```yaml
remote_write:
  - url: "http://influxdb:8086/api/v2/write?org=myorg&bucket=metrics"
    queue_config:
      max_samples_per_send: 10000
      capacity: 50000
      max_shards: 30
```

### 4. Handle Label Cardinality

```yaml
# Drop high-cardinality labels before remote write
metric_relabel_configs:
  - source_labels: [__name__]
    regex: 'debug_.*'
    action: drop
```

## Examples

```
level=warn ts=20240115T103000Z caller=queue_manager.go:553 msg="Remote write queue is full" dropped=15000
```

## Prevent It

- Monitor Prometheus remote write queue metrics
- Set appropriate queue capacity for write throughput
- Use label dropping for high-cardinality metrics

## Related Pages

- [InfluxDB Telegraf Error](/tools/influxdb/influxdb-telegraf-error)
- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
- [InfluxDB Connection Error](/tools/influxdb/influxdb-connection-error)
