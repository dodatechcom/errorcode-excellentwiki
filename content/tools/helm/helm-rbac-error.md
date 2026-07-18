---
title: "[Solution] Helm RBAC Permission Denied Error Fix"
description: "Fix 'RBAC permission denied' errors in Helm. Resolve Kubernetes RBAC issues for Helm deployments and service accounts."
tools: ["helm"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Helm RBAC Permission Denied Error Fix

The RBAC permission denied error occurs when the Helm service account or user lacks permissions to create, update, or delete Kubernetes resources.

## What This Error Means

RBAC (Role-Based Access Control) restricts what actions users and service accounts can perform. When Helm tries to manage resources without proper RBAC permissions, the operation is denied.

A typical error:

```
Error: deployments.apps is forbidden: 
User "system:serviceaccount:default:default" cannot list resource
```

## Why It Happens

Common causes include:

- **Missing ClusterRole** — Helm service account needs cluster-wide permissions.
- **Wrong namespace** — Role binding in wrong namespace.
- **Insufficient verbs** — Role missing required actions (create, update, delete).
- **Tiller not configured** — Helm v2 used Tiller with wrong permissions.
- **Scoped service account** — Service account limited to specific resources.

## How to Fix It

### Fix 1: Create proper RBAC

```yaml
# RIGHT: Service account with RBAC
apiVersion: v1
kind: ServiceAccount
metadata:
  name: helm-sa
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: helm-admin
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
  - kind: ServiceAccount
    name: helm-sa
    namespace: kube-system
```

### Fix 2: Use helm --service-account flag

```bash
# RIGHT: Specify service account
helm install myrelease mychart/ --service-account helm-sa
```

### Fix 3: Check current permissions

```bash
# RIGHT: Debug RBAC
kubectl auth can-i create deployments -n mynamespace
kubectl auth can-i '*' '*' --as system:serviceaccount:default:helm-sa
```

### Fix 4: Create namespace-scoped role

```yaml
# RIGHT: Namespace-scoped permissions
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: helm-role
  namespace: mynamespace
rules:
  - apiGroups: ["", "apps", "batch"]
    resources: ["*"]
    verbs: ["*"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: helm-binding
  namespace: mynamespace
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: helm-role
subjects:
  - kind: ServiceAccount
    name: default
    namespace: mynamespace
```

## Common Mistakes

- **Using cluster-admin when not needed** — Follow least privilege principle.
- **Forgetting that Helm manages many resource types** — Need permissions for all types used.
- **Not checking if service account exists** — Create SA before deploying.

## Related Pages

- [Helm Render Error](helm-render-error) — Template rendering issues
- [Helm CRDs Error](helm-crds-error) — CRD installation issues
- [Helm Resource Quota Error](helm-resource-quota) — Resource limit issues
