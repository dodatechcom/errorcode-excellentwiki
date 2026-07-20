---
title: "[Solution] Invalid annotation in Kubernetes manifest"
description: "Fix Kubernetes invalid annotation errors. Resolve resource creation failures when annotations have invalid format."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Invalid Annotation

`Invalid annotation: <key>: <value>`

This error occurs when a Kubernetes resource has annotations with invalid keys or values.

### Common Causes

- Annotation key does not follow the prefix/name format
- Annotation value is too long (>256KB)
- Annotation key has invalid characters
- Reserved annotation prefix used without permission
- Annotation key is empty or missing

### How to Fix

Check annotation format:
```yaml
metadata:
  annotations:
    # Valid format: <prefix>/<name>
    nginx.ingress.kubernetes.io/rewrite-target: /
    # Built-in annotations don't need prefix
    kubectl.kubernetes.io/last-applied-configuration: "..."
```

Remove or correct the annotation:
```bash
kubectl annotate <resource> <name> <key>-  # remove annotation
kubectl annotate <resource> <name> <key>=<value> --overwrite
```

### Examples

```bash
# Remove an invalid annotation
kubectl annotate deployment my-app my-invalid-annotation-

# Add corrected annotation
kubectl annotate deployment my-app nginx.ingress.kubernetes.io/rewrite-target=/
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})