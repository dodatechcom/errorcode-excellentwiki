---
title: "[Solution] ErrImagePull"
description: "Fix Kubernetes ErrImagePull error. Resolve pod failures when the kubelet encounters an error pulling the container image."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## ErrImagePull

This error occurs when the kubelet encounters an error while trying to pull the container image. Unlike ImagePullBackOff, this is a non-retriable error that requires immediate intervention.

### Common Causes

- Image repository does not exist
- Image tag is invalid
- Registry returned an error (permission denied, not found)
- Network timeout or DNS resolution failure
- Invalid image reference format

### How to Fix

Check the exact error message:
```bash
kubectl describe pod <pod-name> | grep -i "Error"
```

Use a fully qualified image reference:
```yaml
image: docker.io/library/nginx:1.25
```

Pull the image manually on a node:
```bash
crictl pull nginx:1.25
```

### Examples

```bash
# Common error: image doesn't exist
kubectl describe pod test-pod
#  Failed to pull image "nonexistent:v999": rpc error: code = NotFound

# Fix by correcting the image name
kubectl set image deployment/my-app my-app=nginx:1.25
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})