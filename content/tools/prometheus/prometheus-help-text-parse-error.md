---
title: "[Solution] Prometheus HELP Text Parse Error"
description: "How to fix HELP text parsing errors in Prometheus exposition format"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Malformed HELP line in metrics output
- HELP text contains newline characters
- HELP text encoding issues (non-UTF8)
- HELP line does not match the metric name

## How to Fix

Ensure correct HELP format:

```python
# Wrong: HELP line with newline
HELP my_metric Description with\nnewline

# Correct: single line HELP
HELP my_metric Description with spaces
```

Validate exposition format:

```bash
curl -s http://target:8080/metrics | grep -E "^# (HELP|TYPE)"
```

Check for encoding issues:

```bash
curl -s http://target:8080/metrics | file -
```

## Examples

```bash
# View HELP text for a metric
curl -s http://target:8080/metrics | grep -A 1 "# HELP my_metric"

# Validate all HELP lines
curl -s http://target:8080/metrics | grep "^# HELP" | head -10

# Check for parsing errors in logs
journalctl -u prometheus | grep "parse error"
```
