---
title: "[Solution] Kubernetes ErrImagePull — Failed to pull image"
description: "Fix Kubernetes ErrImagePull error. Resolve image pull failures in pod specifications."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["errimagepull", "image-pull", "image", "pull", "kubernetes"]
weight: 5
---

# Kubernetes ErrImagePull — Failed to pull image

ErrImagePull indicates Kubernetes cannot pull the container image specified in the pod. This prevents the container from starting.

## Common Causes

- Image name or tag is incorrect
- Image is in a private registry without imagePullSecrets
- Image doesn't exist in the specified registry
- Network issues reaching the registry

## How to Fix

### Check Pod Events

```bash
kubectl describe pod <pod-name>
```

### Verify Image Exists

```bash
docker pull <image>:<tag>
```

### Create Image Pull Secret

```bash
kubectl create secret docker-registry regcred \
  --docker-server=<registry> \
  --docker-username=<user> \
  --docker-password=<password>
```

### Add ImagePullSecrets to Deployment

```yaml
spec:
  containers:
    - name: app
      image: private-registry.io/my-app:v1
  imagePullSecrets:
    - name: regcred
```

### Check ImagePullBackOff Events

```bash
kubectl get events --field-selector involvedObject.name=<pod-name>
```

## Examples

```bash
# Example 1: Image doesn't exist
kubectl describe pod my-app
# Warning  Failed  Error: ImagePullBackOff
# Fix: verify image name and tag

# Example 2: Private registry
kubectl describe pod my-app
# Warning  Failed  rpc error: code = Unknown desc = unauthorized
# Fix: create and attach imagePullSecrets

# Example 3: Network issue
kubectl describe pod my-app
# Warning  Failed  Error: manifest unknown
# Fix: check network connectivity to registry
```

## Related Errors

- [Pod Crash]({{< relref "/tools/kubernetes/pod-crash" >}}) — CrashLoopBackOff error
- [Pending Pod]({{< relref "/tools/kubernetes/pending-pod" >}}) — pod stuck in Pending state
