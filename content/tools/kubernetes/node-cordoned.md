---
title: "[Solution] Node is cordoned"
description: "Fix Kubernetes 'node is cordoned' scheduling errors. Resolve pod scheduling failures when nodes are cordoned for maintenance."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Node Is Cordoned

This warning or scheduling failure occurs when a node has been cordoned (marked as unschedulable). No new pods can be scheduled on it.

### Common Causes

- Node was cordoned for maintenance or upgrades
- `kubectl cordon` was run on the node
- Node was drained and not uncordoned

### How to Fix

List cordoned nodes:
```bash
kubectl get nodes | grep SchedulingDisabled
```

Uncordon the node:
```bash
kubectl uncordon <node-name>
```

### Examples

```bash
# Find all cordoned nodes
kubectl get nodes | grep SchedulingDisabled
# node-3   NotReady   SchedulingDisabled

# Uncordon node
kubectl uncordon node-3
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})