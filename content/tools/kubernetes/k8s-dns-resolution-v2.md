---
title: "[Solution] Kubernetes DNS — CoreDNS resolution failed"
description: "Fix Kubernetes DNS CoreDNS resolution failed. Resolve DNS lookup failures in cluster."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["kubernetes", "dns", "coredns", "resolution", "nameservice", "lookup"]
weight: 5
---

A DNS resolution failure means pods cannot resolve service names or external hostnames. CoreDNS, the cluster DNS server, is either down, misconfigured, or unreachable from the pod network.

## What This Error Means

Kubernetes uses CoreDNS to provide DNS resolution for services and pods. When a pod tries to resolve a service name (e.g., `my-service.default.svc.cluster.local`), the request goes to CoreDNS. If CoreDNS is unhealthy, its configuration is broken, or network policies block DNS traffic, resolution fails. Pods will see errors like `Temporary failure in name resolution` or `Could not resolve host`.

## Common Causes

- CoreDNS pods are not running or in CrashLoopBackOff
- CoreDNS configuration has syntax errors
- Network policies blocking UDP/TCP port 53 traffic to CoreDNS
- Node where CoreDNS runs has resource pressure
- `/etc/resolv.conf` in pod points to wrong DNS server
- CoreDNS upstream DNS servers are unreachable

## How to Fix

### Check CoreDNS Status

```bash
kubectl get pods -n kube-system -l k8s-app=kube-dns
kubectl logs -n kube-system -l k8s-app=kube-dns
```

### Test DNS Resolution from a Pod

```bash
kubectl run dns-test --rm -it --image=busybox -- nslookup kubernetes.default
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
kubectl exec <pod-name> -- cat /etc/resolv.conf
```

### Fix CoreDNS ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: coredns
  namespace: kube-system
data:
  Corefile: |
    .:53 {
        errors
        health { lameduck 5s }
        ready
        kubernetes cluster.local in-addr.arpa ip6.arpa {
            pods insecure
            fallthrough in-addr.arpa ip6.arpa
        }
        forward . /etc/resolv.conf
        cache 30
        loop
        reload
        loadbalance
    }
```

### Check NetworkPolicy for DNS

```bash
kubectl get networkpolicies -A -o wide | grep -i dns
```

## Related Errors

- [Kubernetes Service Unavailable]({{< relref "/tools/kubernetes/k8s-service-unavailable-v2" >}}) — no endpoints
- [Kubernetes NetworkPolicy]({{< relref "/tools/kubernetes/k8s-network-policy-v2" >}}) — ingress blocked
- [Kubernetes API Server Error]({{< relref "/tools/kubernetes/k8s-api-server-error-v2" >}}) — API server timeout
