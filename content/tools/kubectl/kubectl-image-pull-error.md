---
title: "[Solution] Kubectl ImagePullBackOff — Fix Image Pull Errors"
description: "Fix kubectl ImagePullBackOff errors. Resolve image name typos, registry authentication, and image tag issues with step-by-step fixes."
---

## What This Error Means

ImagePullBackOff means Kubernetes cannot pull the container image specified in the pod definition. The kubelet repeatedly tries to pull the image and backs off after each failure.

A typical output:

```
NAME                    READY   STATUS             RESTARTS      AGE
web-app-7f8b6c5d4-abc   0/1     ImagePullBackOff   3 (2m ago)    4m
```

Or the earlier state:

```
web-app-7f8b6c5d4-abc   0/1     ErrImagePull        3 (2m ago)    4m
```

## Why It Happens

ImagePullBackOff is caused by:

- **Incorrect image name or tag**: Typo in the image path or the tag does not exist.
- **Private registry credentials**: The image is in a private registry without proper pull secrets.
- **Network issues**: The node cannot reach the container registry.
- **Image deleted**: The image was removed from the registry.
- **Rate limiting**: Docker Hub or other registries rate-limit anonymous pulls.
- **Node disk pressure**: The node's disk is full and cannot store the image.

## How to Fix It

**Step 1: Check the exact error**

```bash
kubectl describe pod web-app-7f8b6c5d4-abc
```

Look for events:

```
Events:
  Warning  Failed  Failed to pull image "myregistry.com/app:v2": rpc error:
  code = Unknown desc = failed to pull and unpack image: not found
```

**Step 2: Verify the image exists**

```bash
# Test pulling manually on the node
docker pull myregistry.com/app:v2

# Check if tag exists
curl -s "https://registry.hub.docker.com/v2/myregistry/app/tags/list"
```

**Step 3: Create a pull secret for private registries**

```bash
kubectl create secret docker-registry regcred \
  --docker-server=myregistry.com \
  --docker-username=myuser \
  --docker-password=mypassword \
  --docker-email=myemail@example.com
```

Reference the secret in the pod spec:

```yaml
spec:
  containers:
    - name: web-app
      image: myregistry.com/app:v2
  imagePullSecrets:
    - name: regcred
```

**Step 4: Check for Docker Hub rate limiting**

Use authenticated pulls or mirror images to a private registry:

```bash
docker login
docker tag myregistry/app:v2 my-registry.example.com/app:v2
docker push my-registry.example.com/app:v2
```

**Step 5: Verify node disk space**

```bash
kubectl describe node node1 | grep -A 3 "Conditions"
df -h
```

## Common Mistakes

- **Forgetting image tags**: Without a tag, Kubernetes defaults to `latest` which may not exist.
- **Not using imagePullSecrets for private registries**: Always configure pull secrets for non-public images.
- **Assuming local images work**: Images must be in a registry accessible from all nodes, not just your machine.
- **Ignoring rate limits on Docker Hub**: Mirror images to your own registry for production workloads.

## Related Pages

- [Kubectl Pod CrashLoopBackOff](/tools/kubectl/kubectl-pod-crashloopbackoff/) — Pod crash restart issues
- [Kubectl Pod Pending](/tools/kubectl/kubectl-pod-pending/) — Pod scheduling problems
- [Kubectl Permission Error](/tools/kubectl/kubectl-permission-error/) — RBAC authorization errors
