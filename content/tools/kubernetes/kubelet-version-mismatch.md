---
title: "[Solution] Kubelet version mismatch"
description: "Fix Kubernetes kubelet version mismatch errors. Resolve issues when kubelet version differs from the API server version."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Kubelet Version Mismatch

This error occurs when the kubelet version on a node is too far behind or ahead of the API server version.

### Common Causes

- Node not upgraded after control plane upgrade
- New node added with outdated kubelet version
- Mixing very different Kubernetes versions

### How to Fix

Check versions:
```bash
kubectl version
kubectl get nodes -o wide
```

Upgrade kubelet on the node:
```bash
sudo apt-get update && sudo apt-get install -y kubelet=<version>
sudo systemctl restart kubelet
```

### Examples

```bash
# Check node kubelet versions
kubectl get nodes -o wide | awk '{print $1, $7}'
# node-1   v1.28.3
# node-2   v1.27.1  (outdated)

# Upgrade kubelet on node-2
ssh node-2 "sudo apt-get install -y kubelet=1.28.3-00 && sudo systemctl restart kubelet"
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})