---
title: "[Solution] Node pressure eviction"
description: "Fix Kubernetes node pressure eviction. Resolve pods evicted due to resource pressure on the node."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Node Pressure Eviction

`The node was low on resource: <resource>. Evicted pod <name>.`

This occurs when the kubelet evicts pods from a node due to resource pressure (disk, memory, PID).

### Common Causes

- DiskPressure triggered eviction (most common)
- MemoryPressure triggered eviction
- PIDPressure triggered eviction
- BestEffort QoS pods evicted first
- Burstable QoS pods evicted next
- Guaranteed QoS pods evicted last

### How to Fix

Check node conditions before eviction:
```bash
kubectl describe node <node-name>
```

Set appropriate resource limits on all pods:
```yaml
resources:
  limits:
    memory: 512Mi
  requests:
    memory: 256Mi
```

Add more nodes to the cluster.

### Examples

```bash
# Check for evicted pods
kubectl get pods --all-namespaces -o wide | grep Evicted

# Clean up evicted pods
kubectl get pods --all-namespaces | grep Evicted | awk '{print $2 " -n " $1}' | xargs kubectl delete pod
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})