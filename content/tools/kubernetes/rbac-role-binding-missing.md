---
title: "[Solution] RBAC RoleBinding missing"
description: "Fix Kubernetes RBAC RoleBinding missing errors. Resolve when a role binding does not exist for the required role and user."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## RBAC RoleBinding Missing

`(user "user@example.com" cannot list resource "pods" in API group "" in the namespace "default")`

This error occurs when a user or service account has a role assigned but no RoleBinding links it to the namespace.

### Common Causes

- RoleBinding has not been created in the namespace
- RoleBinding references a role that does not exist
- RoleBinding is in the wrong namespace
- ClusterRoleBinding was created but not ClusterRole

### How to Fix

List RoleBindings in the namespace:
```bash
kubectl get rolebindings -n <namespace>
```

Create a RoleBinding:
```bash
kubectl create rolebinding <name> --role=<role> --user=<user> --namespace=<ns>
```

### Examples

```bash
# Check existing bindings
kubectl get rolebindings --all-namespaces | grep <user>

# Create binding
kubectl create rolebinding pod-reader --role=pod-reader --user=user@example.com --namespace=default
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})