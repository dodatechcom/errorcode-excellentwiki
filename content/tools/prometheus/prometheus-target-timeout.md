---
title: "[Solution] Prometheus Target Scrape Timeout"
description: "How to fix Prometheus target scrape timeout when endpoints respond too slowly"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Target application is slow to respond
- Network latency between Prometheus and target
- `scrape_timeout` set too low
- Target under heavy load
- Large metrics payload taking too long to transfer

## How to Fix

Increase the scrape timeout:

```yaml
global:
  scrape_timeout: 30s
```

Per-job timeout override:

```yaml
scrape_configs:
  - job_name: 'slow-app'
    scrape_timeout: 60s
    static_configs:
      - targets: ['slow-host:8080']
```

Check if target responds within timeout:

```bash
time curl -s http://target-host:8080/metrics > /dev/null
```

Increase HTTP client timeout:

```yaml
scrape_configs:
  - job_name: 'app'
    scrape_timeout: 30s
    http_client_config:
      follow_redirects: true
```

## Examples

```bash
# Measure scrape duration
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | {instance: .labels.instance, lastScrapeDuration: .lastScrapeDuration}'

# Test response time
curl -o /dev/null -s -w '%{time_total}\n' http://target-host:8080/metrics
```
