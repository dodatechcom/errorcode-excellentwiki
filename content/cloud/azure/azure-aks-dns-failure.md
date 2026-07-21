---
title: "[Solution] Azure AKS DNS Resolution Failure"
description: "Fix Azure Kubernetes Service DNS resolution failures preventing pod-to-pod and external communication."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

DNS resolution failures in AKS prevent pods from resolving service names and external domains. This breaks internal service communication and outbound connectivity.

## Common Causes

- CoreDNS pods are not running or have crashed
- The DNS policy on the pod is configured incorrectly
- Network policies block DNS traffic on port 53
- Custom DNS servers are configured but unreachable from the cluster

## How to Fix

### Check CoreDNS pod status

```bash
kubectl get pods -n kube-system -l k8s-app=kube-dns
```

### Restart CoreDNS deployment

```bash
kubectl rollout restart deployment coredns -n kube-system
```

### Verify DNS service is running

```bash
kubectl get svc kube-dns -n kube-system
```

### Test DNS resolution from a pod

```bash
kubectl run dnstest --rm -it --image=busybox -- nslookup kubernetes.default
```

## Examples

- Pods cannot resolve service names and all HTTP calls fail with `ENOTFOUND`
- CoreDNS pods stuck in CrashLoopBackOff due to configuration syntax errors
- External DNS resolution works but internal service discovery fails

## Related Errors

- [Azure AKS Error]({{< relref "/cloud/azure/azure-aks-error" >}}) -- General AKS errors.
- [Azure Network Policy]({{< relref "/cloud/azure/azure-network-policy" >}}) -- Network policy issues.
