---
title: "[Solution] NodeLost (node unreachable)"
description: "Fix Kubernetes NodeLost error. Resolve nodes that have become unreachable from the control plane."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## NodeLost

`status.conditions: [{type: "NodeLost", status: "True"}]`

The NodeLost condition indicates the control plane has lost communication with the node. Kubernetes waits for `pod-eviction-timeout` (default 5 minutes) before evicting pods.

### Common Causes

- Node is powered off or crashed
- Network connectivity lost between node and API server
- Kubelet process crashed or is hung
- Firewall or security group blocking traffic
- Node was terminated by the cloud provider

### How to Fix

Check node status:
```bash
kubectl get node <node-name> -o wide
```

SSH to the node (if possible):
```bash
ssh <node-ip> systemctl status kubelet
ssh <node-ip> systemctl restart kubelet
```

If the node is permanently lost, remove it:
```bash
kubectl delete node <node-name>
```

### Examples

```bash
# Check node conditions
kubectl describe node <node> | grep NodeLost

# Force delete node
kubectl delete node failed-node

# Check pod eviction
kubectl get pods -o wide | grep failed-node
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})