---
title: "[Solution] Orphaned Kubernetes resources"
description: "Fix orphaned Kubernetes resources. Resolve issues when resources remain after their parent controller is deleted."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Orphaned Resources

Orphaned resources occur when Kubernetes resources remain after the controller that created them is deleted or when ownerReferences point to non-existent resources.

### Common Causes

- Deployment deleted but ReplicaSets remain (without cascade deletion)
- Namespace deleted but resources remain due to finalizer
- CRD deleted but custom resources remain
- Owner reference to a resource that no longer exists
- Foreground deletion fails (child resources block deletion)
- Background deletion leaves some resources

### How to Fix

Find orphaned resources:
```bash
kubectl get all --all-namespaces | grep -v "Running\|ready"
```

Clean up manually:
```bash
kubectl delete replicaset <name> --cascade=orphan
```

Delete with cascade:
```bash
kubectl delete deployment <name> --cascade=foreground
```

### Examples

```bash
# Find ReplicaSets not owned by any Deployment
kubectl get replicaset --all-namespaces -o json | jq '.items[] | select(.metadata.ownerReferences == null) | .metadata.name'

# Delete orphaned resources
kubectl delete rs <orphaned-rs>
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})