---
title: "[Solution] CNI plugin failed"
description: "Fix Kubernetes CNI plugin failure. Resolve network setup errors when the CNI plugin cannot configure pod networking."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## CNI Plugin Failed

`NetworkPlugin cni failed: cni plugin not initialized`

This error occurs when the CNI (Container Network Interface) plugin fails to set up network connectivity for a pod.

### Common Causes

- CNI plugin binary is missing or not installed
- CNI configuration file is invalid
- CNI plugin container (Calico, Flannel) is not running
- Kernel modules not loaded (bridge, iptables)

### How to Fix

Check CNI pods:
```bash
kubectl get pods -n kube-system | grep -E "calico|flannel|weave|cilium|canal"
```

On the node, check CNI config:
```bash
ls -la /etc/cni/net.d/
cat /etc/cni/net.d/*.conf*
```

### Examples

```bash
# Check CNI config on node
ssh <node> ls /etc/cni/net.d/
# 10-flannel.conflist
ssh <node> cat /etc/cni/net.d/10-flannel.conflist
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})