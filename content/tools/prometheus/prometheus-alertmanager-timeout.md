---
title: "[Solution] Prometheus Alertmanager Timeout Error"
description: "How to fix Prometheus Alertmanager connection timeout errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Alertmanager under heavy load
- Network latency between Prometheus and Alertmanager
- Alertmanager processing large notification batch
- Timeout configuration too low

## How to Fix

Configure Alertmanager timeout:

```yaml
alerting:
  alertmanagers:
    - timeout: 30s
      static_configs:
        - targets:
          - 'localhost:9093'
```

Check Alertmanager response time:

```bash
time curl http://localhost:9093/api/v2/status
```

Increase Alertmanager resources:

```bash
# Check Alertmanager metrics
curl http://localhost:9093/metrics | grep "notification_duration"
```

## Examples

```bash
# Measure Alertmanager latency
curl -o /dev/null -s -w '%{time_total}\n' http://localhost:9093/api/v2/alerts

# Check Alertmanager processing
curl http://localhost:9093/metrics | grep "alertmanager_notifications_total"
```
