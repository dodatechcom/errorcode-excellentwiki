---
title: "[Solution] HPA failed to get metrics"
description: "Fix Kubernetes HPA 'failed to get metrics' error. Resolve HorizontalPodAutoscaler failures when metrics are unavailable."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## HPA Failed to Get Metrics

`Failed to get metrics: failed to get <metric> metric`

This error occurs when the HorizontalPodAutoscaler cannot retrieve the metrics needed for scaling decisions.

### Common Causes

- Metrics Server not installed or not running
- Resource metrics not available for the target pods
- Custom metrics API endpoint not available
- Metrics Server has insufficient permissions

### How to Fix

Check Metrics Server:
```bash
kubectl get pods -n kube-system -l k8s-app=metrics-server
```

Get resource metrics:
```bash
kubectl top pods
kubectl top nodes
```

Check HPA status:
```bash
kubectl describe hpa <name>
```

Install Metrics Server:
```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

### Examples

```bash
# Check metrics availability
kubectl top nodes
# error: Metrics API not available

# Install Metrics Server
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# Check HPA details
kubectl describe hpa my-hpa
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})