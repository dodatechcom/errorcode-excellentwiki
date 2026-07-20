---
title: "[Solution] Kustomize build error"
description: "Fix Kustomize build errors in Kubernetes. Resolve issues when building Kubernetes manifests with Kustomize."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Kustomize Build Error

`Error: accumulating resources: accumulation err: ...`

This error occurs when `kubectl kustomize` or `kustomize build` fails to generate Kubernetes manifests.

### Common Causes

- Resource file not found in the specified path
- Invalid YAML in base or overlay files
- Patch does not match the target resource
- Name prefix/suffix conflicts
- Duplicate resource names after transformation
- CRD not found when using vars or replacements

### How to Fix

Check the kustomization.yaml syntax:
```bash
kustomize build <dir> 2>&1
```

Validate individual resource files:
```bash
kubectl apply -f <file> --dry-run=server
```

Use `--load-restrictor` for loading resources from outside the root:
```bash
kustomize build --load-restrictor LoadRestrictionsNone <dir>
```

### Examples

```bash
# Build and check for errors
kustomize build overlays/production/ 2>&1

# Validate output
kustomize build overlays/production/ | kubectl apply --dry-run=server -f -
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})