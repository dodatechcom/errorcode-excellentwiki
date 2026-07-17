---
title: "[Solution] Kubernetes RBAC Error — forbidden by policy"
description: "Fix Kubernetes RBAC forbidden errors. Resolve Role-Based Access Control permission issues."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

An RBAC error occurs when a user, service account, or application attempts an action without the required Kubernetes Role-Based Access Control permissions.

## Common Causes

- The ServiceAccount lacks the required Role or ClusterRole
- RoleBinding or ClusterRoleBinding references the wrong namespace
- The role does not include the required API verbs (get, list, create, etc.)
- Using a default ServiceAccount without custom RBAC
- Resource or namespace scope mismatch in the role

## How to Fix

### Check Current Permissions

```bash
kubectl auth can-i <verb> <resource>
kubectl auth can-i --list
```

### Create a Role

```bash
kubectl create role pod-reader \
  --verb=get,list,watch \
  --resource=pods
```

### Bind Role to ServiceAccount

```bash
kubectl create rolebinding pod-reader-binding \
  --role=pod-reader \
  --serviceaccount=default:my-service-account
```

### Check ClusterRole Bindings

```bash
kubectl get clusterrolebindings -o wide | grep <service-account>
```

### Debug RBAC with Auth Can-I

```bash
kubectl auth can-i get pods --as=system:serviceaccount:default:my-sa
```

## Examples

```bash
# Example 1: Forbidden to list pods
kubectl auth can-i list pods --as=system:serviceaccount:default:my-sa
# no
# Fix: create Role and RoleBinding

# Example 2: Check all permissions
kubectl auth can-i --list --as=system:serviceaccount:default:my-sa
```

## Related Errors

- [Kubernetes Secret Error]({{< relref "/tools/kubernetes/k8s-secret-error" >}}) — Secret access denied
- [AWS IAM Error]({{< relref "/cloud/aws/iam-error" >}}) — AWS IAM permission denied
