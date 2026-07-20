---
title: "[Solution] Failed to create pod sandbox"
description: "Fix Kubernetes 'Failed to create pod sandbox' error. Resolve pod creation failures in the container runtime during sandbox setup."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Failed to Create Pod Sandbox

`Failed to create pod sandbox: rpc error: code = Unknown desc = failed to create containerd task`

This error occurs when the container runtime cannot create the pod sandbox (the isolation environment for the pod's containers).

### Common Causes

- CNI plugin failed to set up networking
- Container runtime (containerd/CRI-O) not responding
- Network interface already exists
- IP address allocation failure
- Kernel module missing (overlay, br_netfilter)

### How to Fix

Check the full error:
```bash
kubectl describe pod <pod-name> | grep -A10 "Failed to create pod sandbox"
```

Check containerd/CRI-O status on the node:
```bash
sudo systemctl status containerd
sudo journalctl -u containerd --tail=50
```

### Examples

```bash
# Check containerd for sandbox errors
journalctl -u containerd --no-pager --tail=100 | grep -i "sandbox\|cni\|network"

# Restart containerd and kubelet
sudo systemctl restart containerd && sudo systemctl restart kubelet
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})