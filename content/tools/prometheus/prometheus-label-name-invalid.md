---
title: "[Solution] Prometheus Label Name Invalid"
description: "How to fix invalid label name errors in Prometheus metrics"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Label name contains invalid characters (only [a-zA-Z0-9_])
- Label name starts with a digit
- Label name is empty
- Reserved label names used (e.g., __name__)

## How to Fix

Use only valid characters in label names:

```python
# Wrong
counter = Counter('my_counter', 'Help', ['my-label'])  # hyphen invalid
counter = Counter('my_counter', 'Help', ['123label'])   # starts with digit

# Correct
counter = Counter('my_counter', 'Help', ['my_label'])
counter = Counter('my_counter', 'Help', ['label123'])
```

Valid label name rules:

```bash
# Must match: [a-zA-Z][a-zA-Z0-9_]*
# Examples of valid names:
#   my_label
#   http_status_code
#   __meta_kubernetes
```

Check label names in existing metrics:

```bash
curl -s http://localhost:9090/api/v1/label/__name__/values
```

## Examples

```bash
# Query label names
curl -s 'http://localhost:9090/api/v1/labels' | jq '.data[]'

# Validate metric labels
curl -s http://target:8080/metrics | grep -E '^[a-zA-Z_][a-zA-Z0-9_]*\{'
```
