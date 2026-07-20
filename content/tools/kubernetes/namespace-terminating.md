---
title: "[Solution] Namespace Terminating"
description: "Fix Kubernetes 'namespace is terminating' error. Resolve resource creation failures in a namespace that is being deleted."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Namespace Terminating

`Error: namespace "<namespace>" is terminating`

This error occurs when you try to create resources in a namespace that is in the process of being deleted.

### Common Causes

- Running a kubectl delete namespace that hasn't completed
- Trying to recreate a namespace before it's fully removed
- Namespace stuck in Terminating state due to finalizers

### How to Fix

Wait for the namespace to finish deleting:
```bash
kubectl get ns <namespace>
```

If stuck, remove finalizers:
```bash
kubectl get namespace <name> -o json | jq '.spec.finalizers=[]' | kubectl replace --raw /api/v1/namespaces/<name>/finalize -f -
```

### Examples

```bash
# Check namespace status
kubectl get ns my-ns
# my-ns   Terminating

# Remove finalizers to force delete
kubectl get namespace my-ns -o json | jq '.spec.finalizers=[]' | kubectl replace --raw /api/v1/namespaces/my-ns/finalize -f -
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})