---
title: "[Solution] API 403 Forbidden"
description: "Fix Kubernetes API 403 Forbidden error. Resolve authorization failures when the user lacks permissions for a resource."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## API 403 Forbidden

This HTTP status code occurs when the user is authenticated but does not have authorization to perform the requested operation.

### Common Causes

- Missing RBAC role or cluster role
- Role binding does not include the user or service account
- Operation is restricted by an admission webhook
- Namespace does not exist or user cannot access it

### How to Fix

Check RBAC permissions:
```bash
kubectl auth can-i create deployments --namespace=default
```

Check available roles and bindings:
```bash
kubectl get clusterroles
kubectl get clusterrolebindings
```

### Examples

```bash
# Check what the user can do
kubectl auth can-i --list

# Grant cluster-admin
kubectl create clusterrolebinding my-admin --clusterrole=cluster-admin --user=user@example.com
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})