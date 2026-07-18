---
title: "[Solution] Helm Resource Quota Exceeded Error Fix"
description: "Fix 'resource quota exceeded' errors in Helm. Resolve Kubernetes resource limit issues during chart installation."
tools: ["helm"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Helm Resource Quota Exceeded Error Fix

The resource quota exceeded error occurs when Helm chart resources exceed Kubernetes namespace resource quotas or node resource limits.

## What This Error Means

Kubernetes namespaces can have resource quotas limiting CPU, memory, and object counts. When a Helm chart requests more resources than allowed, the deployment fails.

A typical error:

```
Error: exceeded quota: compute-quota, requested: cpu=2000m, 
used: cpu=1500m, limited: cpu=3000m
```

## Why It Happens

Common causes include:

- **Resource requests too high** — Chart requests more than quota allows.
- **Cumulative usage** — Existing pods plus new pods exceed quota.
- **Object count exceeded** — Too many ConfigMaps, Secrets, etc.
- **No resource limits defined** — Resources not constrained.
- **Wrong namespace** — Deploying to namespace with tight quotas.

## How to Fix It

### Fix 1: Check current quota usage

```bash
# RIGHT: Check quota
kubectl describe resourcequota -n mynamespace
kubectl get resourcequota -n mynamespace
```

### Fix 2: Reduce resource requests

```yaml
# values.yaml
resources:
  requests:
    cpu: 100m      # Reduced from 500m
    memory: 128Mi  # Reduced from 512Mi
  limits:
    cpu: 200m
    memory: 256Mi
```

### Fix 3: Increase quota

```yaml
# RIGHT: Increase namespace quota
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-quota
spec:
  hard:
    requests.cpu: "10"
    requests.memory: 20Gi
    limits.cpu: "20"
    limits.memory: 40Gi
```

### Fix 4: Use different namespace

```bash
# RIGHT: Deploy to namespace with more resources
helm install myrelease mychart/ -n dev --create-namespace
```

### Fix 5: Set resource requests in values

```yaml
# RIGHT: Always define resources
resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 250m
    memory: 256Mi
```

## Common Mistakes

- **Not checking quota before deployment** — Always verify quotas first.
- **Setting limits without requests** — Both should be defined.
- **Forgetting that requests count against quota** — Quotas limit requests, not usage.

## Related Pages

- [Helm Render Error](helm-render-error) — Template rendering issues
- [Helm RBAC Error](helm-rbac-error) — Permission issues
- [Helm Post Install Hook Error](helm-post-install-hook) — Hook failures
