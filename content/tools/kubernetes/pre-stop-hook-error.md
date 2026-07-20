---
title: "[Solution] PreStopHookError"
description: "Fix Kubernetes PreStopHookError. Resolve pod termination failures when the preStop lifecycle hook fails during graceful shutdown."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## PreStopHookError

This error occurs when the preStop lifecycle hook fails during pod termination. Kubernetes still proceeds with termination but logs the error.

### Common Causes

- preStop command or script exits with non-zero
- HTTP handler returns non-2xx status
- Handler takes longer than the terminationGracePeriodSeconds
- Handler tries to access resources already being terminated

### How to Fix

Check the pod events:
```bash
kubectl describe pod <pod-name> | grep -A10 "preStop"
```

Increase terminationGracePeriodSeconds:
```yaml
terminationGracePeriodSeconds: 60
```

### Examples

```bash
# Check for preStop errors
kubectl describe pod my-app | grep -i -A3 "Unhealthy"

# Fix: increase grace period
kubectl patch deployment my-app -p '{"spec":{"template":{"spec":{"terminationGracePeriodSeconds":60}}}}'
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})