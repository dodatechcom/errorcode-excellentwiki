---
title: "[Solution] UnexpectedAdmissionError"
description: "Fix Kubernetes UnexpectedAdmissionError. Resolve pod failures when the container runtime encounters unexpected errors during pod creation."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## UnexpectedAdmissionError

This error occurs when the kubelet encounters an unexpected error during pod admission. The container runtime may not be functioning correctly.

### Common Causes

- Container runtime (containerd/CRI-O) is unhealthy or crashed
- Disk I/O errors on the node
- Node is low on memory or other resources
- Kernel module issues (overlay, devicemapper)
- Inode exhaustion on the filesystem

### How to Fix

Check node conditions:
```bash
kubectl describe node <node-name>
```

Check kubelet logs:
```bash
sudo journalctl -u kubelet --no-pager --tail=100
```

Restart containerd and kubelet:
```bash
sudo systemctl restart containerd
sudo systemctl restart kubelet
```

### Examples

```bash
# Check node for pressure conditions
kubectl describe node <node> | grep -A10 Conditions
# MemoryPressure  True

# Restart container runtime
ssh <node> sudo systemctl restart containerd && sudo systemctl restart kubelet
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})