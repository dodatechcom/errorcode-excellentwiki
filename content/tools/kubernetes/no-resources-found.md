---
title: "[Solution] No resources found"
description: "Fix kubectl 'No resources found' message. Resolve cases where kubectl commands return empty results in a namespace."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## No Resources Found

`No resources found in <namespace> namespace.`

This message means kubectl successfully connected to the API server but found no matching resources. This may be expected or indicate a misconfiguration.

### Common Causes

- Empty namespace (no resources deployed yet)
- Wrong namespace specified
- Wrong resource name or label selector
- Resources were deleted

### How to Fix

List all resources in the namespace:
```bash
kubectl get all
```

List resources in all namespaces:
```bash
kubectl get pods --all-namespaces
```

### Examples

```bash
# List all namespaces
kubectl get ns

# List pods in all namespaces
kubectl get pods -A
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})