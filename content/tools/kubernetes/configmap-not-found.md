---
title: "[Solution] ConfigMap not found"
description: "Fix Kubernetes 'configmap not found' error. Resolve pod failures when a referenced ConfigMap does not exist."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## ConfigMap Not Found

`configmap "<name>" not found`

This error occurs when a pod references a ConfigMap that does not exist in the namespace.

### Common Causes

- ConfigMap name is misspelled
- ConfigMap has not been created
- ConfigMap was deleted
- ConfigMap is in a different namespace

### How to Fix

List ConfigMaps:
```bash
kubectl get configmaps
```

Create the ConfigMap:
```bash
kubectl create configmap <name> --from-file=config.yaml
```

### Examples

```bash
# Create ConfigMap from file
kubectl create configmap app-config --from-file=./app.properties

# Create ConfigMap from literal
kubectl create configmap app-config --from-literal=LOG_LEVEL=debug
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})