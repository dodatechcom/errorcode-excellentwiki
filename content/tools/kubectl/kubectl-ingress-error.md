---
title: "[Solution] Kubectl Ingress Error - Fix Ingress Resource Not Working"
description: "Fix Kubernetes Ingress resource errors. Resolve backend service issues, TLS configuration, and controller misconfigurations."
tools: ["kubectl"]
error-types: ["ingress-error"]
severities: ["error"]
weight: 5
---

This error means a Kubernetes Ingress resource is not routing traffic correctly. The Ingress controller may not be configured, the backend service may be unreachable, or TLS may be misconfigured.

## What This Error Means

When an Ingress resource fails to route traffic, you see symptoms like 502 errors, connection refused, or TLS certificate errors. The Ingress resource itself may appear valid:

```
kubectl get ingress
NAME        CLASS   HOSTS             ADDRESS   PORTS     AGE
my-ingress  nginx   app.example.com             80, 443   5m
```

But traffic to the configured host does not reach the backend service.

## Why It Happens

- No Ingress controller is installed in the cluster
- The Ingress class does not match the installed controller
- The backend service name or port is incorrect
- The service endpoints have no ready pods
- TLS secret does not exist or contains invalid certificates
- The ingress controller cannot resolve the backend service DNS
- The ingress controller pod is not running

## How to Fix It

### Verify an Ingress controller is installed

```bash
kubectl get pods -n ingress-nginx
kubectl get svc -n ingress-nginx
```

Ensure the controller pods are running and the LoadBalancer or NodePort service has an external IP.

### Check the Ingress class

```bash
kubectl get ingressclass
```

Match the Ingress resource's `ingressClassName` to the installed controller:

```yaml
spec:
  ingressClassName: nginx
```

### Verify the backend service

```bash
kubectl get svc my-service
kubectl get endpoints my-service
```

The endpoints must list pod IPs. If empty, the service selector does not match any pods.

### Check ingress controller logs

```bash
kubectl logs -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx
```

Controller logs show routing errors and TLS issues.

### Verify TLS secret

```bash
kubectl get secret my-tls-secret
kubectl get secret my-tls-secret -o jsonpath='{.data.tls\.crt}' | base64 -d | openssl x509 -noout -subject
```

The certificate must match the hostname in the Ingress.

### Test the backend directly

```bash
kubectl exec -it debug-pod -- curl http://my-service:8080
```

If the backend works inside the cluster but not via Ingress, the issue is in the Ingress configuration.

### Enable annotations for your controller

```yaml
metadata:
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
```

Different Ingress controllers use different annotation schemes.

## Common Mistakes

- Deploying an Ingress resource without installing an Ingress controller first
- Using wrong Ingress class name that does not match the controller
- Not checking that service endpoints have ready pods
- Forgetting to create the TLS secret before referencing it in the Ingress
- Assuming the Ingress automatically works without testing backend connectivity

## Related Pages

- [Kubectl Connection Refused]({{< relref "/tools/kubectl/kubectl-connection-refused" >}}) -- connectivity issues
- [Kubectl Pod Pending]({{< relref "/tools/kubectl/kubectl-pod-pending" >}}) -- pod scheduling
- [Kubectl RBAC Error]({{< relref "/tools/kubectl/kubectl-rbac-error" >}}) -- access control
