---
title: "[Solution] Kubernetes ImagePullBackOff — image pull failed"
description: "Fix Kubernetes ImagePullBackOff. Resolve container image pull failures and registry issues."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["kubernetes", "imagepullbackoff", "image", "pull", "registry", "container"]
weight: 5
---

ImagePullBackOff means Kubernetes cannot pull the container image for a pod. The kubelet retries pulling the image with exponential backoff but keeps failing.

## What This Error Means

The kubelet on the target node attempts to pull the specified container image from a registry but fails. Common failure reasons include incorrect image name/tag, missing registry credentials, network connectivity issues, or the image not existing in the registry. The pod will remain in `ImagePullBackOff` until the image is successfully pulled or the pod spec is corrected.

## Common Causes

- Incorrect image name or tag specified in the pod spec
- Image does not exist in the specified registry
- Missing or invalid image pull secret for private registries
- Network connectivity issues between node and registry
- Registry rate limiting (Docker Hub, ghcr.io)
- ImagePullPolicy set to Always with an invalid image reference

## How to Fix

### Check Image Pull Events

```bash
kubectl describe pod <pod-name> | grep -A 5 Events
```

### Verify Image Exists

```bash
docker pull <image>:<tag>
```

### Create Image Pull Secret

```bash
kubectl create secret docker-registry regcred \
  --docker-server=<registry-server> \
  --docker-username=<username> \
  --docker-password=<password>
```

### Reference Secret in Pod Spec

```yaml
spec:
  containers:
    - name: app
      image: private-registry.com/myapp:v1
  imagePullSecrets:
    - name: regcred
```

### Check Image Pull Policy

```yaml
containers:
  - name: app
    image: myregistry.com/app:v1
    imagePullPolicy: IfNotPresent
```

### Test Registry Connectivity from Node

```bash
curl -v https://registry-1.docker.io/v2/
```

## Related Errors

- [Kubernetes CrashLoopBackOff]({{< relref "/tools/kubernetes/k8s-crashloop-v2" >}}) — pod crash loop
- [Kubernetes Secret Error]({{< relref "/tools/kubernetes/k8s-secret-error-v2" >}}) — secret decode error
- [Kubernetes RBAC Error]({{< relref "/tools/kubernetes/k8s-rbac-error-v2" >}}) — RBAC forbidden
