---
title: "[Solution] Kubernetes Ingress — TLS configuration error"
description: "Fix Kubernetes Ingress TLS configuration errors. Resolve TLS certificate and ingress routing issues."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An Ingress TLS configuration error means the Ingress controller cannot establish TLS for incoming traffic, typically due to missing or invalid certificates, misconfigured secret references, or TLS termination issues.

## What This Error Means

Kubernetes Ingress resources route external HTTP/HTTPS traffic to services. When TLS is configured, the Ingress controller (e.g., nginx-ingress) reads the certificate from a TLS Secret referenced in the Ingress spec. If the Secret is missing, has invalid certificate data, or the secret name is incorrect, TLS handshakes fail and clients receive SSL errors. The Ingress controller logs will show the specific TLS failure.

## Common Causes

- TLS Secret does not exist or is in the wrong namespace
- Secret type is not `kubernetes.io/tls`
- Certificate or key data is invalid or corrupted
- Secret name in Ingress spec is misspelled
- Certificate has expired
- Ingress class does not support TLS termination

## How to Fix

### Check Ingress Status

```bash
kubectl describe ingress <ingress-name>
kubectl get ingress <ingress-name> -o yaml
```

### Verify TLS Secret Exists

```bash
kubectl get secret <secret-name> -o yaml
kubectl get secret <secret-name> -o jsonpath='{.type}'
```

### Create TLS Secret

```bash
kubectl create secret tls my-tls-secret \
  --cert=tls.crt \
  --key=tls.key
```

### Fix Ingress TLS Configuration

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  tls:
    - hosts:
        - myapp.example.com
      secretName: my-tls-secret
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

### Check Certificate Expiry

```bash
openssl x509 -in tls.crt -noout -dates
```

### Test TLS Configuration

```bash
curl -v https://myapp.example.com
openssl s_client -connect myapp.example.com:443
```

## Related Errors

- [Kubernetes Service Unavailable]({{< relref "/tools/kubernetes/k8s-service-unavailable-v2" >}}) — no endpoints
- [Kubernetes Secret Error]({{< relref "/tools/kubernetes/k8s-secret-error-v2" >}}) — secret decode error
- [Nginx SSL Error]({{< relref "/tools/nginx/nginx-ssl-error-v2" >}}) — SSL handshake failed
