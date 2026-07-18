---
title: "[Solution] Prometheus Federation Error"
description: "Fix Prometheus federation errors. Learn why this happens and how to resolve it quickly."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Prometheus Federation Error

Prometheus federation errors occur when hierarchical Prometheus instances fail to federate data.

## Why This Happens

- Federation endpoint unreachable
- Data mismatch
- Timeout exceeded
- Auth failed

## Common Error Messages

- `federation_failed`
- `federation_timeout`
- `federation_auth_error`
- `federation_data_error`

## How to Fix It

### Solution 1: Configure federation

Set up federation endpoint:

```yaml
scrape_configs:
  - job_name: 'federate'
    honor_labels: true
    metrics_path: '/federate'
    params:
      'match[]': ['{job="myjob"}']
    static_configs:
      - targets: ['prometheus-1:9090']
```

### Solution 2: Check federation status

Monitor federation scrape duration.

### Solution 3: Fix auth issues

Verify authentication credentials.


## Common Scenarios

- **Federation endpoint unreachable:** Check network connectivity.
- **Data not matching:** Verify label selectors in federation config.

## Prevent It

- Use honor_labels:true
- Monitor federation health
- Document hierarchy
