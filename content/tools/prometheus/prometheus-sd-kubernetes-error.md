---
title: "[Solution] Prometheus Kubernetes Service Discovery Error"
description: "How to fix Prometheus Kubernetes service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- RBAC permissions insufficient for Prometheus
- Kubernetes API server unreachable
- Service account token expired or invalid
- Wrong API server URL or CA certificate

## How to Fix

Configure Kubernetes SD:

```yaml
scrape_configs:
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
        api_server: 'https://kubernetes.default.svc'
        tls_config:
          ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
```

Check RBAC:

```bash
kubectl auth can-i get pods --as=system:serviceaccount:monitoring:prometheus
```

## Examples

```bash
# Check Prometheus service account
kubectl get sa prometheus -n monitoring

# Verify RBAC
kubectl auth can-i list pods --as=system:serviceaccount:monitoring:prometheus

# View discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.labels.job == "kubernetes-pods")'
```
