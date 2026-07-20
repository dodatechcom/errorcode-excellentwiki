---
title: "[Solution] Pod Evicted"
description: "Fix Kubernetes pod eviction. Resolve pods that are evicted from nodes due to resource pressure or taints."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Pod Evicted

A pod enters the Evicted status when the kubelet evicts it from a node. This is a protection mechanism to reclaim resources for higher-priority workloads.

### Common Causes

- Node disk pressure (DiskPressure)
- Node memory pressure (MemoryPressure)
- Node PID pressure (PIDPressure)
- Node pressure condition resolved, but pods remain in evicted status
- Pod exceeded ephemeral storage limit
- Node became unreachable (NodeLost)

### How to Fix

Check the eviction reason:
```bash
kubectl get pod <pod-name> -o jsonpath='{.status.reason}'
```

List evicted pods:
```bash
kubectl get pods --field-selector=status.phase=Failed
```

Remove evicted pods:
```bash
kubectl delete pod <pod-name>
```

Clean up all evicted pods:
```bash
kubectl get pods --all-namespaces | grep Evicted | awk '{print $2 " -n " $1}' | xargs kubectl delete pod
```

### Examples

```bash
# Remove all evicted pods
kubectl get pods --all-namespaces | grep Evicted | while read ns pod rest; do kubectl delete pod -n $ns $pod; done
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})