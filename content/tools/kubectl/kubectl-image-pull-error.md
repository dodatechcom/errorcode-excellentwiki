---
title: "[Solution] Kubectl Image Pull Backoff Error — How to Fix"
description: "Fix kubectl ImagePullBackOff errors by verifying image names, checking registry credentials, configuring imagePullSecrets, debugging Docker daemon issues, and ensuring image exists."
tools: ["kubectl"]
error-types: ["image-pull-error"]
severities: ["error"]
weight: 5
comments: true
---

An `ImagePullBackOff` error occurs when Kubernetes cannot pull the container image specified in a Pod spec. The kubelet retries the pull with exponential backoff, and after each failure, the pod status shows `ImagePullBackOff` or `ErrImagePull`.

## What This Error Means

Kubernetes schedules pods on nodes, and the kubelet on each node is responsible for pulling the container image from the specified registry. If the image pull fails, the container cannot start. The kubelet retries with increasing delays (backoff), and the pod status reflects the failure.

ImagePullBackOff is a transient state — Kubernetes will keep retrying. However, if the underlying issue is not fixed, the pod will never start. Common causes include incorrect image names, authentication failures, network issues, and registry rate limits.

## Why It Happens

- The image name or tag is misspelled or does not exist
- The image registry requires authentication and no `imagePullSecrets` are configured
- The image pull secret is missing, expired, or references the wrong registry
- The node does not have network access to the container registry
- The image registry is rate-limiting anonymous pulls
- The image is stored in a private registry that requires specific credentials
- The image tag is wrong (e.g., `latest` when the tag is `v1.0`)
- The image has been deleted from the registry or moved to a different path

## Common Error Messages

```
Failed to pull image "my-app:latest": rpc error: code = NotFound
# or
Failed to pull image "myregistry.io/my-app": unauthorized: authentication required
# or
ImagePullBackOff: Back-off pulling image "myregistry.io/my-app"
# or
manifest for my-app:latest not found: manifest unknown
```

## How to Fix It

### 1. Check Pod Status and Events

```bash
# Describe the pod to see the exact error
kubectl describe pod my-pod

# Look for the Events section at the bottom
# The event will show the exact error message from the kubelet

# Check all pods with image pull issues
kubectl get pods --all-namespaces | grep -E "ImagePullBackOff|ErrImagePull"
```

### 2. Verify Image Name and Tag

```bash
# Check the image in the pod spec
kubectl get pod my-pod -o yaml | grep -A 5 "image:"

# Test pulling the image manually on a node
# SSH into a worker node and run:
docker pull myregistry.io/my-app:v1.0

# Or use crictl on containerd nodes
crictl pull myregistry.io/my-app:v1.0
```

### 3. Configure imagePullSecrets

```bash
# Create a Docker registry secret
kubectl create secret docker-registry regcred \
    --docker-server=https://index.docker.io/v1/ \
    --docker-username=myuser \
    --docker-password=mypassword \
    --docker-email=myemail@example.com

# Add the secret to the pod spec
kubectl patch serviceaccount default -p '{"imagePullSecrets": [{"name": "regcred"}]}'

# Or reference it in the pod spec directly:
# spec:
#   imagePullSecrets:
#   - name: regcred
```

### 4. Create a Proper Pull Secret for ECR

```bash
# For AWS ECR, get the authentication token
aws ecr get-login-password --region us-east-1 | \
    kubectl create secret docker-registry ecr-regcred \
    --docker-server=123456789012.dkr.ecr.us-east-1.amazonaws.com \
    --docker-username=AWS \
    --docker-password-stdin

# For GCP GCR, use a service account key
kubectl create secret docker-registry gcr-regcred \
    --docker-server=gcr.io \
    --docker-username=_json_key \
    --docker-password="$(cat service-account-key.json)"
```

### 5. Check Image Registry Network Access

```bash
# Test DNS resolution from a node
kubectl run dns-test --image=busybox -- nslookup docker.io
kubectl run dns-test --image=busybox -- nslookup myregistry.io

# Check if a proxy is needed
# In containerd config (/etc/containerd/config.toml) or Docker config:
# [Service]
# Environment="HTTP_PROXY=http://proxy.example.com:8080"
# Environment="HTTPS_PROXY=http://proxy.example.com:8080"
```

### 6. Use Image Pull Policy Effectively

```bash
# Set imagePullPolicy in your pod spec
# Always: always pull the image (default for :latest tags)
# IfNotPresent: only pull if not cached locally
# Never: never pull, use only local images

# Example deployment with explicit pull policy
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  template:
    spec:
      containers:
      - name: my-app
        image: myregistry.io/my-app:v1.0
        imagePullPolicy: IfNotPresent
EOF
```

### 7. Handle Registry Rate Limits

```bash
# Docker Hub imposes rate limits on anonymous pulls
# Use authenticated pulls to get higher limits

# Create a pull secret for Docker Hub
kubectl create secret docker-registry dockerhub \
    --docker-server=https://index.docker.io/v1/ \
    --docker-username=myuser \
    --docker-password=mytoken \  # Use an access token, not your password
    --docker-email=myemail@example.com

# Add to service account
kubectl patch serviceaccount default -p '{"imagePullSecrets": [{"name": "dockerhub"}]}'
```

### 8. Debug with a Simple Test Pod

```bash
# Create a simple pod to test image pulling
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: test-pull
spec:
  containers:
  - name: test
    image: nginx:latest
  restartPolicy: Never
EOF

# Watch events
kubectl get events --watch

# If nginx pulls fine, the issue is specific to your image
```

## Common Scenarios

### Private Image in Docker Hub Without Authentication

A deployment references `my-company/my-app:latest` from a private Docker Hub repository. The pod fails with `unauthorized: authentication required`. Create a Docker Hub pull secret with an access token and add `imagePullSecrets` to the pod spec.

### Image Tag Misspelled in Deployment

The deployment YAML specifies `my-app:1.0` but the actual image tag in the registry is `v1.0`. Kubernetes cannot find the manifest and returns `manifest unknown`. Correct the tag to `v1.0` and redeploy.

### Registry Certificate Expired

The container registry uses a self-signed certificate that has expired. The kubelet refuses to pull because it cannot verify the registry's TLS certificate. Update the registry certificate or configure the container runtime to use the correct CA certificate.

## Prevent It

- Use explicit image tags instead of `latest` to avoid ambiguity
- Configure `imagePullSecrets` in the default service account for private registries
- Pre-pull images on nodes for applications that must start quickly
- Use a local or cached registry mirror to reduce external dependencies
- Set up CI/CD to verify image existence before deployment
- Use immutable image tags (commit SHA-based) for traceability
- Configure container runtime with appropriate registry mirrors and proxies
- Implement image vulnerability scanning as part of the build pipeline

## Related Pages

- [Kubectl CrashLoopBackOff Error](/tools/kubectl/kubectl-crash-loop-error)
- [Kubectl Pod Logs Error](/tools/kubectl/kubectl-logs-error)
- [Kubectl Service Endpoint Not Found](/tools/kubectl/kubectl-service-error)
