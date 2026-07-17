---
title: "[Solution] Kubernetes RBAC Error — forbidden: RBAC denied"
description: "Fix Kubernetes RBAC denied error. Resolve Role, ClusterRole, and RoleBinding permission issues."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Kubernetes RBAC Error — forbidden: RBAC denied

RBAC (Role-Based Access Control) errors occur when a user, service account, or pod doesn't have sufficient permissions to perform an action in the cluster.

## Common Causes

- Missing Role or ClusterRole for the service account
- RoleBinding not associated with the correct namespace
- Insufficient permissions in the Role rules
- Service account not assigned to the pod

## How to Fix

### Check Current Permissions

```bash
kubectl auth can-i <verb> <resource>
```

### Check Service Account

```bash
kubectl get serviceaccount <name> -n <namespace>
```

### Create a Role

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: default
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "list", "watch"]
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
    name: my-service-account
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

### Assign Service Account to Pod

```yaml
spec:
  serviceAccountName: my-service-account
```

## Examples

```bash
# Example 1: Forbidden error
kubectl get pods
# Error from server (Forbidden): pods is forbidden: User "system:serviceaccount:default:my-sa"
# Fix: create appropriate Role and RoleBinding

# Example 2: Check permissions
kubectl auth can-i list pods --as=system:serviceaccount:default:my-sa
# no
# Fix: grant permissions via RoleBinding

# Example 3: Cluster-wide access
kubectl create clusterrole pod-reader --verb=get,list,watch --resource=pods
```

## Related Errors

- [Secret Error]({{< relref "/tools/kubernetes/secret-error" >}}) — secret access denied
- [ConfigMap Error]({{< relref "/tools/kubernetes/configmap-error" >}}) — configmap not found
