---
title: "[Solution] KubeletNotReady"
description: "Fix Kubernetes KubeletNotReady error. Resolve issues where the kubelet cannot start or becomes unhealthy on a node."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## KubeletNotReady

This error occurs when the kubelet on a node is running but not ready. The kubelet may be initializing, waiting for resources, or encountering configuration errors.

### Common Causes

- Kubelet cannot connect to the API server
- CNI plugin not configured or not working
- Container runtime not initialized
- Kubelet configuration is invalid
- TLS certificate issues

### How to Fix

SSH to the node and check kubelet:
```bash
sudo journalctl -u kubelet --no-pager --tail=100
```

Check kubelet configuration:
```bash
sudo cat /var/lib/kubelet/config.yaml
```

Restart kubelet:
```bash
sudo systemctl restart kubelet
```

### Examples

```bash
# Check kubelet for CNI errors
sudo journalctl -u kubelet | grep -i "cni"
#  Failed to initialize CNI: failed to load CNI config

# Fix: install CNI plugin binary and config
sudo cp /opt/cni/bin/<plugin> /opt/cni/bin/
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})