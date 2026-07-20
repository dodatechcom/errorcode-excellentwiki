---
title: "[Solution] Preempting (pod being preempted by scheduler)"
description: "Fix Kubernetes pod preemption warnings. Resolve pods that are being preempted (evicted) by the scheduler to make room for higher-priority pods."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Preempting

`Preempting: preempting <pod> to schedule <higher-priority-pod>`

This is a scheduler action where a lower-priority pod is being preempted (evicted) to free resources for a higher-priority pod.

### Common Causes

- Higher priority pod needs resources on the node
- Low-priority pods are scheduled on a node needed for critical workloads
- Scheduler is doing normal priority-based preemption
- No other nodes available for the high-priority pod

### How to Fix

This is expected behavior when using priority classes. To reduce preemption:

- Set appropriate PriorityClass values for your workloads
- Add more nodes to reduce resource contention
- Use podDisruptionBudget on the low-priority pods to limit disruption
- Set preemptionPolicy: Never on the high-priority pod if preemption is not desired

### Examples

```bash
# Check PriorityClasses
kubectl get priorityclass

# Create a balanced priority scheme
kubectl create priorityclass high --value=1000
kubectl create priorityclass medium --value=500
kubectl create priorityclass low --value=100
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})