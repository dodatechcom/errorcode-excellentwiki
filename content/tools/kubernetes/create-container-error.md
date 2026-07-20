---
title: "[Solution] CreateContainerError"
description: "Fix Kubernetes CreateContainerError. Resolve pod failures when the container runtime cannot create the container due to configuration issues."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## CreateContainerError

This error occurs when the container runtime cannot create the container due to configuration or resource issues after the image is pulled and config is resolved.

### Common Causes

- Invalid security context settings
- Root filesystem issues or overlay filesystem errors
- Container runtime (containerd/CRI-O) not functioning
- Node disk space exhausted
- Invalid container capabilities or seccomp profile

### How to Fix

Describe the pod for detailed error:
```bash
kubectl describe pod <pod-name>
```

Check node disk space:
```bash
kubectl debug node/<node-name> -- df -h
```

Check container runtime on the node:
```bash
kubectl get nodes -o wide
# SSH to node and check: systemctl status containerd
```

### Examples

```bash
# Check node disk pressure
kubectl describe node <node-name> | grep -i -A5 "Conditions"

# Free disk space on node
kubectl debug node/<node-name> -it --image=busybox -- df -h
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})