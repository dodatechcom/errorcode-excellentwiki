---
title: "[Solution] ImagePullSecret missing"
description: "Fix Kubernetes ImagePullSecret missing errors. Resolve pod creation failures when private registry credentials are required but not provided."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## ImagePullSecret Missing

`Failed to pull image "<image>": rpc error: code = Unknown desc = Error response from daemon: pull access denied for <repository>`

This error occurs when a pod references an image from a private registry but does not provide authentication credentials via an imagePullSecret.

### Common Causes

- Image is in a private registry (ECR, GCR, private Docker Hub, etc.)
- No imagePullSecret is configured in the pod spec or service account
- The imagePullSecret exists but has incorrect credentials
- The service account does not have the imagePullSecret attached

### How to Fix

Create an imagePullSecret:
```bash
kubectl create secret docker-registry regcred   --docker-server=<registry>   --docker-username=<user>   --docker-password=<token>
```

Add to pod spec:
```yaml
spec:
  imagePullSecrets:
  - name: regcred
```

Or add to the default service account:
```bash
kubectl patch serviceaccount default -p '{"imagePullSecrets":[{"name":"regcred"}]}'
```

### Examples

```bash
# Create ECR pull secret
kubectl create secret docker-registry ecr-cred   --docker-server=<account>.dkr.ecr.us-east-1.amazonaws.com   --docker-username=AWS   --docker-password=$(aws ecr get-login-password)
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})