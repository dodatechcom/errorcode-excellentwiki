---
title: "[Solution] LimitRange violation"
description: "Fix Kubernetes LimitRange violations. Resolve pod creation failures when resource limits do not comply with namespace LimitRange."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## LimitRange Violation

This error occurs when a pod's resource requests or limits do not comply with the LimitRange constraints in the namespace.

### Common Causes

- Pod has no resource requests set but LimitRange requires them
- Pod requests are below the minimum LimitRange
- Pod limits exceed the maximum LimitRange

### How to Fix

Check LimitRange:
```bash
kubectl describe limitrange <name> -n <namespace>
```

Set resource requests on the pod:
```yaml
resources:
  requests:
    cpu: 100m
    memory: 128Mi
```

### Examples

```bash
# Check LimitRange constraints
kubectl describe limitrange my-limits -n my-ns
# Type      Resource  Min    Max     Default Request  Default Limit
# Container cpu       100m   1       200m             500m

# Fix pod with no requests
kubectl set resources deployment/my-app --requests=cpu=100m,memory=128Mi
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})