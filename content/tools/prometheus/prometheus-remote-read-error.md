---
title: "[Solution] Prometheus Remote Read Error"
description: "How to fix Prometheus remote read errors when querying remote storage"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Remote read endpoint unreachable
- Authentication or authorization failure
- Query timeout too short
- Data format mismatch between Prometheus and remote storage
- TLS configuration errors

## How to Fix

Configure remote read:

```yaml
remote_read:
  - url: 'http://remote-storage:9201/api/v1/read'
    read_recent: true
    tls_config:
      ca_file: /etc/prometheus/ca.crt
    basic_auth:
      username: prometheus
      password_file: /etc/prometheus/password
```

Check remote read status:

```bash
curl -s http://localhost:9090/api/v1/status/runtimeinfo | jq '.data.remoteRead'
```

## Examples

```bash
# Test remote read endpoint
curl -X POST http://remote-storage:9201/api/v1/read -d '{}'

# Monitor remote read queries
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_remote_read_queries_total'
```
