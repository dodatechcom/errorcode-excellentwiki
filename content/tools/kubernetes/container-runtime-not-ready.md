---
title: "[Solution] Container runtime not ready"
description: "Fix Kubernetes container runtime not ready errors. Resolve kubelet startup failures when the container runtime is not available."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Container Runtime Not Ready

`Container runtime not ready: runtime "containerd" is not ready: connection refused`

This error occurs when the kubelet starts but cannot connect to the container runtime (containerd or CRI-O).

### Common Causes

- containerd/CRI-O service is not started
- containerd/CRI-O crashed during startup
- containerd socket path is incorrect in kubelet config
- containerd configuration is invalid
- containerd is enabled but failed to start due to cgroup issues

### How to Fix

Check the runtime status:
```bash
sudo systemctl status containerd
sudo journalctl -u containerd --no-pager --tail=100
```

Start the runtime:
```bash
sudo systemctl start containerd
```

Check the kubelet config for the correct runtime endpoint:
```bash
sudo cat /var/lib/kubelet/kubeadm-flags.env
```

### Examples

```bash
# Check containerd status
ssh <node> sudo systemctl status containerd
# Active: failed (Result: exit-code)

# Restart containerd
ssh <node> sudo systemctl restart containerd
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})