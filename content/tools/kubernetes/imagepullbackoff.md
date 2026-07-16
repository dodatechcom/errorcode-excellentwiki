---
title: "[Solution] Kubernetes ImagePullBackOff — Failed to pull image"
description: "Fix Kubernetes ImagePullBackOff errors. Resolve issues pulling container images in Kubernetes clusters."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["imagepullbackoff", "pull-image", "registry", "image"]
weight: 5
---

# Kubernetes ImagePullBackOff — Failed to pull image

ImagePullBackOff means Kubernetes cannot pull the container image for a pod. The kubelet repeatedly tries and backs off, unable to fetch the image from the specified registry.

## Common Causes

- Image name or tag is incorrect
- Image is in a private registry and no imagePullSecret is configured
- Registry requires authentication and credentials are missing
- Image does not exist in the specified registry

## How to Fix

### Check Pod Events

```bash
kubectl describe pod <pod-name>
```

### Verify Image Name and Tag

```bash
kubectl get pod <pod-name> -o jsonpath='{.spec.containers[*].image}'
```

### Create an Image Pull Secret

```bash
kubectl create secret docker-registry regcred \
  --docker-server=<registry-url> \
  --docker-username=<username> \
  --docker-password=<password>
```

### Reference the Secret in Deployment

```yaml
spec:
  containers:
    - name: app
      image: private-registry.example.com/my-app:v1
  imagePullSecrets:
    - name: regcred
```

### Test Registry Access

```bash
docker login <registry-url>
docker pull <registry-url>/<image-name>:<tag>
```

## Examples

```bash
# Example 1: Wrong image tag
kubectl describe pod my-app
# Warning: Failed to pull image "my-app:v99": image not found
# Fix: correct the tag in deployment spec

# Example 2: Private registry without credentials
kubectl describe pod my-app
# Warning: You may not have access to the repository
# Fix: create imagePullSecret and add to pod spec
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crashloopbackoff" >}}) — pod crashing after successful image pull
- [Image Not Found]({{< relref "/tools/docker/image-not-found" >}}) — Docker image not found locally
