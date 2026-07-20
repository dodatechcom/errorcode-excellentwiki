---
title: "[Solution] API 422 Unprocessable Entity"
description: "Fix Kubernetes API 422 Unprocessable Entity error. Resolve resource creation failures due to validation errors."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## API 422 Unprocessable Entity

This HTTP status code occurs when the API server cannot process the request due to semantic validation errors in the resource definition.

### Common Causes

- Required fields are missing
- Invalid field values or types
- Schema validation failure
- Invalid YAML/JSON syntax
- Immutable field modification

### How to Fix

Check the exact validation error in the response:
```bash
kubectl apply -f resource.yaml --validate=true
```

Run dry-run validation:
```bash
kubectl apply -f resource.yaml --dry-run=server
```

### Examples

```bash
# Dry run validation
kubectl apply -f deployment.yaml --dry-run=server
# error: Deployment.apps "my-app" is invalid: spec.selector: Invalid value

# Fix: use matching selector and labels
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})