---
title: "[Solution] ImagePullBackOff"
description: "Fix Kubernetes ImagePullBackOff error. Resolve pod startup failures when the kubelet cannot pull the container image from the registry."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## ImagePullBackOff

This error occurs when the kubelet cannot pull the container image for a pod. Kubernetes retries the pull with exponential backoff (BackOff), and the pod enters ImagePullBackOff while waiting.

### Common Causes

- Image name or tag is incorrect
- Image does not exist in the registry
- Registry requires authentication but no credentials are configured
- Network issues preventing access to the registry
- Image pull rate limits exceeded (Docker Hub, etc.)

### How to Fix

Verify the image name:
```bash
kubectl describe pod <pod-name> | grep -A5 "Failed to pull image"
```

Check the exact error:
```bash
kubectl get events --field-selector involvedObject.name=<pod-name>
```

Set image pull secrets:
```bash
kubectl create secret docker-registry regcred \
  --docker-server=<registry> \
  --docker-username=<user> \
  --docker-password=<pass>
kubectl patch serviceaccount default -p '{"imagePullSecrets":[{"name":"regcred"}]}'
```

### Examples

```bash
# Check which image is failing
kubectl describe pod my-app-7d4f9c7b6-abcde | grep -i "Failed to pull image"
#  Failed to pull image "my-app:latest": rpc error: code = NotFound

# Fix typo in deployment
kubectl set image deployment/my-app my-app=my-app:v1.0.0
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})