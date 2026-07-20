---
title: "[Solution] PodFitsResources predicate failed"
description: "Fix Kubernetes PodFitsResources scheduling failures. Resolve pods that cannot be scheduled due to cumulative resource constraints."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## PodFitsResources Failed

`0/4 nodes are available: 4 Insufficient cpu, 3 Insufficient memory`

This error occurs when the scheduler evaluates nodes and finds that no node has enough remaining resources for the pod.

### Common Causes

- Pod's resource requests exceed available resources on all nodes
- Cluster has been scaled down and cannot accommodate new pods
- Many pods with small requests but cumulative total is high
- Node allocatable resources are less than capacity due to reserved resources

### How to Fix

Check aggregate cluster resource usage:
```bash
kubectl top nodes
kubectl describe nodes | grep -A5 "Allocated resources"
```

Reduce resource requests or add nodes.

Check for reserved resources on nodes:
```bash
kubectl describe node <name> | grep -i "Allocatable"
```

### Examples

```bash
# Check allocatable vs capacity
kubectl describe node <name> | grep -E "Capacity|Allocatable"
# cpu:                4
# cpu:                3920m
# memory:             8192088Ki
# memory:             7986008Ki
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})