---
title: "[Solution] ImageInspectError"
description: "Fix Kubernetes ImageInspectError. Resolve pod failures when the container runtime cannot inspect a pulled image's metadata."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## ImageInspectError

This error occurs when the container runtime successfully pulls an image but cannot inspect or parse its metadata. The image manifest may be corrupted or incompatible.

### Common Causes

- Corrupted image manifest
- Image built for a different architecture
- Incompatible image format
- Registry returned a malformed image
- Disk I/O errors reading the image layers

### How to Fix

Try pulling the image manually on the node:
```bash
crictl pull <image>:<tag>
```

Re-pull the image:
```bash
kubectl delete pod <pod-name>
# New pod will be created by the controller
```

### Examples

```bash
# Check architecture mismatch
kubectl describe pod my-app | grep -i "ImageInspectError"
#  Error: image with reference my-app requires ARM64 but node is amd64

# Fix: use multi-arch image or specify correct architecture
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})