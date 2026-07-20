---
title: "[Solution] Pod stuck in Terminating"
description: "Fix Kubernetes pod stuck in Terminating state. Resolve pods that cannot be deleted."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Pod Stuck in Terminating

A pod stuck in Terminating means the kubelet has received the deletion request but cannot stop the container(s).

### Common Causes

- Container has a process that ignores SIGTERM and SIGKILL
- PreStop hook is hanging or running indefinitely
- terminationGracePeriodSeconds is very high
- Node is unreachable (NotReady)
- Volume mount issues preventing umount

### How to Fix

Force delete a pod:
```bash
kubectl delete pod <name> --grace-period=0 --force
```

Remove finalizers:
```bash
kubectl patch pod <name> -p '{"metadata":{"finalizers":[]}}' --type=merge
```

### Examples

```bash
# Force delete terminating pod
kubectl delete pod my-app-xxx --grace-period=0 --force

# Remove finalizers from stuck pod
kubectl patch pod my-app-xxx -p '{"metadata":{"finalizers":[]}}' --type=merge
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})