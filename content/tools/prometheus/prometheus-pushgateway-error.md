---
title: "[Solution] Prometheus Pushgateway Error"
description: "Fix Prometheus pushgateway errors. Learn why this happens and how to resolve it quickly."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Prometheus Pushgateway Error

Prometheus pushgateway errors occur when jobs cannot push metrics to the Pushgateway.

## Why This Happens

- Pushgateway unreachable
- Metric name invalid
- Job not registered
- Auth failed

## Common Error Messages

- `push_failed`
- `push_auth_error`
- `metric_name_error`
- `pushgateway_unreachable`

## How to Fix It

### Solution 1: Push metrics correctly

Use the Push API:

```bash
echo "my_metric 42" | curl --data-binary @- http://pushgateway:9091/metrics/job/my_job
```

### Solution 2: Check metric names

Ensure metric names follow naming conventions.

### Solution 3: Verify Pushgateway

Check if Pushgateway is running and accessible.


## Common Scenarios

- **Push failed:** Verify Pushgateway is accessible.
- **Metric not appearing:** Check metric name and job label.

## Prevent It

- Use Push API
- Verify metric naming
- Monitor Pushgateway
