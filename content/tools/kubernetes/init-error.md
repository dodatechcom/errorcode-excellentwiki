---
title: "[Solution] Init:Error"
description: "Fix Kubernetes Init:Error. Resolve pod initialization container failures during startup."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Init:Error

This error occurs when an init container in the pod fails to complete successfully. Init containers run before application containers and must finish successfully for the pod to start.

### Common Causes

- Init container command or script fails
- Missing dependencies or configuration in init container
- Network connectivity issues during init
- Volume mount permissions in init container
- Resource limits too low for init container

### How to Fix

Check init container logs:
```bash
kubectl logs <pod-name> -c <init-container-name>
```

Check init container exit code:
```bash
kubectl get pod <pod-name> -o jsonpath='{.status.initContainerStatuses[0].state.terminated.exitCode}'
```

### Examples

```bash
# View init container logs
kubectl logs my-app-7d4f9c7b6-abcde -c init-mydb

# Check init status
kubectl get pod my-app -o wide
# my-app   0/1   Init:Error   0   2m
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})