---
title: "[Solution] CRI runtime error"
description: "Fix Kubernetes CRI runtime errors. Resolve Container Runtime Interface failures between kubelet and containerd/CRI-O."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## CRI Runtime Error

`failed to "CreateContainer" for "<container>" with CreateContainerError`

This error occurs when the CRI runtime (containerd/CRI-O) cannot create a container as requested by the kubelet.

### Common Causes

- Container runtime daemon is not responding
- OCI runtime (runc) errors during container creation
- Cgroup configuration issues
- Kernel security module (AppArmor, SELinux) blocking

### How to Fix

Check container runtime logs:
```bash
sudo journalctl -u containerd --no-pager --tail=100
sudo journalctl -u crio --no-pager --tail=100
```

### Examples

```bash
# Check containerd CRI errors
journalctl -u containerd --no-pager --tail=50 | grep -i "createcontainer\|CreateContainerError"
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})