---
title: "[Solution] MemoryPressure"
description: "Fix Kubernetes MemoryPressure node condition. Resolve nodes under memory pressure affecting pod scheduling and stability."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## MemoryPressure

A node enters MemoryPressure when its available memory drops below the configured threshold (default 100Mi). The kubelet starts evicting lower-priority pods to reclaim memory.

### Common Causes

- Node memory is overcommitted
- Pods are using more memory than requested
- Memory leak in an application
- Burstable or BestEffort QoS pods consuming excess memory

### How to Fix

Check node memory:
```bash
kubectl top node <node-name>
free -m
```

Check which pods use the most memory:
```bash
kubectl top pods --all-namespaces --sort-by=memory | head -10
```

Set memory limits on problematic pods:
```bash
kubectl set resources deployment/<name> --limits=memory=256Mi
```

### Examples

```bash
# Top memory consumers
kubectl top pods --all-namespaces --sort-by=memory | head -10

# Add more memory or evict pods
kubectl drain <node-name> --ignore-daemonsets
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})