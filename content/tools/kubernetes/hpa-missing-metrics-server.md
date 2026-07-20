---
title: "[Solution] HPA missing Metrics Server"
description: "Fix Kubernetes HPA 'Metrics Server not available' error. Resolve HPA failures when resource metrics API is not installed."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## HPA Missing Metrics Server

`the metrics server is not configured to handle the request`

This error occurs when the HorizontalPodAutoscaler cannot query resource metrics because the Metrics Server is not installed.

### Common Causes

- Metrics Server is not deployed in the cluster
- Metrics Server is not reachable via the API
- Metrics API endpoint is disabled
- Metrics Server is in CrashLoopBackOff
- Aggregation layer is not configured

### How to Fix

Install Metrics Server:
```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

Check Metrics Server availability:
```bash
kubectl get apiservice v1beta1.metrics.k8s.io
kubectl get --raw /apis/metrics.k8s.io/v1beta1
```

### Examples

```bash
# Check if Metrics API is available
kubectl get --raw /apis/metrics.k8s.io/v1beta1 | jq .
# Error: the server could not handle the request

# Install Metrics Server
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})