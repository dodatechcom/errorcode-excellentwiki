---
title: "[Solution] Prometheus Scrape Slow Target Error"
description: "Fix Prometheus scrape slow target errors. Resolve targets taking too long to respond during scrape."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

# Prometheus Scrape Slow Target Error

Prometheus scrape slow target errors occur when a target takes longer than the scrape timeout to return its metrics response, causing the scrape to fail.

## Common Causes

- Target application is under heavy load and slow to respond
- scrape_timeout too short for the target's metric generation
- Target computing expensive metrics on each scrape
- Network latency between Prometheus and the target

## How to Fix It

### Solution 1: Increase the scrape timeout

Set a longer timeout for slow targets:

```yaml
scrape_configs:
  - job_name: "slow-app"
    scrape_timeout: 30s
    scrape_interval: 60s
    static_configs:
      - targets: ["slow-app:8080"]
```

### Solution 2: Use a dedicated scrape job with longer interval

Separate slow targets into their own job:

```yaml
scrape_configs:
  - job_name: "fast-apps"
    scrape_interval: 15s
    scrape_timeout: 10s
    static_configs:
      - targets: ["app1:8080"]

  - job_name: "slow-apps"
    scrape_interval: 60s
    scrape_timeout: 45s
    static_configs:
      - targets: ["app2:8080"]
```

### Solution 3: Check target response time

Measure the target metrics endpoint:

```bash
time curl -s http://slow-app:8080/metrics > /dev/null
```

## Prevent It

- Separate fast and slow targets into different scrape jobs
- Use shorter metric generation time in target applications
- Monitor the up metric for consistent scrape failures
