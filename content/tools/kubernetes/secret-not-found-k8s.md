---
title: "[Solution] Secret not found in Kubernetes"
description: "Fix Kubernetes 'secret not found' error. Resolve pod failures when a referenced Secret does not exist."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Secret Not Found

`secret "<name>" not found`

This error occurs when a pod references a Secret (via env, volume, or imagePullSecrets) that does not exist in the namespace.

### Common Causes

- Secret name is misspelled
- Secret has not been created yet
- Secret was deleted
- Secret is in a different namespace

### How to Fix

List secrets:
```bash
kubectl get secrets
```

Create the secret:
```bash
kubectl create secret generic <name> --from-literal=key=value
```

### Examples

```bash
# Create secret from literal
kubectl create secret generic app-secret --from-literal=api-key=abc123

# Create secret from file
kubectl create secret generic app-secret --from-file=./config.json
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})