---
title: "[Solution] Cluster autoscaler failed to scale"
description: "Fix Kubernetes cluster autoscaler errors. Resolve issues when the cluster autoscaler cannot add or remove nodes."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Cluster Autoscaler Failed

`failed to scale up: AccessDenied`

This error occurs when the cluster autoscaler cannot add nodes due to cloud provider issues.

### Common Causes

- Cloud provider API permissions insufficient
- Instance quota exceeded in the cloud region
- Instance type unavailable in the availability zone
- Autoscaling group configuration issues

### How to Fix

Check cluster autoscaler logs:
```bash
kubectl logs -n kube-system deployment/cluster-autoscaler
```

### Examples

```bash
# Check cluster autoscaler status
kubectl get pods -n kube-system | grep autoscaler
# cluster-autoscaler-xxx   1/1   Running

# View autoscaler logs
kubectl logs -n kube-system deployment/cluster-autoscaler --tail=100
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})