---
title: "[Solution] Kubectl Permission Error — Fix RBAC Authorization"
description: "Fix kubectl forbidden not authorized errors. Resolve RBAC roles, service accounts, and cluster permissions with step-by-step fixes."
---

## What This Error Means

The `forbidden` or `not authorized` error means the authenticated user or service account lacks the RBAC permissions required to perform the requested action on the specified resource.

A typical error:

```
Error from server (Forbidden): deployments.apps is forbidden: User
"system:serviceaccount:default:myapp" cannot list resource "deployments"
in API group "apps" in the namespace "default"
```

Or:

```
error: You must be logged in to the server (Unauthorized)
```

## Why It Happens

Permission errors occur when:

- **Missing RBAC role**: No Role or ClusterRole grants the required permissions.
- **Role not bound**: The Role exists but is not bound to the user or service account via RoleBinding.
- **Wrong namespace**: The RoleBinding is in a different namespace than the target resource.
- **Cluster-level permissions needed**: A Role only provides namespace-level access; ClusterRole is needed for cross-namespace operations.
- **Service account not configured**: Pods use a default service account without required permissions.
- **Authentication failure**: No valid credentials or token for API server authentication.

## How to Fix It

**Step 1: Check what permissions you have**

```bash
kubectl auth can-i --list
kubectl auth can-i get deployments
kubectl auth can-i create pods --namespace kube-system
```

**Step 2: Create a Role for namespace-level access**

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
    verbs: ["get", "list", "watch"]
```

**Step 3: Bind the Role to a user or service account**

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: default
subjects:
  - kind: User
    name: myuser
    apiGroup: rbac.authorization.k8s.io
  - kind: ServiceAccount
    name: myapp
    namespace: default
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

**Step 4: Create a ClusterRole for cluster-wide access**

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

**Step 5: Configure pod service accounts**

```yaml
spec:
  serviceAccountName: myapp
  containers:
    - name: myapp
      image: myapp:latest
```

## Common Mistakes

- **Using the default service account for production workloads**: Create dedicated service accounts with minimal permissions.
- **Binding ClusterRole to a namespace**: Use ClusterRoleBinding for cluster-wide access, RoleBinding for namespace-specific access.
- **Not testing permissions after changes**: Always verify with `kubectl auth can-i` after creating RBAC resources.
- **Granting overly broad permissions**: Follow the principle of least privilege. Grant only the verbs and resources needed.

## Related Pages

- [Kubectl Context Error](/tools/kubectl/kubectl-context-error/) — Context and authentication issues
- [Kubectl Resource Not Found](/tools/kubectl/kubectl-resource-not-found/) — Resource lookup failures
- [Ansible Permission Denied](/tools/ansible/ansible-permission-denied/) — SSH authentication errors
