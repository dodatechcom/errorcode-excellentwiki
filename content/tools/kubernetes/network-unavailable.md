---
title: "[Solution] NetworkUnavailable"
description: "Fix Kubernetes NetworkUnavailable node condition. Resolve nodes where the network is not ready for pod communication."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## NetworkUnavailable

This node condition indicates that the network on the node is not properly configured for pod networking. Usually caused by CNI plugin issues.

### Common Causes

- CNI plugin (Calico, Flannel, Weave, Cilium) is not installed
- CNI pod is not running on the node
- CNI configuration is invalid
- Firewall rules blocking pod-to-pod communication

### How to Fix

Check CNI pods:
```bash
kubectl get pods -n kube-system | grep -E "calico|flannel|weave|cilium"
```

Check CNI logs:
```bash
kubectl logs -n kube-system <cni-pod> --tail=50
```

On the node, check CNI config:
```bash
ls /etc/cni/net.d/
cat /etc/cni/net.d/*.conf
```

### Examples

```bash
# Check CNI status
kubectl get pods -n kube-system | grep -i "calico\|flannel\|weave\|cilium"
# calico-node-xxxxx   1/1   Running

# Check node network condition
kubectl describe node <node> | grep NetworkUnavailable
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})