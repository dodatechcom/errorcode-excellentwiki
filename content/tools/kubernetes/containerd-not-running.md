---
title: "[Solution] containerd not running"
description: "Fix Kubernetes containerd service failures. Resolve container runtime issues on worker nodes."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Containerd Not Running

`failed to connect to containerd: connection refused`

This error occurs when the kubelet cannot connect to the containerd (or CRI-O) socket.

### Common Causes

- containerd service stopped or crashed
- containerd socket (/var/run/containerd/containerd.sock) is missing
- containerd configuration is invalid
- Disk space exhausted

### How to Fix

SSH to the node and check containerd:
```bash
sudo systemctl status containerd
sudo journalctl -u containerd --no-pager --tail=100
```

Start containerd:
```bash
sudo systemctl start containerd
sudo systemctl enable containerd
```

### Examples

```bash
# Check containerd status
ssh <node> sudo systemctl status containerd
# containerd.service - Container Runtime
#    Active: failed (Result: exit-code)

# Start containerd
ssh <node> sudo systemctl start containerd
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})