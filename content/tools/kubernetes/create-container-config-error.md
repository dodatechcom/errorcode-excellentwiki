---
title: "[Solution] CreateContainerConfigError"
description: "Fix Kubernetes CreateContainerConfigError. Resolve pod failures when container configuration references ConfigMaps or Secrets that are missing."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## CreateContainerConfigError

This error occurs when the kubelet cannot create the container because required configuration references do not exist or are invalid.

### Common Causes

- ConfigMap referenced in environment variables does not exist
- Secret referenced in environment variables does not exist
- ConfigMap key or Secret key does not exist
- ConfigMap or Secret is in a different namespace

### How to Fix

Check the exact error:
```bash
kubectl describe pod <pod-name> | grep -A5 "CreateContainerConfigError"
```

Verify ConfigMaps exist:
```bash
kubectl get configmap
kubectl get configmap <name> -o yaml
```

Verify Secrets exist:
```bash
kubectl get secret
kubectl get secret <name> -o yaml
```

### Examples

```bash
# Check for missing ConfigMap
kubectl describe pod my-app
#  Error: configmap "app-config" not found

# Fix
kubectl create configmap app-config --from-file=config.yaml
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})