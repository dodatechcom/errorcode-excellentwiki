---
title: "[Solution] Insufficient Pods"
description: "Fix Kubernetes Insufficient Pods scheduling error. Resolve pods that cannot be scheduled because nodes have reached their pod capacity limit."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Insufficient Pods

`0/4 nodes are available: 4 Insufficient Pods`

This scheduling error occurs when all nodes in the cluster have reached their maximum pod capacity (default 110 pods per node).

### Common Causes

- Default pod limit (110 pods per node) has been reached
- Large number of daemonset pods on each node
- Node has been configured with a low `--max-pods` limit
- Too many small sidecar containers

### How to Fix

Check pods per node:
```bash
kubectl get pods --all-namespaces -o wide | grep <node> | wc -l
```

Increase max pods per node (kubelet config):
```yaml
kubeletConfig:
  maxPods: 250
```

### Examples

```bash
# Count pods per node
kubectl get pods --all-namespaces -o wide | awk '{print $8}' | sort | uniq -c | sort -rn
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})