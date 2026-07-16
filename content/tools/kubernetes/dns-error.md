---
title: "[Solution] Kubernetes DNS resolution failed inside cluster"
description: "Fix Kubernetes DNS resolution failures. Resolve CoreDNS issues and service name resolution problems."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["dns", "coredns", "name-resolution", "service", "networking"]
weight: 5
---

# Kubernetes DNS resolution failed inside cluster

DNS resolution failures prevent pods from reaching services by name. This affects all service-to-service communication that relies on Kubernetes DNS, which is nearly all cluster traffic.

## Common Causes

- CoreDNS pods are not running or crashing
- DNS service (kube-dns) is misconfigured
- Network policies blocking DNS traffic on port 53
- Pod's DNS policy is set to a non-cluster value

## How to Fix

### Check CoreDNS Status

```bash
kubectl get pods -n kube-system -l k8s-app=kube-dns
kubectl logs -n kube-system -l k8s-app=kube-dns
```

### Test DNS Resolution from a Pod

```bash
kubectl run dns-test --image=busybox:1.36 --rm -it -- nslookup kubernetes.default
# If this fails, CoreDNS is the issue
```

### Check DNS Service

```bash
kubectl get svc kube-dns -n kube-system
kubectl get endpoints kube-dns -n kube-system
```

### Restart CoreDNS

```bash
kubectl rollout restart deployment coredns -n kube-system
```

### Verify Pod DNS Configuration

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  dnsPolicy: ClusterFirst
  containers:
    - name: app
      image: my-app:latest
```

## Examples

```bash
# Example 1: CoreDNS crash loop
kubectl get pods -n kube-system -l k8s-app=kube-dns
# NAME                       READY   STATUS
# coredns-abc123             0/1     CrashLoopBackOff
kubectl logs -n kube-system coredns-abc123
# Error: plugin/loop: read udp 10.96.0.10:53: i/o timeout
# Fix: check upstream DNS and /etc/resolv.conf on node

# Example 2: Service name not resolving
kubectl run test --image=busybox --rm -it -- nslookup my-service
# ** server can't find my-service.default.svc.cluster.local: NXDOMAIN
# Fix: verify service exists: kubectl get svc my-service

# Example 3: DNS policy override
kubectl get pod my-pod -o jsonpath='{.spec.dnsPolicy}'
# None
# Fix: remove dnsPolicy or set to ClusterFirst
```

## Related Errors

- [Ingress Error]({{< relref "/tools/kubernetes/ingress-error" >}}) — 503 no backend available
- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crashloop-debug" >}}) — CoreDNS pod crashing
- [Network Error]({{< relref "/tools/kubernetes/service-error2" >}}) — service connectivity issues
