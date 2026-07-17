---
title: "[Solution] Kubernetes DNS Resolution Failed — DNS resolution failed in pod"
description: "Fix Kubernetes DNS resolution errors. Resolve DNS failures in pods."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

A DNS resolution failed error means pods cannot resolve service names or external hostnames. This breaks service-to-service communication and external connectivity.

## Common Causes

- CoreDNS pods are not running or are crash-looping
- DNS configuration in resolv.conf is incorrect
- Network policies block DNS traffic (port 53)
- CoreDNS has insufficient resources
- Node DNS resolver configuration is wrong

## How to Fix

### Check CoreDNS Pods

```bash
kubectl get pods -n kube-system -l k8s-app=kube-dns
```

### Test DNS Resolution from Pod

```bash
kubectl exec -it <pod> -- nslookup kubernetes.default
kubectl exec -it <pod> -- nslookup <service-name>
```

### Check CoreDNS Configuration

```bash
kubectl get configmap coredns -n kube-system -o yaml
```

### Restart CoreDNS

```bash
kubectl rollout restart deployment coredns -n kube-system
```

### Verify Pod DNS Settings

```bash
kubectl exec -it <pod> -- cat /etc/resolv.conf
```

## Examples

```bash
# Example 1: CoreDNS not running
kubectl get pods -n kube-system -l k8s-app=kube-dns
# No resources found
# Fix: check kube-dns deployment

# Example 2: DNS resolution fails
kubectl exec -it my-pod -- nslookup my-service
# ** server can't find my-service.default.svc.cluster.local: NXDOMAIN
# Fix: check service name and namespace
```

## Related Errors

- [Kubernetes NetworkPolicy]({{< relref "/tools/kubernetes/k8s-network-policy" >}}) — connection refused
- [Kubernetes Service Unavailable]({{< relref "/tools/kubernetes/k8s-service-unavailable" >}}) — no endpoints
