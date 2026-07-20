---
title: "[Solution] Insufficient CPU"
description: "Fix Kubernetes Insufficient CPU scheduling error. Resolve pods that cannot be scheduled because no node has enough available CPU."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Insufficient CPU

`0/4 nodes are available: 4 Insufficient cpu`

This scheduling error occurs when every node in the cluster has insufficient available CPU capacity to meet the pod's resource request.

### Common Causes

- Pod CPU request is set too high
- Cluster is at capacity with other workloads
- Node CPU requests are overallocated
- Too many pods running on the nodes

### How to Fix

Check node resources:
```bash
kubectl top nodes
```

Reduce CPU request in the pod spec:
```bash
kubectl set resources deployment/my-app --requests=cpu=200m --limits=cpu=500m
```

Add more nodes to the cluster.

### Examples

```bash
# Reduce CPU request
kubectl set resources deployment/my-app --requests=cpu=200m --limits=cpu=500m
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})