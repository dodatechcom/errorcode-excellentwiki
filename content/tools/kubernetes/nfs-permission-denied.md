---
title: "[Solution] NFS volume permission denied in Kubernetes"
description: "Fix Kubernetes NFS volume permission denied errors. Resolve access issues when pods cannot read or write to NFS mounts."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## NFS Permission Denied

`Permission denied` when accessing files on a mounted NFS volume

This error occurs when the container user does not have the correct permissions on the NFS exported directory.

### Common Causes

- Container runs as a non-root user but NFS files are owned by root
- NFS export has root_squash enabled (maps root to nobody)
- NFS directory permissions do not allow the container UID
- Pod securityContext runAsUser does not match NFS file ownership
- NFS export options restrict access
- SELinux blocking NFS access

### How to Fix

Set the pod's securityContext to match the NFS file ownership:
```yaml
securityContext:
  runAsUser: 1000
  runAsGroup: 1000
  fsGroup: 1000
```

Configure NFS export with no_root_squash (if using root):
```bash
# /etc/exports
/path/to/export *(rw,no_root_squash,no_subtree_check)
```

Check NFS mount permissions:
```bash
kubectl exec <pod> -- ls -la /mount/path
kubectl exec <pod> -- id
```

### Examples

```bash
# Check current user in container
kubectl exec my-pod -- id
# uid=1000(appuser) gid=1000(appuser)

# Fix file ownership on NFS server
sudo chown -R 1000:1000 /path/to/export
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})