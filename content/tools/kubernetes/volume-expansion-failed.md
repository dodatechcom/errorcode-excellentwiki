---
title: "[Solution] Persistent volume expansion failed"
description: "Fix Kubernetes persistent volume expansion failures. Resolve issues when filesystem resizing fails after storage backend expansion."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Volume Expansion Failed

`FileSystemResizeFailed`

This error occurs when the filesystem resize fails after the volume has been expanded in the storage backend.

### Common Causes

- Filesystem type not supported for online resize
- Volume is not in use (filesystem resize requires a running pod)
- Node kernel missing filesystem resize support

### How to Fix

Check PVC status:
```bash
kubectl describe pvc <name> | grep -i "resize\|expansion"
```

Manually resize the filesystem:
```bash
# For ext4: resize2fs <device>
# For xfs: xfs_growfs <mount-point>
```

### Examples

```bash
# Check PVC events for resize failure
kubectl describe pvc my-claim | grep -A5 Events
#  FileSystemResizeFailed

# Check StorageClass
kubectl get sc gp2 -o yaml | grep allowVolumeExpansion
# false

# Enable expansion
kubectl patch sc gp2 -p '{"allowVolumeExpansion":true}'
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})