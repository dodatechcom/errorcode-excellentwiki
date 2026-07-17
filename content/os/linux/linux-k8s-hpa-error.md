---
title: "[Solution] k8s: HPA Error — Horizontal Pod Autoscaler Issues"
description: "Fix Kubernetes HPA (Horizontal Pod Autoscaler) errors. Resolve metrics unavailability, scaling failures, and misconfigured HPA resources."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# k8s: HPA Error — Horizontal Pod Autoscaler Issues

An HPA error occurs when the Horizontal Pod Autoscaler cannot scale pods based on metrics. The status shows:

> "FailedGetMetric" or "FailedComputeMetrics" in `kubectl describe hpa`

Or:

> "unable to fetch metrics from custom metrics API"

## What This Error Means

HPA monitors pod metrics (CPU, memory, or custom metrics) and adjusts the replica count. When the metrics server is unavailable, metric targets are unreachable, or the HPA configuration is invalid, it cannot make scaling decisions.

## Common Causes

- Metrics Server not installed or not running
- Metrics not available for the target pods
- CPU/memory requests not set on containers (required for CPU/memory HPA)
- Custom metrics API not configured
- Min/max replicas misconfigured
- Scaling policy conflicts

## How to Fix

### Check HPA Status

```bash
kubectl get hpa
kubectl describe hpa <hpa-name>
kubectl get hpa <hpa-name> -o yaml
```

### Install Metrics Server

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# For self-signed certs
kubectl patch deployment metrics-server -n kube-system --type='json' -p='[
  {"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--kubelet-insecure-tls"},
  {"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--kubelet-preferred-address-types=InternalIP"}
]'
```

### Verify Metrics Are Available

```bash
kubectl top pods
kubectl top nodes
```

### Set CPU/Memory Requests

```yaml
containers:
  - name: app
    resources:
      requests:
        cpu: "100m"
        memory: "128Mi"
      limits:
        cpu: "500m"
        memory: "512Mi"
```

### Fix HPA Configuration

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

## Related Errors

- [k8s Pod Pending]({{< relref "/os/linux/linux-k8s-pending" >}}) — Pods waiting for scheduling
- [k8s OOMKilled]({{< relref "/os/linux/linux-k8s-oom-killed" >}}) — Container memory issues
- [k8s Service Unavailable]({{< relref "/os/linux/linux-k8s-service-unavailable" >}}) — Service connectivity issues
