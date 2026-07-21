---
title: "[Solution] Prometheus Bearer Token Error"
description: "How to fix bearer token authentication errors in Prometheus scrape configs"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Expired or invalid bearer token
- Token file missing or empty
- Wrong token format (should not include "Bearer" prefix)
- Target requires specific token scope

## How to Fix

Configure bearer token in scrape config:

```yaml
scrape_configs:
  - job_name: 'kubernetes-pods'
    bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    tls_config:
      ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    kubernetes_sd_configs:
      - role: pod
```

Inline token (not recommended for production):

```yaml
scrape_configs:
  - job_name: 'app'
    bearer_token: 'eyJhbGciOiJSUzI1NiIs...'
```

Refresh expired token:

```bash
# Kubernetes
kubectl get secret $(kubectl get sa prometheus -o jsonpath='{.secrets[0].name}') -o jsonpath='{.data.token}' | base64 -d
```

## Examples

```bash
# Test bearer token
curl -H "Authorization: Bearer $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" https://kubernetes:443/metrics

# Verify token is valid
kubectl auth can-i get pods --as=system:serviceaccount:monitoring:prometheus
```
