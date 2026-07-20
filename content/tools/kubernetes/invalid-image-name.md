---
title: "[Solution] InvalidImageName"
description: "Fix Kubernetes InvalidImageName error. Resolve pod failures when the container image name format is invalid."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## InvalidImageName

This error occurs when the container image name or tag does not follow valid format rules. Kubernetes cannot parse the image reference.

### Common Causes

- Whitespace in the image name or tag
- Missing repository name or tag
- Invalid characters in the image reference
- Missing colon between image and tag
- Trailing slash or special characters

### How to Fix

Check the image in the pod spec:
```bash
kubectl get pod <pod-name> -o jsonpath='{.spec.containers[0].image}'
```

Verify the image format:
```yaml
# Valid formats
image: nginx
image: nginx:1.25
image: docker.io/library/nginx:1.25
image: myregistry.example.com/app:v1.0
```

### Examples

```bash
# Invalid formats
# image: nginx:   (empty tag)
# image: my-app:v1.0-beta 1  (space in tag)

# Fix by correcting the image reference
kubectl set image deployment/my-app my-app=nginx:1.25
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})