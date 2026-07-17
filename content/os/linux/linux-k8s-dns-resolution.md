---
title: "[Solution] k8s: DNS Resolution Failed — Cannot Resolve Service Names"
description: "Fix Kubernetes DNS resolution failures. Resolve 'could not resolve host', CoreDNS issues, and service name resolution problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["kubernetes", "k8s", "dns", "coredns", "service", "resolution", "ndots"]
weight: 5
---

# k8s: DNS Resolution Failed — Cannot Resolve Service Names

A DNS resolution failure occurs when pods cannot resolve Kubernetes Service names. The error reads:

> "Could not resolve host: my-service"

Or:

> "Temporary failure in name resolution"

## What This Error Means

Kubernetes uses CoreDNS to provide DNS resolution for pods. Services are accessible via DNS names like `my-service.my-namespace.svc.cluster.local`. When CoreDNS is down, misconfigured, or the pod's DNS settings are wrong, name resolution fails. This breaks all service-to-service communication.

## Common Causes

- CoreDNS pods not running or crashing
- CoreDNS configuration corrupted
- Pod DNS policy misconfigured
- Network policy blocking DNS traffic (UDP/TCP port 53)
- ndots setting causing unnecessary DNS lookups
- Node DNS configuration broken (resolv.conf)

## How to Fix

### Check CoreDNS Status

```bash
kubectl get pods -n kube-system -l k8s-app=kube-dns
kubectl logs -n kube-system -l k8s-app=kube-dns
```

### Restart CoreDNS

```bash
kubectl rollout restart deployment coredns -n kube-system
```

### Check CoreDNS Configuration

```bash
kubectl get configmap coredns -n kube-system -o yaml
```

### Test DNS Resolution from Inside a Pod

```bash
kubectl run debug --rm -it --image=busybox -- nslookup my-service
kubectl run debug --rm -it --image=busybox -- nslookup kubernetes.default
```

### Fix DNS Policy

```yaml
spec:
  dnsPolicy: ClusterFirst
  # Or use host DNS
  dnsPolicy: ClusterFirstWithHostNet
```

### Adjust ndots Setting

```yaml
spec:
  dnsConfig:
    options:
      - name: ndots
        value: "2"
```

### Ensure DNS Traffic Is Allowed

```bash
# Check NetworkPolicy doesn't block port 53
kubectl get networkpolicy -o yaml | grep -A 10 "ports"
```

### Check Node DNS

```bash
cat /etc/resolv.conf
# Should contain the cluster DNS IP
```

## Related Errors

- [k8s Service Unavailable]({{< relref "/os/linux/linux-k8s-service-unavailable" >}}) — Service connectivity issues
- [k8s NetworkPolicy Error]({{< relref "/os/linux/linux-k8s-network-policy" >}}) — Network policy blocking traffic
- [k8s CoreDNS Error]({{< relref "/os/linux/linux-k8s-dns-resolution" >}}) — CoreDNS pod issues
