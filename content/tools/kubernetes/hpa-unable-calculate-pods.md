---
title: "[Solution] HPA unable to calculate pod count"
description: "Fix Kubernetes HPA 'unable to calculate' pod count error. Resolve HPA failures when pods lack resource requests."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## HPA Unable to Calculate Pod Count

`unable to calculate pod count: missing request for <resource>`

This error occurs when the HPA cannot calculate the desired number of pods because the target pods do not have resource requests defined.

### Common Causes

- Pods in the target do not have CPU or memory requests set
- HPA is using a custom metrics query that returns no data
- Some pods in the replica set have different resource configurations

### How to Fix

Add resource requests to pods:
```yaml
resources:
  requests:
    cpu: 200m
    memory: 256Mi
```

### Examples

```bash
# Check if pods have resource requests
kubectl get pod <pod-name> -o jsonpath='{.spec.containers[0].resources.requests}'
# {cpu: 200m memory: 256Mi}

# Add requests to deployment
kubectl set resources deployment/my-app --requests=cpu=200m,memory=256Mi
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})