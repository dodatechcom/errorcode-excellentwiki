---
title: "[Solution] API 401 Unauthorized"
description: "Fix Kubernetes API 401 Unauthorized error. Resolve authentication failures when accessing the Kubernetes API."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## API 401 Unauthorized

This HTTP status code occurs when the API server receives a request without valid authentication credentials.

### Common Causes

- Missing or expired bearer token
- Invalid or expired client certificate
- Service account token has expired or been deleted
- Token review API failure

### How to Fix

Check the current authentication method:
```bash
kubectl config view --minify
```

Generate a new service account token:
```bash
kubectl create token <service-account>
```

Update kubeconfig:
```bash
kubectl config set-credentials <user> --token=<new-token>
```

### Examples

```bash
# Create new service account token
kubectl create token my-sa --duration=24h

# Update kubeconfig with new token
kubectl config set-credentials cluster-admin --token=$(kubectl create token admin --duration=24h)
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})