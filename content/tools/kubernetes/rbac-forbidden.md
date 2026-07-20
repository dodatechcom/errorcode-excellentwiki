---
title: "[Solution] RBAC Forbidden (user cannot access resource)"
description: "Fix Kubernetes RBAC Forbidden error. Resolve permission denied errors when a user or service account lacks necessary roles."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## RBAC Forbidden

`<user> is forbidden: User "<user>" cannot <verb> resource "<resource>" in API group "<group>"`

This error occurs when the authenticated user or service account does not have RBAC permissions for the requested operation.

### Common Causes

- Insufficient RBAC role bindings
- Service account has limited scope
- Wrong namespace for the role binding
- Role binding references a role that doesn't exist

### How to Fix

Check the exact error to see what permission is missing:
```bash
kubectl auth can-i <verb> <resource> --as=<user>
```

Create a role binding:
```bash
kubectl create rolebinding <name> --role=<role> --user=<user> --namespace=<ns>
```

Create a cluster role binding:
```bash
kubectl create clusterrolebinding <name> --clusterrole=<role> --user=<user>
```

### Examples

```bash
# Check permissions for specific user
kubectl auth can-i list pods --as=deploy-bot --all-namespaces
# no

# Grant permission
kubectl create clusterrolebinding deploy-bot-view --clusterrole=view --user=deploy-bot
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})