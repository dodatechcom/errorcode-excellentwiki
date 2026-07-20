---
title: "[Solution] CoreDNS pending or crash looping"
description: "Fix Kubernetes CoreDNS Pending or CrashLoopBackOff errors. Resolve DNS service failures in the cluster."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## CoreDNS Pending / CrashLoopBackOff

CoreDNS provides DNS resolution for the cluster. If CoreDNS pods are not running, service discovery breaks and pods cannot resolve service names.

### Common Causes

- CoreDNS pods cannot be scheduled (insufficient resources)
- CoreDNS ConfigMap is misconfigured
- Network policy blocking DNS traffic
- CoreDNS image not available (rate limited)

### How to Fix

Check CoreDNS status:
```bash
kubectl get pods -n kube-system -l k8s-app=kube-dns
```

Check CoreDNS logs:
```bash
kubectl logs -n kube-system -l k8s-app=kube-dns
```

Restart CoreDNS:
```bash
kubectl rollout restart -n kube-system deployment/coredns
```

### Examples

```bash
# Check CoreDNS pods
kubectl get pods -n kube-system | grep dns
# coredns-xxxxx   0/1   CrashLoopBackOff

# View CoreDNS logs
kubectl logs -n kube-system deployment/coredns
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})