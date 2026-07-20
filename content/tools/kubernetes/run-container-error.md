---
title: "[Solution] RunContainerError"
description: "Fix Kubernetes RunContainerError. Resolve pod failures when the container runtime cannot start the container after the image is pulled."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## RunContainerError

This error occurs when the container runtime (containerd, CRI-O) cannot start the container after the image has been successfully pulled. The container fails before the application process begins.

### Common Causes

- Container command or entrypoint not found or invalid
- Working directory does not exist in the container
- Volume mount points to a non-existent or invalid path
- Container runtime configuration issue
- Invalid container permissions or security context

### How to Fix

Check the error description:
```bash
kubectl describe pod <pod-name> | grep -A10 "RunContainerError"
```

Verify the container command exists in the image:
```bash
kubectl run test --image=<image> -- ls /app/start.sh
```

Check volume mounts and paths:
```bash
kubectl describe pod <pod-name> | grep -A5 Mounts
```

### Examples

```bash
# Check exact error
kubectl describe pod my-app | grep -A5 "RunContainerError"
#  Error: container command '/app/start.sh' not found

# Fix by correcting command in deployment
kubectl edit deployment my-app
# Change command or entrypoint to match the image
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})