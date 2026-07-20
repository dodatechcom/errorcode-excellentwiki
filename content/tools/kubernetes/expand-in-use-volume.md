---
title: "[Solution] ExpandInUseVolume"
description: "Fix Kubernetes ExpandInUseVolume error. Resolve issues when expanding a persistent volume that is in use by a pod."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## ExpandInUseVolume

This error occurs when attempting to expand a PersistentVolumeClaim that is in use by a running pod. Kubernetes supports online volume expansion but may encounter issues.

### Common Causes

- StorageClass does not support allowVolumeExpansion
- Filesystem resizing fails on the node
- Volume driver does not support online expansion

### How to Fix

Check if the StorageClass supports expansion:
```bash
kubectl get storageclass <name> -o yaml | grep allowVolumeExpansion
```

Edit PVC to request more storage:
```bash
kubectl edit pvc <name>
# Change spec.resources.requests.storage
```

### Examples

```bash
# Enable volume expansion on StorageClass
kubectl patch storageclass gp2 -p '{"allowVolumeExpansion":true}'

# Resize PVC
kubectl patch pvc my-claim -p '{"spec":{"resources":{"requests":{"storage":"20Gi"}}}}'
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})