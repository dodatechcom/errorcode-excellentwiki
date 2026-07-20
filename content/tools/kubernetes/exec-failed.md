---
title: "[Solution] kubectl exec failed"
description: "Fix 'kubectl exec' errors. Resolve command execution failures inside running containers."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## kubectl Exec Failed

`error: unable to upgrade connection: pod not found`

This error occurs when kubectl exec cannot connect to the container to execute a command.

### Common Causes

- Pod is not running (Pending, CrashLoopBackOff, Evicted)
- Container name is incorrect (for multi-container pods)
- exec command or binary does not exist in the container

### How to Fix

Check pod status:
```bash
kubectl get pod <pod-name>
```

For multi-container pods, specify the container:
```bash
kubectl exec -it <pod-name> -c <container-name> -- /bin/sh
```

### Examples

```bash
# List containers in pod
kubectl get pod <pod-name> -o jsonpath='{.spec.containers[*].name}'

# Exec into specific container
kubectl exec -it my-app -c sidecar -- sh
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})