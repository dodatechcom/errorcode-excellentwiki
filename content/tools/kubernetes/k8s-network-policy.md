---
title: "[Solution] Kubernetes NetworkPolicy Error — connection refused"
description: "Fix Kubernetes NetworkPolicy errors. Resolve network policy blocking connection issues."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["networkpolicy", "network", "policy", "connection", "kubernetes"]
weight: 5
---

A NetworkPolicy error occurs when network policies block traffic between pods or to external services. Connections are refused or timeout.

## Common Causes

- Default deny-all NetworkPolicy is applied
- Ingress or egress rules do not allow the required traffic
- NetworkPolicy namespace selector does not match target pods
- CNI plugin does not support NetworkPolicy (e.g., Docker bridge)
- Policy references non-existent pods or namespaces

## How to Fix

### List NetworkPolicies

```bash
kubectl get networkpolicy -A
```

### Check NetworkPolicy Details

```bash
kubectl get networkpolicy <name> -o yaml
```

### Verify CNI Plugin Supports NetworkPolicy

```bash
kubectl get pods -n kube-system | grep -i calico
kubectl get pods -n kube-system | grep -i cilium
```

### Create Allow Rules

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend
spec:
  podSelector:
    matchLabels:
      app: backend
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
```

### Delete Restrictive Policy (temporary)

```bash
kubectl delete networkpolicy <name>
```

## Examples

```bash
# Example 1: Connection refused between pods
kubectl get networkpolicy -A
# NAME            POD-SELECTOR   AGE
# deny-all        <none>         1d
# Fix: add allow rules for required traffic

# Example 2: Test without NetworkPolicy
kubectl delete networkpolicy deny-all
# Connection works now
# Fix: create proper allow rules
```

## Related Errors

- [Kubernetes DNS Resolution]({{< relref "/tools/kubernetes/k8s-dns-resolution" >}}) — DNS resolution failed
- [Kubernetes Service Unavailable]({{< relref "/tools/kubernetes/k8s-service-unavailable" >}}) — no endpoints
