---
title: "[Solution] k8s: RBAC Forbidden — Access Denied by RBAC"
description: "Fix Kubernetes RBAC forbidden errors. Resolve 'forbidden' access denied errors by creating proper Role, ClusterRole, and RoleBinding resources."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["kubernetes", "k8s", "rbac", "forbidden", "role", "clusterrole", "binding"]
weight: 5
---

# k8s: RBAC Forbidden — Access Denied by RBAC

An RBAC forbidden error occurs when a user or service account tries to perform an action that is not permitted by Kubernetes RBAC policies. The error reads:

> "Error from server (Forbidden): pods is forbidden: User \"system:serviceaccount:default:default\" cannot list resource \"pods\" in API group \"\" in the namespace \"default\""

## What This Error Means

Kubernetes Role-Based Access Control (RBAC) controls who can do what on which resources. Every API request is checked against ClusterRoles, Roles, ClusterRoleBindings, and RoleBindings. When no rule grants the requested permission, the API server returns a 403 Forbidden error.

## Common Causes

- Default service account has no permissions
- RoleBinding or ClusterRoleBinding not created
- Role created in wrong namespace
- Missing verbs (create, get, list, watch, update, delete)
- ClusterRole not bound to the service account
- Token expired or invalid

## How to Fix

### Check Current Permissions

```bash
# Check what a service account can do
kubectl auth can-i list pods --as=system:serviceaccount:default:default
kubectl auth can-i '*' '*' --as=system:serviceaccount:default:default

# Check all permissions
kubectl auth can-i --list --as=system:serviceaccount:default:default
```

### Create a Role

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-reader
rules:
  - apiGroups: [""]
    resources: ["pods", "pods/log"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["get", "list"]
```

### Create a RoleBinding

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: default
subjects:
  - kind: ServiceAccount
    name: my-sa
    namespace: default
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

### Create Cluster-Wide Access

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader
rules:
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: read-secrets
subjects:
  - kind: ServiceAccount
    name: my-sa
    namespace: default
roleRef:
  kind: ClusterRole
  name: secret-reader
  apiGroup: rbac.authorization.k8s.io
```

### Debug RBAC

```bash
kubectl describe clusterrolebinding <name>
kubectl describe rolebinding <name> -n <namespace>

# Check if token is valid
kubectl auth whoami
```

## Related Errors

- [k8s Secret Error]({{< relref "/os/linux/linux-k8s-secret-error" >}}) — Secret access issues
- [k8s ConfigMap Error]({{< relref "/os/linux/linux-k8s-configmap-error" >}}) — ConfigMap access issues
- [k8s API Server Error]({{< relref "/os/linux/linux-k8s-api-server-error" >}}) — API server problems
