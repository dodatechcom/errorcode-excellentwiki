---
title: "[Solution] Prometheus Counter Increment Error"
description: "How to fix errors when incrementing Prometheus counters"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Counter value going backwards (reset detected)
- Incrementing counter with negative value
- Counter label changes causing unexpected resets
- Counter renamed without migration plan

## How to Fix

Never decrement a counter:

```python
from prometheus_client import Counter

COUNTER = Counter('requests_total', 'Total requests')

COUNTER.inc()       # Increment by 1
COUNTER.inc(5)      # Increment by 5
COUNTER.inc(1.5)    # Increment by float

# Wrong: counter cannot go backwards
COUNTER.dec()       # This will cause an error
```

Handle counter resets gracefully:

```yaml
# In recording rules
- record: requests:rate5m
  expr: rate(requests_total[5m])
```

## Examples

```bash
# Check counter value
curl -s 'http://localhost:9090/api/v1/query?query=requests_total'

# Calculate rate
curl -s 'http://localhost:9090/api/v1/query?query=rate(requests_total[5m])'

# Check for counter resets
curl -s 'http://localhost:9090/api/v1/query?query=changes(requests_total[1h])'
```
