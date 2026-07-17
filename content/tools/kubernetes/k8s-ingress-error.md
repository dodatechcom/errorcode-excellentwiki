---
title: "[Solution] Kubernetes Ingress Error — Ingress controller error"
description: "Fix Kubernetes Ingress controller errors. Resolve Ingress routing and configuration issues."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

An Ingress error occurs when the Ingress controller cannot route traffic to backend services. This can be caused by misconfiguration, missing controller, or certificate issues.

## Common Causes

- Ingress controller is not installed in the cluster
- Ingress resource references a non-existent Service
- TLS certificate is missing or invalid
- Host or path rules conflict with each other
- Backend service port is incorrect

## How to Fix

### Check Ingress Controller

```bash
kubectl get pods -n ingress-nginx
```

### Verify Ingress Resource

```bash
kubectl get ingress <name> -o yaml
```

### Check Ingress Events

```bash
kubectl describe ingress <name>
```

### Verify Service Exists

```bash
kubectl get svc <backend-service>
```

### Check TLS Secret

```bash
kubectl get secret <tls-secret>
```

### Test Ingress URL

```bash
curl -v http://<ingress-host>
```

## Examples

```bash
# Example 1: Ingress controller not found
kubectl get ingress my-ingress
# HOST        ADDRESS
# my-app.com
# Fix: install ingress-nginx controller

# Example 2: Backend service not found
kubectl describe ingress my-ingress
# Warning: service "my-app" not found
# Fix: create the service or correct the ingress spec
```

## Related Errors

- [Kubernetes Service Unavailable]({{< relref "/tools/kubernetes/k8s-service-unavailable" >}}) — no endpoints
- [Kubernetes DNS Resolution]({{< relref "/tools/kubernetes/k8s-dns-resolution" >}}) — DNS resolution failed
