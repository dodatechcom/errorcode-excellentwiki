---
title: "[Solution] kubectl logs failed"
description: "Fix 'kubectl logs' failures. Resolve errors when trying to view container logs."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## kubectl Logs Failed

`error: previous terminated container "<name>" in pod "<name>" not found`

This error occurs when kubectl cannot retrieve logs from a container.

### Common Causes

- Pod has not started yet or is in Pending state
- Container has never run (no logs available)
- Container name is incorrect (multi-container pods)
- Pod has been deleted and logs are no longer available
- Container crashed before producing any output

### How to Fix

Check pod status:
```bash
kubectl get pod <pod-name>
```

List containers in the pod:
```bash
kubectl get pod <pod-name> -o jsonpath='{.spec.containers[*].name}'
```

For multi-container pods, specify the container:
```bash
kubectl logs <pod-name> -c <container-name>
```

Use `--tail` and `--since` to limit output:
```bash
kubectl logs <pod-name> --tail=50 --since=5m
```

### Examples

```bash
# View logs for specific container
kubectl logs my-app -c sidecar

# Stream logs
kubectl logs -f my-app

# Check previous instance logs
kubectl logs my-app --previous
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})