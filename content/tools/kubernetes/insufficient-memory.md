---
title: "[Solution] Insufficient Memory"
description: "Fix Kubernetes Insufficient Memory scheduling error. Resolve pods that cannot be scheduled due to memory constraints on all nodes."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Insufficient Memory

`0/4 nodes are available: 4 Insufficient memory`

This scheduling error occurs when no node in the cluster has enough available memory to run the pod.

### Common Causes

- Pod memory request is too high
- Cluster memory is fully utilized by existing workloads
- Memory leak in other pods consuming excessive memory
- Nodes have memory pressure condition

### How to Fix

Check node memory usage:
```bash
kubectl top nodes
```

Reduce memory request:
```bash
kubectl set resources deployment/my-app --requests=memory=256Mi --limits=memory=512Mi
```

### Examples

```bash
# Reduce memory request
kubectl set resources deployment/my-app --requests=memory=256Mi --limits=memory=512Mi
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})