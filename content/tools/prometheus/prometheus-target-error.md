---
title: "[Solution] Prometheus Target Error"
description: "Fix Prometheus target errors. Learn why this happens and how to resolve it quickly."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Prometheus Target Error

Prometheus target errors occur when discovered targets cannot be scraped or are misconfigured.

## Why This Happens

- Target not discovered
- Label cardinality too high
- Target timeout
- Health check failing

## Common Error Messages

- `target_not_found`
- `cardinality_error`
- `target_timeout`
- `target_health_error`

## How to Fix It

### Solution 1: Check service discovery

Verify targets are discovered:

```yaml
scrape_configs:
  - job_name: 'kubernetes'
    kubernetes_sd_configs:
      - role: pod
```

### Solution 2: Limit label cardinality

Use label_relabel_configs to reduce cardinality:

```yaml
metric_relabel_configs:
  - source_labels: [__name__]
    regex: 'go_.*'
    action: drop
```

### Solution 3: Monitor target health

Check the targets page for health status.


## Common Scenarios

- **Target not discovered:** Check service discovery configuration.
- **Cardinality too high:** Drop high-cardinality labels.

## Prevent It

- Monitor target health
- Use relabeling
- Set scrape timeouts
