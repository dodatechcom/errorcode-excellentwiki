---
title: "[Solution] BackOff (restarting failed container)"
description: "Fix Kubernetes BackOff restart backoff delay. Resolve pods that fail to start and are delayed by exponential backoff between restart attempts."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## BackOff

This status means Kubernetes is using exponential backoff between container restart attempts. The delay increases with each retry (10s, 20s, 40s, 80s, up to 5 minutes).

### Common Causes

- Application crashes immediately after start
- Configuration errors preventing application startup
- Missing dependencies at startup
- Resource limits causing immediate OOM

### How to Fix

Check the crash reason:
```bash
kubectl logs <pod-name> --previous
```

Check for configuration issues:
```bash
kubectl describe pod <pod-name>
```

Reset the backoff by deleting the pod:
```bash
kubectl delete pod <pod-name>
# The controller recreates it
```

### Examples

```bash
# View crash logs
kubectl logs my-app-7d4f9c7b6-abcde --previous --tail=50

# Delete pod to reset backoff (deployment recreates)
kubectl delete pod my-app-7d4f9c7b6-abcde
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})