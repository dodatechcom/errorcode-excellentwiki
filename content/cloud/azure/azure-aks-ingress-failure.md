---
title: "[Solution] Azure AKS Ingress Controller Failure"
description: "Troubleshoot Azure AKS ingress controller failures preventing external traffic routing to services."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Ingress controller failures prevent external HTTP/HTTPS traffic from reaching services inside the AKS cluster. This affects web applications and APIs exposed via ingress resources.

## Common Causes

- NGINX ingress controller pod is not running or stuck in CrashLoopBackOff
- Ingress resource references a service that does not exist in the namespace
- TLS certificate is missing or invalid for the configured hostname
- Load balancer health probes are failing due to incorrect backend health

## How to Fix

### Install NGINX ingress controller

```bash
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm install ingress-nginx ingress-nginx/ingress-nginx \
  --namespace ingress-nginx --create-namespace
```

### Check ingress controller logs

```bash
kubectl logs -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx
```

### Verify ingress resource status

```bash
kubectl get ingress my-ingress -o wide
```

### Create an ingress resource

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: my-service
                port:
                  number: 80
```

## Examples

- Ingress returns 502 Bad Gateway because the backend service is not responding
- TLS termination fails with `CertificateNotFound` when Secret is in a different namespace
- Health probe returns unhealthy status causing the load balancer to drain all backends

## Related Errors

- [Azure AKS Error]({{< relref "/cloud/azure/azure-aks-error" >}}) -- General AKS errors.
- [Azure Load Balancer Error]({{< relref "/cloud/azure/azure-load-balancer-error" >}}) -- Load balancer issues.
