---
title: "[Solution] Node selector mismatch"
description: "Fix Kubernetes nodeSelector scheduling error. Resolve pods that cannot be scheduled because no node has the required labels."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Node Selector Mismatch

`0/4 nodes are available: 4 node(s) didn't match node selector`

This scheduling error occurs when no node has the labels required by the pod's `nodeSelector`. The pod can only run on nodes with matching labels.

### Common Causes

- Node selector label does not exist on any node
- Node labels were removed or renamed
- Labels are case-sensitive
- Pod was deployed to wrong cluster

### How to Fix

Check node labels:
```bash
kubectl get nodes --show-labels
```

Add label to a node:
```bash
kubectl label nodes <node-name> <key>=<value>
```

### Examples

```bash
# Find nodes with specific label
kubectl get nodes -l disktype=ssd

# Label a node
kubectl label nodes node1 disktype=ssd
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})