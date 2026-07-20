---
title: "[Solution] No endpoints for service"
description: "Fix Kubernetes 'no endpoints for service' error. Resolve service connectivity failures when no pods match the service selector."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## No Endpoints for Service

`Warning: No endpoints for service <service>`

This warning occurs when a Kubernetes Service has no endpoints because no pods match its label selector.

### Common Causes

- Pod labels do not match the service selector
- Pods are not running (Pending, CrashLoopBackOff)
- Pods are in a different namespace
- Service selector is incorrect or has typos

### How to Fix

Check the service selector:
```bash
kubectl get service <name> -o yaml | grep selector
```

Check pod labels:
```bash
kubectl get pods --show-labels
```

Check endpoints:
```bash
kubectl get endpoints <name>
```

### Examples

```bash
# Check service selector
kubectl get service my-service -o yaml | grep -A5 selector
#   selector:
#     app: my-app

# Check pod labels
kubectl get pods -l app=my-app
# No resources found
# Fix: correct the service selector or add the correct label to pods
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})