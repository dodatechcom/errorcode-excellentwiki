---
title: "[Solution] FailedScheduling"
description: "Fix Kubernetes FailedScheduling error. Resolve pods that cannot be scheduled to any node in the cluster."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## FailedScheduling

This error occurs when the Kubernetes scheduler cannot find a suitable node to run the pod. The pod remains in Pending state.

### Common Causes

- Insufficient CPU or memory resources on any node
- Node selector or affinity rules cannot be satisfied
- Pod tolerations do not match node taints
- All nodes have resource pressure (DiskPressure, MemoryPressure)
- PVC not bound or does not exist
- Cluster autoscaler is provisioning new nodes (may be temporary)

### How to Fix

Check the scheduling error:
```bash
kubectl describe pod <pod-name> | grep -A5 "Events"
```

View node resource usage:
```bash
kubectl top nodes
```

Check for taints:
```bash
kubectl describe nodes | grep -i taint
```

### Examples

```bash
kubectl describe pod my-app
#  Events:
#    0/4 nodes are available: 2 Insufficient cpu, 2 Insufficient memory.

# Fix: reduce resource requests or add more nodes
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})