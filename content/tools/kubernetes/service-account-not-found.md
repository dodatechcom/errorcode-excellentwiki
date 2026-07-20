---
title: "[Solution] Service account not found"
description: "Fix Kubernetes service account not found error. Resolve pod creation failures when a referenced service account does not exist."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Service Account Not Found

`serviceaccounts "<name>" not found`

This error occurs when a pod spec references a service account that does not exist in the namespace.

### Common Causes

- Service account name is misspelled
- Service account has not been created
- Service account was deleted
- Pod is in a different namespace than the service account

### How to Fix

List service accounts:
```bash
kubectl get serviceaccounts
```

Create a service account:
```bash
kubectl create serviceaccount <name>
```

### Examples

```bash
# List all service accounts
kubectl get sa --all-namespaces

# Create service account
kubectl create sa my-app-sa
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})