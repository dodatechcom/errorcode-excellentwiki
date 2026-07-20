---
title: "[Solution] CustomResourceDefinition not found"
description: "Fix Kubernetes CRD not found error. Resolve issues when custom resources cannot be created because the CRD is missing."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## CRD Not Found

`the server could not find the requested resource (post <resource>.example.com)`

This error occurs when you try to create a custom resource but the CustomResourceDefinition (CRD) has not been installed.

### Common Causes

- CRD manifest has not been applied
- CRD was deleted
- CRD name or API group does not match the custom resource

### How to Fix

List installed CRDs:
```bash
kubectl get crd
```

Install the CRD:
```bash
kubectl apply -f crd.yaml
```

### Examples

```bash
# List custom resources
kubectl get crd | grep -i "example.com"

# Install CRD
kubectl apply -f https://example.com/crd.yaml
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})