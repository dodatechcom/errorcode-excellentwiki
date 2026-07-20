---
title: "[Solution] Unknown field in Kubernetes manifest"
description: "Fix Kubernetes 'unknown field' error. Resolve resource creation failures when the manifest contains unrecognized fields."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Unknown Field

`error: validation failure: unknown field "<field>" in <resource>`

This error occurs when a Kubernetes manifest contains a field that does not exist in the API schema.

### Common Causes

- Typo in a field name
- Field exists in a different API version
- Using a deprecated field that was removed
- API version mismatch between cluster and manifest

### How to Fix

Check the correct API version:
```bash
kubectl explain pod
```

Use the correct API version:
```yaml
apiVersion: apps/v1  # instead of extensions/v1beta1
```

### Examples

```bash
# Check supported fields
kubectl explain deployment.spec
# Find the correct field name

# Common fix: update API version
# Old: apiVersion: extensions/v1beta1
# New: apiVersion: networking.k8s.io/v1
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})