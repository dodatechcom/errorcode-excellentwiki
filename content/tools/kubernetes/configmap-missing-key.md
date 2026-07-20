---
title: "[Solution] ConfigMap key not found"
description: "Fix Kubernetes ConfigMap key not found errors. Resolve pod failures when a referenced ConfigMap key does not exist."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## ConfigMap Key Not Found

This error occurs when a pod references a specific key from a ConfigMap that does not exist.

### Common Causes

- ConfigMap key name is misspelled
- ConfigMap key was renamed or removed
- Key name is case-sensitive
- Wrong ConfigMap referenced
- Key has special characters that need escaping

### How to Fix

Check the ConfigMap contents:
```bash
kubectl get configmap <name> -o yaml
# Check the data section for available keys
```

List keys in a ConfigMap:
```bash
kubectl get configmap <name> -o jsonpath='{.data}'
```

Update the deployment to use the correct key name.

### Examples

```bash
# View ConfigMap keys
kubectl get configmap app-config -o yaml
# data:
#   DATABASE_URL: "postgres://..."
#   LOG_LEVEL: "debug"

# Correct the env var reference in deployment
kubectl set env deployment/my-app --from=configmap/app-config
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})