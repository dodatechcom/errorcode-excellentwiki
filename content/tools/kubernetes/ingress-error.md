---
title: "[Solution] Kubernetes Ingress — no backend available / 503"
description: "Fix Kubernetes Ingress 503 Service Unavailable errors. Resolve no backend available issues in ingress controllers."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["ingress", "503", "service", "backend", "load-balancer"]
weight: 5
---

# Kubernetes Ingress — no backend available / 503

A 503 error from the ingress controller means no healthy backend pods are available to serve the request. The ingress rule exists but the target service has no ready endpoints.

## Common Causes

- Backend pods are not running or not ready
- Service selector does not match any pod labels
- Ingress controller cannot reach the backend service
- Backend pods failing health checks

## How to Fix

### Check Ingress and Endpoints

```bash
kubectl get ingress
kubectl get endpoints <service-name>
# If endpoints are empty, no pods match the service selector
```

### Verify Service Selector Matches Pods

```bash
kubectl get svc <service-name> -o yaml | grep -A 3 selector
kubectl get pods -l app=my-app
```

### Check Pod Readiness

```bash
kubectl get pods -o wide
# Ensure pods show READY 1/1
kubectl describe pod <pod-name> | grep -A 5 Conditions
```

### Verify Ingress Configuration

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
  annotations:
    nginx.ingress.kubernetes.io/backend-protocol: HTTP
spec:
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: my-app-service
                port:
                  number: 80
```

### Check Ingress Controller Logs

```bash
kubectl logs -n ingress-nginx <ingress-controller-pod>
```

## Examples

```bash
# Example 1: Empty endpoints
kubectl get endpoints my-app-service
# NAME             ENDPOINTS
# my-app-service   <none>
# Fix: ensure pod labels match service selector

# Example 2: Pods not ready
kubectl get pods
# NAME                    READY   STATUS
# my-app-7f8b9c6d5-x2k4  0/1     Running
# Fix: check readiness probe and application startup

# Example 3: Wrong port in ingress
kubectl describe ingress my-ingress
# Backend: my-app-service:8080
kubectl get svc my-app-service
# Port: 80
# Fix: match port numbers between ingress and service
```

## Related Errors

- [DNS Error]({{< relref "/tools/kubernetes/dns-error" >}}) — DNS resolution failed inside cluster
- [HPA Error]({{< relref "/tools/kubernetes/hpa-error" >}}) — autoscaler failing to get metrics
- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crashloop-debug" >}}) — backend pods crashing
