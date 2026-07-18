---
title: "[Solution] Kubectl RBAC Error - Fix Forbidden RBAC Access Denied"
description: "Fix Kubernetes RBAC forbidden errors when access is denied. Configure ClusterRoles, RoleBindings, and service account permissions."
tools: ["kubectl"]
error-types: ["rbac-error"]
severities: ["error"]
weight: 5
---

This error means your user or service account lacks the RBAC permissions to perform the requested action. Kubernetes denies any operation not explicitly allowed by a Role or ClusterRole binding.

## What This Error Means

When you try to perform an operation without proper RBAC permissions, you see:

```
Error from server (Forbidden): pods is forbidden: User "system:serviceaccount:default:my-sa"
cannot list resource "pods" in API group "" in the namespace "default"
```

RBAC is the access control system in Kubernetes. Every API request is checked against Role and ClusterRole bindings to determine if the caller has permission.

## Why It Happens

- The service account does not have a RoleBinding for the resource
- The ClusterRole does not include the required verbs (get, list, create, delete)
- The RoleBinding targets a different namespace than the operation
- You are using a default service account with no permissions
- A ClusterRoleBinding is missing for cluster-wide resources
- The user identity in the kubeconfig does not match any RBAC rules

## How to Fix It

### Check current permissions

```bash
kubectl auth can-i list pods
kubectl auth can-i create deployments --namespace=production
```

This tests whether the current user has specific permissions.

### Create a Role for the service account

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
```

### Bind the Role to the service account

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

### Create a ClusterRole for cluster-wide access

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: node-reader
rules:
  - apiGroups: [""]
    resources: ["nodes"]
    verbs: ["get", "list", "watch"]
```

### Bind the ClusterRole

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: read-nodes
subjects:
  - kind: ServiceAccount
    name: monitoring-sa
    namespace: kube-system
roleRef:
  kind: ClusterRole
  name: node-reader
  apiGroup: rbac.authorization.k8s.io
```

### Debug RBAC with verbose output

```bash
kubectl get pods -v=9 2>&1 | grep forbidden
```

Verbose output shows exactly which RBAC check failed.

## Common Mistakes

- Using the default service account instead of creating a dedicated one
- Forgetting that Roles are namespace-scoped while ClusterRoles are cluster-wide
- Not including all necessary verbs (get, list, watch, create, update, delete)
- Binding a Role to the wrong namespace
- Assuming admin access is available without explicit RBAC configuration

## Related Pages

- [Kubectl Permission Error]({{< relref "/tools/kubectl/kubectl-permission-error" >}}) -- permission denied
- [Kubectl Config Error]({{< relref "/tools/kubectl/kubectl-config-error" >}}) -- kubeconfig issues
- [Kubectl Connection Refused]({{< relref "/tools/kubectl/kubectl-connection-refused" >}}) -- connectivity
