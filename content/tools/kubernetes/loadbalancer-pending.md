---
title: "[Solution] LoadBalancer Pending"
description: "Fix Kubernetes LoadBalancer service stuck in Pending state. Resolve issues when a Service of type LoadBalancer does not get an external IP."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## LoadBalancer Pending

`<service>   LoadBalancer   <cluster-ip>   <pending>     80:30080/TCP`

This issue occurs when a LoadBalancer service cannot get an external IP address from the cloud provider.

### Common Causes

- Running on-premises or bare-metal without a load balancer controller
- Cloud provider load balancer quota exceeded
- MetalLB or other LB controller not installed
- Service annotation misconfiguration

### How to Fix

Check the service events:
```bash
kubectl describe service <name>
```

Install a load balancer controller (for on-premises):
```bash
# MetalLB
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.14/config/manifests/metallb-native.yaml
```

### Examples

```bash
# Check service events
kubectl describe service my-service | grep -A10 Events
#  Error: error creating load balancer: Quota exceeded

# Install MetalLB
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.14/config/manifests/metallb-native.yaml
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})