---
title: "[Solution] Pod failed admission"
description: "Fix Kubernetes pod failed admission errors. Resolve pods that are rejected during admission control before scheduling."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Pod Failed Admission

`pod "<name>" is forbidden: <reason>`

This error occurs when a pod is rejected by Kubernetes admission controllers before it reaches the scheduler.

### Common Causes

- PodSecurityPolicy or Pod Security Admission rejection
- ResourceQuota exceeded in the namespace
- LimitRange validation failure
- Admission webhook rejection
- ServiceAccount does not exist
- ImagePullSecret missing

### How to Fix

Check the full error message for the specific reason:
```bash
kubectl apply -f pod.yaml 2>&1
```

Fix the specific issue mentioned in the error (resource limits, missing SA, security context, etc).

### Examples

```bash
# Apply with verbose output
kubectl apply -f pod.yaml 2>&1
# Error: pods "my-pod" is forbidden: exceeded quota: compute-quota
# Fix: reduce resource requests or increase quota
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})