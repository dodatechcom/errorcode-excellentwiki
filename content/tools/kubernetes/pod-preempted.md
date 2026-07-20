---
title: "[Solution] Pod was preempted by higher priority pod"
description: "Fix Kubernetes pod preemption. Resolve issues when a lower-priority pod is evicted for a higher-priority pod."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Pod Preempted

This occurs when a higher-priority pod cannot be scheduled and the scheduler preempts (evicts) a lower-priority pod to free resources.

### Common Causes

- Higher priority pod needs resources on a full node
- PriorityClass values not balanced properly
- Critical pods preempting non-critical ones

### How to Fix

Check priority classes:
```bash
kubectl get priorityclass
```

Adjust pod priority:
```yaml
priorityClassName: low-priority
```

### Examples

```bash
# Check PriorityClasses
kubectl get priorityclass
# system-cluster-critical   2000000000   true
# system-node-critical      2000001000   true

# Create a low priority class
kubectl create priorityclass low-priority --value=100 --global-default=false
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})