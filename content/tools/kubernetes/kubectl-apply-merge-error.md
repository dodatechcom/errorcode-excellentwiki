---
title: "[Solution] kubectl apply merge error"
description: "Fix kubectl apply merge conflicts. Resolve errors when applying Kubernetes manifests with conflicting changes."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## kubectl Apply Merge Error

`error: failed to apply patch: <resource> "<name>" is invalid: <field>: Invalid value: "<value>": <conflict>`

This error occurs when kubectl apply cannot merge the changes from the manifest with the existing resource.

### Common Causes

- Conflicting field values
- Immutable field modification (selector, nodePort, etc.)
- Server-side apply conflict
- Wrong merge strategy
- Resource drift between apply calls

### How to Fix

Use server-side apply:
```bash
kubectl apply --server-side --force-conflicts -f manifest.yaml
```

Re-read and re-apply the manifest:
```bash
kubectl get <resource> <name> -o yaml > current.yaml
# Merge changes manually
kubectl apply -f current.yaml
```

### Examples

```bash
# Force server-side apply
kubectl apply --server-side --force-conflicts -f deployment.yaml

# Read current state and compare
kubectl diff -f deployment.yaml
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})