---
title: "[Solution] Prometheus Gauge Set Error"
description: "How to fix errors when setting Prometheus gauge values"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Setting gauge to NaN or Inf
- Gauge value type mismatch (string where number expected)
- Gauge decremented below zero without tracking
- Concurrent gauge modifications causing race conditions

## How to Fix

Use proper gauge operations:

```python
from prometheus_client import Gauge

GAUGE = Gauge('connections', 'Active connections')

GAUGE.set(42)              # Set absolute value
GAUGE.inc()                # Increment by 1
GAUGE.inc(5)               # Increment by 5
GAUGE.dec()                # Decrement by 1
GAUGE.set_to_current_time() # Set to current timestamp
```

Avoid setting NaN:

```python
# Wrong
GAUGE.set(float('nan'))

# Correct
if value is not None and math.isfinite(value):
    GAUGE.set(value)
```

## Examples

```bash
# Check gauge value
curl -s 'http://localhost:9090/api/v1/query?query=connections'

# View gauge history
curl -s 'http://localhost:9090/api/v1/query_range?query=connections&start=1h ago&step=60s'
```
