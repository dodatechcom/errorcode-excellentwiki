---
title: "[Solution] StatefulSet pod ordering error"
description: "Fix Kubernetes StatefulSet pod ordering errors. Resolve StatefulSet startup and shutdown ordering issues."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## StatefulSet Pod Ordering Error

`StatefulSet <name> is waiting for pod <pod-name> to be Running and Ready`

This occurs when a StatefulSet cannot proceed with pod creation or deletion due to its ordinal ordering guarantees.

### Common Causes

- Pod with lower ordinal is not Ready
- Pod deletion is blocked by PDB
- Pod is stuck in Pending or ContainerCreating
- Volume provisioning is slow for the next pod
- Partitioned rollout with updateStrategy.rollingUpdate.partition

### How to Fix

Check pod status:
```bash
kubectl get pods -l app=<name>
```

Check the StatefulSet status:
```bash
kubectl describe statefulset <name>
```

Force delete a stuck pod:
```bash
kubectl delete pod <name> --grace-period=0 --force
```

### Examples

```bash
# Check StatefulSet status
kubectl describe statefulset my-sts
#  Waiting for pods 1 to be ready

# Check pod status
kubectl get pods -l app=my-sts
# my-sts-0   1/1   Running
# my-sts-1   0/1   Pending
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})