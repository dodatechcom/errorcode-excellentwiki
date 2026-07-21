---
title: "[Solution] Prometheus Scrape Timeout Exceeded"
description: "How to fix Prometheus scrape timeout exceeded errors for slow targets"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Target application taking too long to respond
- Network congestion or packet loss
- Target exporting a very large number of metrics
- `scrape_timeout` too low for the workload

## How to Fix

Increase global scrape timeout:

```yaml
global:
  scrape_timeout: 30s
```

Per-target timeout configuration:

```yaml
scrape_configs:
  - job_name: 'large-app'
    scrape_timeout: 60s
    static_configs:
      - targets: ['large-host:8080']
```

Reduce metrics cardinality on target:

```bash
# Check metric count on target
curl -s http://target:8080/metrics | wc -l
```

## Examples

```bash
# Monitor scrape durations
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | {instance: .labels.instance, lastScrape: .lastScrapeDuration}'

# Find slow targets
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.lastScrapeDuration > 10) | .labels.instance'
```
