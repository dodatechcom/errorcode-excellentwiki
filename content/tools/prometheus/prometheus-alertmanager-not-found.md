---
title: "[Solution] Prometheus Alertmanager Not Found"
description: "How to fix Prometheus cannot find or connect to Alertmanager"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Alertmanager URL misconfigured in Prometheus
- Alertmanager not running
- DNS resolution failure for Alertmanager host
- Network firewall blocking connection
- Alertmanager listening on different port

## How to Fix

Configure Alertmanager in prometheus.yml:

```yaml
alerting:
  alertmanagers:
    - static_configs:
        - targets:
          - 'localhost:9093'
```

Check Alertmanager status:

```bash
curl http://localhost:9093/-/healthy
curl http://localhost:9093/api/v2/status
```

Verify Prometheus can reach Alertmanager:

```bash
curl -s http://localhost:9090/api/v1/status/config | jq '.data.yaml' | grep -A 5 alerting
```

## Examples

```bash
# Check Alertmanager connectivity
curl http://localhost:9093/-/healthy

# Verify Prometheus targets include Alertmanager
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.labels.job == "alertmanager")'

# Check Alertmanager config
amtool config show --alertmanager.url=http://localhost:9093
```
