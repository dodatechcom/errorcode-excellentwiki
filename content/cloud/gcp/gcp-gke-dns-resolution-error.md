---
title: "[Solution] GCP GKE DNS Resolution Error"
description: "Fix GKE DNS resolution errors. Resolve CoreDNS, kube-dns, and service discovery issues in Google Kubernetes Engine clusters."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP GKE DNS Resolution Error

The GKE DNS Resolution error occurs when pods cannot resolve service names or external hostnames due to DNS misconfiguration.

## Common Causes

- CoreDNS pods are not running or are in CrashLoopBackOff
- DNS service is not deployed in the cluster
- DNS policies are incorrect or too restrictive
- Node DNS configuration conflicts with cluster DNS
- External DNS is not configured for private zones

## How to Fix

### 1. Check CoreDNS status
```bash
kubectl get pods -n kube-system -l k8s-app=kube-dns
```

### 2. Test DNS resolution from a pod
```bash
kubectl run dns-test --rm -it --image=busybox -- nslookup kubernetes.default
```

### 3. Check DNS configuration
```bash
kubectl get configmap coredns -n kube-system -o yaml
```

### 4. Restart CoreDNS
```bash
kubectl rollout restart deployment coredns -n kube-system
```

### 5. Check node DNS settings
```bash
kubectl get nodes -o yaml | grep -A 5 "dnsPolicy"
```

## Examples

### Custom DNS config for a pod
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: dns-test
spec:
  dnsPolicy: "None"
  dnsConfig:
    nameservers:
    - 8.8.8.8
    searches:
    - ns1.svc.cluster-domain
    options:
    - name: ndots
      value: "5"
```

### Verify DNS service
```bash
kubectl get svc kube-dns -n kube-system
```

## Related Errors

- [GCP GKE Error]({{< relref "/cloud/gcp/gcp-gke-error" >}})
- [GCP Cloud DNS Error]({{< relref "/cloud/gcp/gcp-cloud-dns-error" >}})
