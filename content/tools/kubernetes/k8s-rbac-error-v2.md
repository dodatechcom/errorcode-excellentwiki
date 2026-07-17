---
title: "[Solution] Kubernetes RBAC — forbidden by ClusterRole"
description: "Fix Kubernetes RBAC forbidden errors. Resolve ClusterRole and ClusterRoleBinding permission issues."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An RBAC forbidden error means the authenticated user or service account lacks the required ClusterRole or Role permissions to perform the requested action on the Kubernetes API server.

## What This Error Means

Kubernetes RBAC (Role-Based Access Control) denies API requests when the caller does not have sufficient permissions. The error appears as `Error from server (Forbidden): <resource> is forbidden: User "<user>" cannot list resource "<resource>" in API group ""`. The request is authenticated but not authorized — the identity is valid but lacks the necessary role bindings.

## Common Causes

- Service account missing required ClusterRoleBinding
- ClusterRole does not include the needed API verbs
- Role is namespace-scoped but resource is cluster-scoped
- Missing `verbs: ["*"]` or specific verbs like `list`, `get`, `create`
- RoleBinding references wrong namespace
- Custom resource not included in RBAC rules

## How to Fix

### Check Current Permissions

```bash
kubectl auth can-i list pods --as=system:serviceaccount:default:my-sa
kubectl auth can-i '*' '*' --as=system:serviceaccount:default:my-sa
```

### Create ClusterRoleBinding

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: my-binding
subjects:
  - kind: ServiceAccount
    name: my-sa
    namespace: default
roleRef:
  kind: ClusterRole
  name: admin
  apiGroup: rbac.authorization.k8s.io
```

### Define Custom ClusterRole

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: pod-reader
rules:
  - apiGroups: [""]
    resources: ["pods", "pods/log"]
    verbs: ["get", "list", "watch"]
```

### Check Existing Role Bindings

```bash
kubectl get clusterrolebindings -o wide | grep <service-account>
kubectl describe clusterrole <role-name>
```

### Grant Namespace Role

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: pod-viewer
  namespace: default
subjects:
  - kind: User
    name: developer
roleRef:
  kind: Role
  name: view
  apiGroup: rbac.authorization.k8s.io
```

## Related Errors

- [Kubernetes Secret Error]({{< relref "/tools/kubernetes/k8s-secret-error-v2" >}}) — secret access error
- [Kubernetes API Server Error]({{< relref "/tools/kubernetes/k8s-api-server-error-v2" >}}) — API server timeout
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error-v2" >}}) — AWS IAM access denied
