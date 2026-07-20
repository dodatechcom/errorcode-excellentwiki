---
title: "[Solution] ErrImageNeverPull"
description: "Fix Kubernetes ErrImageNeverPull error. Resolve pod failures when imagePullPolicy is Never but the image does not exist locally on the node."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## ErrImageNeverPull

This error occurs when the pod has `imagePullPolicy: Never` but the specified image does not exist on the node where the pod is scheduled.

### Common Causes

- `imagePullPolicy` set to `Never` in the pod spec
- Image was pre-loaded on some nodes but not on the scheduling node
- Image was removed by image garbage collection
- Deployment uses `Never` pull policy unintentionally

### How to Fix

Check the imagePullPolicy:
```bash
kubectl get pod <pod-name> -o jsonpath='{.spec.containers[0].imagePullPolicy}'
```

Change to a pull policy that will pull the image:
```yaml
imagePullPolicy: IfNotPresent
# or
imagePullPolicy: Always
```

### Examples

```bash
# Fix pull policy
kubectl patch deployment my-app -p '{"spec":{"template":{"spec":{"containers":[{"name":"my-app","imagePullPolicy":"IfNotPresent"}]}}}}'
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})