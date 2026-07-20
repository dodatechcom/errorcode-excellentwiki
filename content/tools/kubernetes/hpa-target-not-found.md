---
title: "[Solution] HPA target not found"
description: "Fix Kubernetes HPA target not found error. Resolve HorizontalPodAutoscaler failures when the target resource does not exist."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## HPA Target Not Found

`error: target <resource>/<name> not found`

This error occurs when the HorizontalPodAutoscaler references a deployment, statefulset, or custom resource that does not exist.

### Common Causes

- HPA target name is misspelled
- Target deployment has not been created
- Target deployment was deleted
- HPA is looking in the wrong namespace

### How to Fix

Check the HPA target:
```bash
kubectl describe hpa <name>
```

List available deployments:
```bash
kubectl get deployments
```

### Examples

```bash
# Check HPA target
kubectl get hpa my-hpa -o jsonpath='{.spec.scaleTargetRef}'
# {"apiVersion":"apps/v1","kind":"Deployment","name":"my-app"}

# Verify target exists
kubectl get deployment my-app
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})