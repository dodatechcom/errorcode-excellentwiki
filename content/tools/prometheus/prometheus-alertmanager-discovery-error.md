---
title: "[Solution] Prometheus Alertmanager Discovery Error"
description: "How to fix Prometheus Alertmanager service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- DNS SRV record lookup failure for Alertmanager
- Consul/etcd discovery not returning Alertmanager targets
- Kubernetes service discovery misconfiguration
- Alertmanager cluster endpoints not resolvable

## How to Fix

Use DNS discovery:

```yaml
alerting:
  alertmanagers:
    - dns_sd_configs:
        - names:
            - '_alertmanager._tcp.example.com'
          type: SRV
          refresh_interval: 30s
```

Use static config as fallback:

```yaml
alerting:
  alertmanagers:
    - static_configs:
        - targets:
            - 'alertmanager-1:9093'
            - 'alertmanager-2:9093'
```

## Examples

```bash
# Test DNS SRV lookup
dig _alertmanager._tcp.example.com SRV

# Check discovered Alertmanager targets
curl -s http://localhost:9090/api/v1/alertmanagers | jq '.data.activeAlertmanagers'
```
