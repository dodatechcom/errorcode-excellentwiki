---
title: "[Solution] Node resources exceeded"
description: "Fix Kubernetes node resource exceeded errors. Resolve pod scheduling failures when a single node does not have enough remaining resources."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Node Resources Exceeded

`0/4 nodes are available: 1 Insufficient cpu, 1 Insufficient memory, 2 node(s) didn't match pod anti-affinity rules`

This error occurs when individual nodes have different resource constraints. The scheduler evaluates each node against the pod's requirements.

### Common Causes

- Multiple resource constraints on different nodes
- CPU requested but only available on nodes without enough memory
- Memory available but only on nodes without enough CPU
- Nodes have different hardware configurations

### How to Fix

Check each node's available resources:
```bash
kubectl describe nodes | grep -A10 "Allocated resources"
```

Consider using multiple node pools with different resource profiles.

Reduce resource requests or increase node capacity.

### Examples

```bash
# Check node resource allocation
kubectl describe nodes | grep -A5 "Allocated resources"
#  Resource           Requests     Limits
#  cpu                3500m/4000m  4500m/4000m
#  memory             6Gi/8Gi      7Gi/8Gi
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})