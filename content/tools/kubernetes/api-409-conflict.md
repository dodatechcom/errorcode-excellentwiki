---
title: "[Solution] API 409 Conflict"
description: "Fix Kubernetes API 409 Conflict error. Resolve resource update conflicts when the object has been modified by another process."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## API 409 Conflict

`Conflict (409): Operation cannot be fulfilled on <resource> "<name>": the object has been modified`

This error occurs when you try to update a Kubernetes resource that has been modified since you last read it. Kubernetes uses optimistic concurrency to prevent conflicting writes.

### Common Causes

- Multiple controllers or users updating the same resource
- Automation tools (CI/CD) making concurrent updates
- Using kubectl edit or kubectl patch on a stale version

### How to Fix

Re-read the resource and re-apply the change:
```bash
kubectl get <resource> <name> -o yaml | kubectl replace -f -
```

Use server-side apply:
```bash
kubectl apply --server-side --force-conflicts -f resource.yaml
```

### Examples

```bash
# Re-read and re-apply
kubectl get deployment my-app -o yaml | kubectl replace -f -
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})