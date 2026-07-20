---
title: "[Solution] CrashLoopBackOff"
description: "Fix Kubernetes CrashLoopBackOff error. Resolve pods that repeatedly crash and restart in an infinite loop."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## CrashLoopBackOff

This error occurs when a pod crashes immediately after starting, and Kubernetes repeatedly restarts it. After each crash, the backoff delay increases exponentially (10s, 20s, 40s, 80s, up to 5 minutes).

### Common Causes

- Application error or unhandled exception in the container
- Missing environment variables or configuration
- Liveness probe failing and killing the container
- Resource limits too low (OOMKilled)
- Incorrect command or entrypoint
- Dependency service not available (database, API)

### How to Fix

View container logs (previous instance):
```bash
kubectl logs <pod-name> --previous
```

Check the exit code:
```bash
kubectl get pod <pod-name> -o jsonpath='{.status.containerStatuses[0].state.terminated.exitCode}'
```

Check resource limits:
```bash
kubectl describe pod <pod-name> | grep -A5 Limits
```

Check liveness probe:
```bash
kubectl describe pod <pod-name> | grep -A10 Liveness
```

### Examples

```bash
# View logs of crashed container
kubectl logs my-app-7d4f9c7b6-abcde --previous --tail=50

# Increase memory limit
kubectl set resources deployment/my-app --limits=memory=512Mi
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})