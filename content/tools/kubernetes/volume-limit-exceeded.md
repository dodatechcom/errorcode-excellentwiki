---
title: "[Solution] Volume limit exceeded"
description: "Fix Kubernetes volume limit exceeded errors. Resolve pod scheduling failures when a node has reached its maximum volume attachment limit."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Volume Limit Exceeded

`0/4 nodes are available: 4 node(s) exceed max volume count`

This error occurs when the node has reached its maximum number of attached volumes. Each EC2 instance type, for example, has a limit on how many EBS volumes can be attached.

### Common Causes

- Node has reached the maximum attachable volumes
- Too many PVCs scheduled on a single node
- Some volumes remain attached but are not in use
- Instance type limits (e.g., t3.medium supports 3 EBS volumes)

### How to Fix

Check volume attachment limits for your instance type.

Use larger instance types that support more volumes.

Check which volumes are attached to the node:
```bash
kubectl get pods -o wide | grep <node> | wc -l
```

### Examples

```bash
# Check PVCs per node
kubectl get pods --all-namespaces -o wide | awk '{print $8}' | sort | uniq -c | sort -rn
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})