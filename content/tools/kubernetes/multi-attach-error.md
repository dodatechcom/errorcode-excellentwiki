---
title: "[Solution] Multi-Attach volume error"
description: "Fix Kubernetes Multi-Attach volume error. Resolve volume attachment failures when a ReadWriteOnce volume is attached to multiple nodes."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Multi-Attach Volume Error

`Multi-Attach error for volume "<volume>"`
`Volume is already exclusively attached to one node and can't be attached to another`

This error occurs when two pods using the same ReadWriteOnce (RWO) persistent volume are scheduled on different nodes. RWO volumes can only be mounted on one node at a time.

### Common Causes

- Deployment with multiple replicas using an RWO volume
- Rolling update creates new pod on different node before old pod terminates
- StatefulSet with multiple replicas sharing the same volume

### How to Fix

Use ReadWriteMany (RWX) if the storage class supports it:
```yaml
accessModes:
  - ReadWriteMany
```

Use a StatefulSet with individual volumes per replica.

### Examples

```bash
# Check volume access mode
kubectl get pv <name> -o jsonpath='{.spec.accessModes}'

# Fix: schedule all replicas to same node
kubectl patch deployment my-app -p '{"spec":{"template":{"spec":{"nodeSelector":{"kubernetes.io/hostname":"node-1"}}}}}'
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})