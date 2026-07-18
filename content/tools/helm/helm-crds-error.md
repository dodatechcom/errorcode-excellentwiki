---
title: "[Solution] Helm CRDs Installation Failed Error Fix"
description: "Fix 'CRDs installation failed' errors in Helm. Install and manage Custom Resource Definitions with Helm charts."
tools: ["helm"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Helm CRDs Installation Failed Error Fix

The CRDs installation failed error occurs when Helm cannot install Custom Resource Definitions due to existing CRDs, permission issues, or invalid CRD manifests.

## What This Error Means

CRDs define new resource types in Kubernetes. Helm handles CRDs specially — they are only installed on create, not on upgrade. When CRDs fail to install, dependent resources cannot be created.

A typical error:

```
Error: CustomResourceDefinition.apiextensions.k8s.io is forbidden: 
User cannot list resource
```

## Why It Happens

Common causes include:

- **CRD already exists** — Helm skips CRDs on upgrade.
- **Insufficient permissions** — Service account cannot create CRDs.
- **Invalid CRD manifest** — CRD YAML is malformed.
- **Version conflict** — CRD version differs from installed.
- **Namespace issue** — CRDs are cluster-scoped but chart expects namespace.
- **Helm hooks misconfigured** — CRD hooks not running at right time.

## How to Fix It

### Fix 1: Install CRDs manually first

```bash
# RIGHT: Install CRDs before chart
kubectl apply -f mychart/crds/

# Or from specific file
kubectl apply -f mychart/crds/my-crd.yaml
```

### Fix 2: Use Helm hooks for CRDs

```yaml
# RIGHT: CRD as pre-install hook
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: myresources.example.com
  annotations:
    "helm.sh/hook": pre-install,pre-upgrade
    "helm.sh/hook-weight": "-5"
    "helm.sh/hook-delete-policy": before-hook-creation
```

### Fix 3: Check RBAC permissions

```yaml
# RIGHT: Ensure service account has CRD permissions
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: helm-crds
rules:
  - apiGroups: ["apiextensions.k8s.io"]
    resources: ["customresourcedefinitions"]
    verbs: ["create", "get", "list", "update"]
```

### Fix 4: Validate CRD YAML

```bash
# RIGHT: Validate before applying
kubectl apply --dry-run=client -f my-crd.yaml

# Lint with helm
helm lint mychart/
```

### Fix 5: Handle CRD updates

```bash
# RIGHT: Update CRDs manually
kubectl replace -f mychart/crds/my-crd.yaml

# Or delete and recreate
kubectl delete crd myresources.example.com
kubectl apply -f mychart/crds/my-crd.yaml
```

## Common Mistakes

- **Assuming Helm upgrades CRDs** — Helm does not upgrade CRDs automatically.
- **Not checking CRD exists before install** — Use `kubectl get crd`.
- **Forgetting CRDs are cluster-scoped** — They do not belong to namespaces.

## Related Pages

- [Helm Render Error](helm-render-error) — Template rendering issues
- [Helm RBAC Error](helm-rbac-error) — Permission issues
- [Helm Schema Error](helm-schema-error) — Values schema issues
