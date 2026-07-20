---
title: "[Solution] Image garbage collection failed"
description: "Fix Kubernetes image garbage collection failures. Resolve issues when the kubelet cannot clean up unused images."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Image GC Failed

`Failed to garbage collect images: failed to remove image "<image>": rpc error: code = Unknown desc = ...`

This error occurs when the kubelet's image garbage collector cannot remove unused container images to free disk space.

### Common Causes

- Image is in use by a running container
- Disk I/O errors preventing image removal
- containerd/CRI-O not responding
- Filesystem corruption on the image storage
- Permission issues on image storage directory

### How to Fix

Manually prune images:
```bash
sudo crictl rmi --prune
sudo docker image prune -a -f
```

Check image storage disk usage:
```bash
sudo du -sh /var/lib/containerd/
sudo du -sh /var/lib/docker/
```

### Examples

```bash
# Manual image cleanup
ssh <node> sudo crictl rmi --prune
ssh <node> sudo docker image prune -a -f
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})