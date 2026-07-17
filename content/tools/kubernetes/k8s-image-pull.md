---
title: "[Solution] Kubernetes ImagePullBackOff — failed to pull image"
description: "Fix Kubernetes ImagePullBackOff errors. Resolve image pull failures in pods."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["imagepullbackoff", "image", "pull", "registry", "kubernetes"]
weight: 5
---

ImagePullBackOff means Kubernetes cannot pull the container image for a pod. The kubelet repeatedly tries and backs off after each failure.

## Common Causes

- Image name or tag is incorrect
- Image is in a private registry without proper imagePullSecrets
- Registry is unreachable from the cluster
- Image was deleted or never pushed to the registry
- Image pull timeout due to large image size

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
  --docker-server=registry.example.com \
  --docker-username=user \
  --docker-password=pass
```

### Reference Secret in Deployment

```yaml
spec:
  containers:
    - name: app
      image: registry.example.com/my-app:latest
  imagePullSecrets:
    - name: regcred
```

### Check Node Connectivity to Registry

```bash
kubectl debug node/<node-name> -it --image=busybox
wget -qO- https://registry.example.com/v2/
```

## Examples

```bash
# Example 1: Image not found
kubectl describe pod my-pod
# Failed: ImagePullBackOff
# Fix: verify image name and tag

# Example 2: Private registry
kubectl describe pod my-pod
# Failed: unauthorized
# Fix: create imagePullSecrets
```

## Related Errors

- [Kubernetes CrashLoopBackOff]({{< relref "/tools/kubernetes/k8s-crashloop" >}}) — pod keeps crashing
- [Docker Image Not Found]({{< relref "/tools/docker/docker-image-not-found" >}}) — image not found in registry
