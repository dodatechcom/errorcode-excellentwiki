---
title: "[Solution] Kubernetes NetworkPolicy — ingress blocked"
description: "Fix Kubernetes NetworkPolicy ingress blocked. Resolve network policy blocking pod communication."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A NetworkPolicy ingress blocked error means a NetworkPolicy is preventing incoming traffic to pods, causing connectivity failures between services or from external clients.

## What This Error Means

Kubernetes NetworkPolicies act as firewalls for pod traffic. When a NetworkPolicy with `ingress` rules is applied, only traffic matching the specified `from` selectors is allowed. All other ingress traffic is denied by default. Pods behind a restrictive NetworkPolicy become unreachable from services, ingress controllers, or other namespaces that are not explicitly allowed.

## Common Causes

- NetworkPolicy has no `ingress` rules allowing traffic from needed sources
- Default deny-all policy applied without explicit allow rules
- Namespace selector in NetworkPolicy does not match source namespace
- Pod selector does not match target pod labels
- Network plugin (Calico, Cilium) not installed — policies have no effect or block everything
- Missing `ingress` stanza entirely when `podSelector` is set

## How to Fix

### Check Existing NetworkPolicies

```bash
kubectl get networkpolicies -n <namespace>
kubectl describe networkpolicy <policy-name>
```

### Test Connectivity

```bash
kubectl run test --rm -it --image=busybox -- wget -qO- --timeout=5 http://<service-name>
```

### Allow Traffic from Specific Namespace

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-ingress
  namespace: default
spec:
  podSelector:
    matchLabels:
      app: my-app
  policyTypes:
    - Ingress
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              name: ingress-nginx
      ports:
        - protocol: TCP
          port: 8080
```

### Allow All Ingress Traffic

```yaml
ingress:
  - {}  # Empty rule allows all ingress
```

### Verify Network Plugin is Installed

```bash
kubectl get pods -n kube-system | grep -E "calico|cilium|weave"
```

### Test with NetworkPolicy Removed

```bash
kubectl delete networkpolicy <policy-name> -n <namespace>
```

## Related Errors

- [Kubernetes Service Unavailable]({{< relref "/tools/kubernetes/k8s-service-unavailable-v2" >}}) — no endpoints
- [Kubernetes DNS Resolution]({{< relref "/tools/kubernetes/k8s-dns-resolution-v2" >}}) — CoreDNS failed
- [Kubernetes Ingress Error]({{< relref "/tools/kubernetes/k8s-ingress-error-v2" >}}) — TLS error
