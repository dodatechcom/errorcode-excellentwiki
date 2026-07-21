---
title: "[Solution] Prometheus TYPE Line Invalid"
description: "How to fix invalid TYPE declaration lines in Prometheus exposition format"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- TYPE line does not match a following metric line
- Invalid type value (must be counter, gauge, histogram, summary, or untyped)
- TYPE declared after metric samples instead of before
- Multiple TYPE declarations for the same metric

## How to Fix

Ensure correct TYPE format:

```
# Wrong
# TYPE my_metric counter
# TYPE my_metric gauge
my_metric 42

# Correct
# TYPE my_metric gauge
my_metric 42
```

Valid TYPE values:

```
# TYPE my_counter counter
# TYPE my_gauge gauge
# TYPE my_histogram histogram
# TYPE my_summary summary
# TYPE my_metric untyped
```

Validate with promtool:

```bash
promtool check metrics < target-metrics.txt
```

## Examples

```bash
# Check TYPE lines on target
curl -s http://target:8080/metrics | grep "^# TYPE"

# Validate metrics format
curl -s http://target:8080/metrics | promtool check metrics

# View parsed metric types
curl -s 'http://localhost:9090/api/v1/query?query=metric_metadata'
```
