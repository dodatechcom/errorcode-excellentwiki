---
title: "[Solution] k8s: NetworkPolicy Error — Traffic Blocked by Policy"
description: "Fix Kubernetes NetworkPolicy errors. Resolve network policy blocking pod-to-pod communication and traffic isolation issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["kubernetes", "k8s", "networkpolicy", "cni", "network", "isolation", "ingress", "egress"]
weight: 5
---

# k8s: NetworkPolicy Error — Traffic Blocked by Policy

A NetworkPolicy error occurs when a Kubernetes NetworkPolicy blocks legitimate pod-to-pod communication. Pods cannot reach services or other pods despite being healthy and scheduled.

## What This Error Means

Kubernetes NetworkPolicies control traffic flow between pods at the IP/port level. When a NetworkPolicy is applied, the CNI plugin (Calico, Cilium, etc.) enforces the rules. A misconfigured policy can accidentally block all ingress or egress traffic, isolating pods.

## Common Causes

- Default deny-all policy applied without explicit allow rules
- NetworkPolicy selector matching the wrong pods
- Ingress/egress rules missing for required services
- CNI plugin does not support NetworkPolicy (e.g., default Docker bridge)
- Policy applied to wrong namespace
- Label selector not matching target pods

## How to Fix

### Check Existing NetworkPolicies

```bash
kubectl get networkpolicy
kubectl describe networkpolicy <policy-name>
```

### Debug Blocked Traffic

```bash
# Test connectivity from a pod
kubectl exec -it <pod> -- curl -v http://<service>:<port>

# Check if CNI supports NetworkPolicy
kubectl get pods -n kube-system | grep -E "calico|cilium|weave|canal"
```

### Fix a Default Deny Policy

```yaml
# Allow ingress only from specific pods
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-backend
  namespace: default
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - port: 8080
          protocol: TCP
```

### Allow All Traffic (Remove Isolation)

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-all
  namespace: default
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress
  ingress:
    - {}
  egress:
    - {}
```

### Check CNI Plugin

```bash
# Verify CNI supports NetworkPolicy
kubectl get pods -n kube-system -o wide | grep -E "calico|cilium|flannel"
```

If using Flannel (no NetworkPolicy support), switch to Calico or Cilium.

## Related Errors

- [k8s Service Unavailable]({{< relref "/os/linux/linux-k8s-service-unavailable" >}}) — Service connectivity issues
- [k8s DNS Resolution Failed]({{< relref "/os/linux/linux-k8s-dns-resolution" >}}) — DNS lookup failures
- [k8s RBAC Forbidden]({{< relref "/os/linux/linux-k8s-rbac-error" >}}) — RBAC permission issues
