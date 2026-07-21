---
title: "[Solution] Prometheus Naming Convention Error"
description: "Fix Prometheus naming convention errors. Resolve metric name validation failures from invalid names."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

# Prometheus Naming Convention Error

Prometheus naming convention errors occur when metric names do not follow the required format of alphanumeric characters and underscores, starting with a letter.

## Common Causes

- Metric name starts with a number or underscore
- Metric name contains hyphens, dots, or other invalid characters
- Exporter generating non-compliant metric names
- Metric name exceeding the maximum length

## How to Fix It

### Solution 1: Validate metric names

Check metric naming rules -- names must match [a-zA-Z_:][a-zA-Z0-9_:]*:

```bash
curl -s http://localhost:8080/metrics | grep -v '^[a-zA-Z_:]' | head -10
```

### Solution 2: Use metric relabeling to fix names

Rename invalid metrics at scrape time:

```yaml
scrape_configs:
  - job_name: "my-app"
    metric_relabel_configs:
      - source_labels: [__name__]
        regex: "app-metric-name(.*)"
        target_label: __name__
        replacement: "app_metric_name$1"
```

### Solution 3: Check exporter metric generation

If using a custom exporter, fix the metric registration:

```go
// Invalid
prometheus.NewGauge(prometheus.GaugeOpts{
    Name: "app-metric-name",
})

// Correct
prometheus.NewGauge(prometheus.GaugeOpts{
    Name: "app_metric_name",
})
```

## Prevent It

- Follow Prometheus naming conventions in all new metrics
- Use metric relabeling to correct invalid names at scrape time
- Run promtool check metrics before deploying exporters
