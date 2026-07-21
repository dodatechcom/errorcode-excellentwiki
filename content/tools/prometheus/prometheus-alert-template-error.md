---
title: "[Solution] Prometheus Alert Template Error"
description: "How to fix Prometheus alert template syntax and rendering errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid Go template syntax in annotations
- Referencing non-existent label or annotation
- Template function not available
- Missing or extra delimiters

## How to Fix

Use correct template syntax:

```yaml
annotations:
  summary: "High error rate on {{ $labels.instance }}"
  description: "Error rate is {{ $value | humanizePercentage }}"
```

Available template variables:

```yaml
# $labels  - all labels of the series
# $value   - current value of the expression
# $labels.instance - specific label
# $labels.job
```

Common template functions:

```yaml
{{ $value | humanize }}          # 1234567 -> 1.235M
{{ $value | humanizePercentage }} # 0.1532 -> 15.32%
{{ $value | humanizeDuration }}   # 365 -> 1h0m0s
```

## Examples

```bash
# Test template rendering
amtool template render --template-file=template.tmpl alertname=HighErrorRate instance=localhost:8080

# Check alert annotations
curl -s http://localhost:9090/api/v1/alerts | jq '.data.alerts[].annotations'
```
