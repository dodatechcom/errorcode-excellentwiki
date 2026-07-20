---
title: "[Solution] VPA recommendation failed"
description: "Fix Kubernetes Vertical Pod Autoscaler (VPA) recommendation failures. Resolve VPA issues when resource recommendations cannot be calculated."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## VPA Recommendation Failed

This error occurs when the Vertical Pod Autoscaler cannot generate resource recommendations for a pod.

### Common Causes

- Metrics Server is not installed
- Pod has not been running long enough for metrics collection (minimum 8 hours for default mode)
- VPA recommender pod is not running
- VPA admission controller is not installed
- Pod resource requests are not set

### How to Fix

Check VPA components:
```bash
kubectl get pods -n kube-system | grep vpa
```

Check VPA status:
```bash
kubectl describe vpa <name>
```

Update mode to auto or recreate:
```yaml
spec:
  updateMode: Auto
```

### Examples

```bash
# Check VPA status
kubectl describe vpa my-app-vpa
#  Conditions:
#    Type    Status  Reason
#    Update  False   NoPodHistory

# Install VPA
git clone https://github.com/kubernetes/autoscaler.git
kubectl apply -k autoscaler/vertical-pod-autoscaler/deploy/
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})