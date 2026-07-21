---
title: "[Solution] Prometheus Stale Sample Error"
description: "How to fix Prometheus stale sample errors when targets disappear or stop reporting"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Target disappeared and stopped sending metrics
- Target restarted with a gap in metric reporting
- Series terminated without proper staleness marker
- Remote write connection dropped

## How to Fix

Configure scrape interval appropriately:

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
```

Adjust staleness delta:

```yaml
storage:
  tsdb:
    staleness_delta: 5m
```

Use `honor_labels` when needed:

```yaml
scrape_configs:
  - job_name: 'app'
    honor_labels: true
```

## Examples

```bash
# Check for stale series
curl -s 'http://localhost:9090/api/v1/query?query=stale' | jq '.data.result'

# Monitor target uptime
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | {instance: .labels.instance, lastScrape: .lastScrape}'
```
