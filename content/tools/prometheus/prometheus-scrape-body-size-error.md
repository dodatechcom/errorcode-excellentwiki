---
title: "[Solution] Prometheus Scrape Body Size Error"
description: "Fix Prometheus scrape body size errors. Resolve metrics response exceeding the maximum body size limit."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

# Prometheus Scrape Body Size Error

Prometheus scrape body size errors occur when the HTTP response from a target exceeds the configured maximum scrape body size, causing metrics to be truncated or discarded.

## Common Causes

- Target exposing an unexpectedly large number of metrics
- Histogram or summary metrics with excessive label cardinality
- Default body size limit of 50MB being exceeded
- Metric name explosion from unbounded label values

## How to Fix It

### Solution 1: Increase the body size limit

Set a higher scrape body size limit:

```yaml
scrape_configs:
  - job_name: "my-app"
    body_size_limit: 100MB
    static_configs:
      - targets: ["localhost:8080"]
```

### Solution 2: Reduce exposed metrics

Filter metrics at the exporter level:

```yaml
scrape_configs:
  - job_name: "my-app"
    metric_relabel_configs:
      - source_labels: [__name__]
        regex: "go_.*"
        action: drop
```

### Solution 3: Check the target metric output

View the raw metrics response size:

```bash
curl -s http://localhost:8080/metrics | wc -c
```

## Prevent It

- Monitor scrape response size per target
- Use metric relabeling to drop unneeded metrics
- Set body_size_limit per job to catch growth early
