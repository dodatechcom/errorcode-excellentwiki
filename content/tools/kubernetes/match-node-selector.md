---
title: "[Solution] MatchNodeSelector"
description: "Fix Kubernetes MatchNodeSelector scheduling error. Resolve pods stuck in Pending when nodeSelector cannot be satisfied."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## MatchNodeSelector

`0/4 nodes are available: 4 node(s) didn't match node selector`

This scheduling error means no nodes have labels matching the pod's nodeSelector requirements.

### Common Causes

- Node labels were removed or never set
- pod has a restrictive nodeSelector
- Pod was moved to a cluster without the required labels
- Node pool label differs from what the pod expects

### How to Fix

Check the pod's nodeSelector:
```bash
kubectl get pod <pod-name> -o jsonpath='{.spec.nodeSelector}'
```

List node labels:
```bash
kubectl get nodes --show-labels
```

Remove or relax the nodeSelector:
```bash
kubectl patch deployment <name> -p '{"spec":{"template":{"spec":{"nodeSelector":null}}}}'
```

### Examples

```bash
# Find nodes with specific label
kubectl get nodes -l kubernetes.io/os=linux
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})