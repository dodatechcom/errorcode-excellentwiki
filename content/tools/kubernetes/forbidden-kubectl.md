---
title: "[Solution] kubectl Forbidden error"
description: "Fix kubectl 'Forbidden' error. Resolve RBAC permission issues when kubectl commands are denied by the API server."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## kubectl Forbidden

`Error from server (Forbidden): <resource> is forbidden: User "<user>" cannot list resource "<resource>"`

This error occurs when the authenticated user or service account does not have RBAC permissions to perform the requested operation.

### Common Causes

- User lacks necessary RBAC role bindings
- Wrong namespace context
- Service account has limited permissions
- Cluster-admin role not granted

### How to Fix

Check your current permissions:
```bash
kubectl auth can-i create deployments
kubectl auth can-i list pods --all-namespaces
```

Create a role binding:
```bash
kubectl create clusterrolebinding <name> --clusterrole=cluster-admin --user=<user>
```

### Examples

```bash
# Check permissions
kubectl auth can-i get pods
# yes

# Grant admin access
kubectl create clusterrolebinding my-admin-binding --clusterrole=admin --user=user@example.com
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})