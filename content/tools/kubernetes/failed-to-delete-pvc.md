---
title: "[Solution] Failed to delete PVC"
description: "Fix Kubernetes failed PVC deletion errors. Resolve persistent volume claim stuck in Terminating state."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Failed to Delete PVC

This error occurs when a PersistentVolumeClaim cannot be deleted because it is still in use or has protection finalizers.

### Common Causes

- PVC protection finalizer not removed
- Pod still referencing the PVC
- Volume snapshot exists for the PVC
- Storage system is unreachable
- PV retention policy preventing deletion

### How to Fix

Find pods using the PVC:
```bash
kubectl get pods --all-namespaces -o json | jq '.items[] | select(.spec.volumes[]?.persistentVolumeClaim.claimName=="<pvc-name>") | .metadata.namespace + "/" + .metadata.name'
```

Remove finalizers:
```bash
kubectl patch pvc <name> -p '{"metadata":{"finalizers":[]}}' --type=merge
```

Delete the protecting pods first.

### Examples

```bash
# Force remove a stuck PVC
kubectl patch pvc my-claim -p '{"metadata":{"finalizers":[]}}' --type=merge
kubectl delete pvc my-claim --grace-period=0 --force
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})