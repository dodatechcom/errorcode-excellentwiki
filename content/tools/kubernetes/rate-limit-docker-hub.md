---
title: "[Solution] Docker Hub rate limited in Kubernetes"
description: "Fix Kubernetes Docker Hub rate limiting errors. Resolve image pull failures when Docker Hub rate limits are exceeded."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Docker Hub Rate Limited

`toomanyrequests: You have reached your pull rate limit`

This error occurs when you exceed Docker Hub's anonymous (100 pulls/6h) or authenticated (200 pulls/6h) rate limits.

### Common Causes

- Cluster nodes pulling images without authentication
- High number of pod replicas restarting or rolling out
- Many nodes pulling the same image simultaneously

### How to Fix

Add Docker Hub credentials:
```bash
kubectl create secret docker-registry dockerhub \
  --docker-username=<user> \
  --docker-password=<token>
kubectl patch serviceaccount default -p '{"imagePullSecrets":[{"name":"dockerhub"}]}'
```

Use imagePullPolicy: IfNotPresent to cache images:
```yaml
imagePullPolicy: IfNotPresent
```

### Examples

```bash
# Create image pull secret
kubectl create secret docker-registry regcred \
  --docker-server=https://index.docker.io/v1/ \
  --docker-username=myuser \
  --docker-password=$(cat ~/dockerhub-token)

# Add to default service account
kubectl patch serviceaccount default -p '{"imagePullSecrets":[{"name":"regcred"}]}'
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})