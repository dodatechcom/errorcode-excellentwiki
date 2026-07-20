---
title: "[Solution] API 429 Too Many Requests"
description: "Fix Kubernetes API 429 Too Many Requests error. Resolve API rate limiting issues when making too many requests."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## API 429 Too Many Requests

This HTTP status code occurs when the client exceeds the API server's rate limit. Kubernetes imposes rate limits to protect the control plane.

### Common Causes

- Automated scripts making rapid API requests
- Monitoring or CI/CD tools polling too frequently
- Watch requests creating excessive load
- Controller or operator in a tight reconciliation loop

### How to Fix

Implement exponential backoff in your application:
```python
import time
time.sleep(1)  # rate limit: 1 QPS
```

Use caching to reduce redundant requests.

Bulk operations instead of individual requests:
```bash
kubectl get pods --all-namespaces  # instead of per-namespace calls
```

### Examples

```bash
# Use list instead of individual get operations
kubectl get deployments --all-namespaces
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})