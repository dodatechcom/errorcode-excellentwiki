---
title: "[Solution] k8s: ImagePullBackOff — Failed to Pull Image"
description: "Fix Kubernetes ImagePullBackOff errors. Resolve image pull failures caused by wrong image names, missing pull secrets, and registry issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# k8s: ImagePullBackOff — Failed to Pull Image

ImagePullBackOff means Kubernetes repeatedly failed to pull the container image for a pod. The status shows:

> "ImagePullBackOff" or "ErrImagePull" in `kubectl get pods`

Events show:

> "Failed to pull image: rpc error: code = NotFound desc = failed to pull and unpack image"

## What This Error Means

Kubernetes kubelet on each node pulls container images before starting containers. When the image pull fails — due to wrong image name, missing credentials, or network issues — the kubelet retries with exponential backoff, entering `ImagePullBackOff` state.

## Common Causes

- Incorrect image name or tag (typo, case sensitivity)
- Image does not exist in the specified registry
- Private registry requires pull secret (not configured)
- Pull secret is invalid or expired
- Network connectivity issue between node and registry
- Image removed from registry
- Node has no disk space to pull the image

## How to Fix

### Check Pod Events

```bash
kubectl describe pod <pod-name> | grep -A 10 "Events:"
```

### Verify Image Exists

```bash
# Test image pull manually
docker pull <image>:<tag>

# Check registry for image
curl -s "https://registry.hub.docker.com/v2/repositories/library/<image>/tags" | jq
```

### Create or Fix Pull Secret

```bash
# Create a pull secret
kubectl create secret docker-registry my-registry-secret \
  --docker-server=registry.example.com \
  --docker-username=user \
  --docker-password=pass \
  --docker-email=user@example.com

# Use it in the pod spec
```

```yaml
spec:
  containers:
    - name: app
      image: registry.example.com/myimage:latest
  imagePullSecrets:
    - name: my-registry-secret
```

### Check Pull Secret Status

```bash
kubectl get secret <secret-name> -o yaml
kubectl describe secret <secret-name>
```

### Use Public Images or Correct Registry

```bash
# Wrong
image: myregistry.io/nginx:latest

# Correct
image: docker.io/library/nginx:latest
```

### Check Node Disk Space

```bash
kubectl describe node <node-name> | grep -A 5 "Conditions"
ssh <node> "df -h /var/lib/containerd"
```

## Related Errors

- [Docker Image Not Found]({{< relref "/os/linux/linux-docker-image-not-found" >}}) — Image pull failures at Docker level
- [Docker Pull Timeout]({{< relref "/os/linux/linux-docker-pull-timeout" >}}) — Registry connectivity issues
- [k8s Pod Pending]({{< relref "/os/linux/linux-k8s-pending" >}}) — Pod scheduling failures
