---
title: "[Solution] QoS class eviction (BestEffort/Burstable)"
description: "Fix Kubernetes QoS class eviction. Resolve pod eviction priority based on Quality of Service classes."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## QoS Class Eviction

Kubernetes uses Quality of Service (QoS) classes to determine pod eviction priority under resource pressure.

### QoS Classes (lowest to highest eviction priority)

1. BestEffort (no requests or limits set)
2. Burstable (requests < limits)
3. Guaranteed (requests == limits for all resources)

### Common Causes

- BestEffort pods are evicted first under node pressure
- Burstable pods evicted next if more resources needed
- Guaranteed pods are evicted last (only if absolutely necessary)
- OOM score is higher for BestEffort pods
- No resource limits set on critical pods

### How to Fix

Set Guaranteed QoS for critical workloads:
```yaml
resources:
  requests:
    memory: 512Mi
    cpu: 500m
  limits:
    memory: 512Mi
    cpu: 500m
```

Check pod QoS class:
```bash
kubectl get pod <name> -o jsonpath='{.status.qosClass}'
```

### Examples

```bash
# Check pod QoS class
kubectl get pod my-app -o jsonpath='{.status.qosClass}'
# Burstable

# Upgrade to Guaranteed
kubectl set resources deployment/my-app --requests=cpu=500m,memory=512Mi --limits=cpu=500m,memory=512Mi

# Check QoS class again
kubectl get pod my-app-xxx -o jsonpath='{.status.qosClass}'
# Guaranteed
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})