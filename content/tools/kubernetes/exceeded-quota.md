---
title: "[Solution] Resource quota exceeded"
description: "Fix Kubernetes 'exceeded quota' error. Resolve resource creation failures when namespace quotas are reached."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Resource Quota Exceeded

`exceeded quota: <quota-name>, requested: <resource>, used: <resource>, limited: <resource>`

This error occurs when a namespace has a ResourceQuota and the new resource would exceed the quota limits.

### Common Causes

- Namespace CPU or memory quota exhausted
- Pod count quota exceeded
- PVC count or storage quota exceeded
- Quotas set too restrictive

### How to Fix

Check quota usage:
```bash
kubectl get quota -n <namespace>
kubectl describe quota <name> -n <namespace>
```

Increase quota:
```bash
kubectl edit quota <name> -n <namespace>
```

Delete unnecessary resources to free up quota.

### Examples

```bash
# Check quota status
kubectl describe quota my-quota -n my-ns
# Resource     Used  Hard
# --------     ---   ---
# pods         45    50
# requests.cpu  8     10

# Free up resources
kubectl delete pod -n my-ns --field-selector=status.phase=Succeeded
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})