---
title: "[Solution] kube-proxy not running"
description: "Fix Kubernetes kube-proxy not running errors. Resolve service connectivity issues when kube-proxy is down on a node."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## kube-proxy Not Running

`kube-proxy: error running: error: could not start daemon`

This error occurs when kube-proxy is not running on a node, causing service traffic to fail.

### Common Causes

- kube-proxy DaemonSet pod is not running on the node
- kube-proxy configuration is invalid
- iptables/nftables kernel modules not loaded
- kube-proxy image not available
- kube-proxy cannot connect to the API server
- IPVS mode requires kernel modules

### How to Fix

Check kube-proxy pods:
```bash
kubectl get pods -n kube-system -l k8s-app=kube-proxy
```

Check kube-proxy logs:
```bash
kubectl logs -n kube-system -l k8s-app=kube-proxy
```

Restart kube-proxy:
```bash
kubectl delete pod -n kube-system -l k8s-app=kube-proxy
```

### Examples

```bash
# Check kube-proxy status
kubectl get pods -n kube-system | grep kube-proxy
# kube-proxy-xxxxx   0/1   CrashLoopBackOff

# View kube-proxy logs
kubectl logs -n kube-system kube-proxy-xxxxx
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})