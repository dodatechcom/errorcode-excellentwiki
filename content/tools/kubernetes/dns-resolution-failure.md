---
title: "[Solution] DNS resolution failure in pod"
description: "Fix Kubernetes DNS resolution failures inside pods. Resolve service discovery and name resolution issues."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## DNS Resolution Failure

`wget: bad address 'my-service'`

This error occurs when pods cannot resolve DNS names (service names, external hostnames).

### Common Causes

- CoreDNS pods are not running or in CrashLoopBackOff
- CoreDNS ConfigMap is misconfigured
- Network policy blocking DNS traffic (port 53)
- Pod's dnsPolicy is set to None without explicit nameservers
- ndots setting causes excessive DNS queries
- Cluster DNS IP is incorrect

### How to Fix

Check CoreDNS pods:
```bash
kubectl get pods -n kube-system -l k8s-app=kube-dns
```

Test DNS from a pod:
```bash
kubectl run test-$RANDOM --image=busybox -it --rm -- nslookup kubernetes.default
```

Check pod DNS configuration:
```bash
kubectl get pod <pod-name> -o jsonpath='{.spec.dnsPolicy}'
```

### Examples

```bash
# Test DNS
kubectl run dns-test --image=busybox -it --rm -- nslookup kubernetes.default.svc.cluster.local
# Server:    10.96.0.10
# Address:   10.96.0.10:53
# Name:      kubernetes.default.svc.cluster.local
# Address:   10.96.0.1
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})