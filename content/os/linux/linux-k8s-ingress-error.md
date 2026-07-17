---
title: "[Solution] k8s: Ingress Controller Error — Failed to Route Traffic"
description: "Fix Kubernetes Ingress controller errors. Resolve Ingress routing failures, SSL/TLS issues, and controller configuration problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# k8s: Ingress Controller Error — Failed to Route Traffic

An Ingress controller error occurs when the Ingress resource cannot route external traffic to backend services. The error may show:

> "no endpoints available for service" or

> "nginx: [emerg] host not found in upstream"

Or in the Ingress status:

> No IP address assigned to the Ingress load balancer.

## What This Error Means

Kubernetes Ingress resources define routing rules for external HTTP/HTTPS traffic. An Ingress controller (nginx, Traefik, HAProxy, etc.) watches Ingress resources and configures its reverse proxy. When the Ingress resource is misconfigured, the controller crashes, or backend services have no endpoints, traffic cannot flow.

## Common Causes

- Ingress controller not installed or not running
- Backend service has no endpoints (pods not ready)
- Incorrect host or path rules in Ingress
- TLS secret missing or invalid
- Ingress class not matching the controller
- Controller misconfiguration (annotations)
- Load balancer not provisioned for the Ingress controller

## How to Fix

### Check Ingress Controller Status

```bash
kubectl get pods -n ingress-nginx
kubectl logs -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx
```

### Check Ingress Resource

```bash
kubectl get ingress
kubectl describe ingress <ingress-name>
kubectl get ingress <ingress-name> -o yaml
```

### Verify Backend Service Endpoints

```bash
kubectl get endpoints <service-name>
kubectl get svc <service-name>
```

### Fix TLS Configuration

```bash
# Ensure TLS secret exists and has correct keys
kubectl get secret <tls-secret> -o yaml
kubectl get secret <tls-secret> -o jsonpath='{.data.tls\.crt}' | base64 -d
```

### Install nginx Ingress Controller

```bash
# Using Helm
helm upgrade --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace
```

### Check Ingress Class

```bash
kubectl get ingressclass
kubectl annotate ingress <name> kubernetes.io/ingress.class=nginx
```

### View Controller Logs for Errors

```bash
kubectl logs -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx --tail=100 | grep -i error
```

## Related Errors

- [k8s Service Unavailable]({{< relref "/os/linux/linux-k8s-service-unavailable" >}}) — Service has no endpoints
- [k8s Secret Error]({{< relref "/os/linux/linux-k8s-secret-error" >}}) — TLS secret issues
- [k8s DNS Resolution Failed]({{< relref "/os/linux/linux-k8s-dns-resolution" >}}) — DNS lookup failures
