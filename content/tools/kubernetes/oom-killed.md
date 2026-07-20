---
title: "[Solution] OOMKilled (Exit Code 137)"
description: "Fix Kubernetes OOMKilled error. Resolve pods terminated for exceeding memory limits with exit code 137 (SIGKILL)."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## OOMKilled (Exit Code 137)

This error occurs when a container exceeds its memory limit and is killed by the Out-Of-Memory (OOM) killer. The exit code 137 (128 + 9 = SIGKILL) indicates the process was forcefully terminated.

### Common Causes

- Memory limit is set too low for the application
- Memory leak in the application
- Traffic spike causing higher memory usage
- Pod running on a node with insufficient memory
- No memory limits set (can be killed under node pressure)

### How to Fix

Check the termination reason:
```bash
kubectl describe pod <pod-name> | grep -i "OOM"
```

Check memory usage:
```bash
kubectl top pod <pod-name>
```

Increase memory limit:
```bash
kubectl set resources deployment/my-app --limits=memory=1Gi
```

### Examples

```bash
# Check if pod was OOMKilled
kubectl get pod my-app-7d4f9c7b6-abcde -o jsonpath='{.status.containerStatuses[0].state.terminated.reason}'
# OOMKilled

# Increase memory
kubectl set resources deployment/my-app --requests=memory=256Mi --limits=memory=512Mi
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})