---
title: "[Solution] Kubernetes HPA — metrics not available"
description: "Fix Kubernetes HPA metrics not available. Resolve HorizontalPodAutoscaler scaling failures."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An HPA error means the HorizontalPodAutoscaler cannot retrieve metrics to make scaling decisions. The HPA remains unable to adjust pod replicas based on resource utilization.

## What This Error Means

The HPA controller queries the Metrics Server (or custom metrics API) to determine current resource utilization. When metrics are unavailable, the HPA logs `unable to fetch metrics` and cannot calculate desired replica count. The HPA's current and desired replica counts remain unknown, and the target's `currentMetrics` will show `<unknown>`. Scaling is completely blocked until metrics become available.

## Common Causes

- Metrics Server is not installed or not running
- Metrics Server is unreachable from the API server
- Target pods do not expose metrics endpoints
- Custom metrics API server is not configured
- Resource requests not set on target pods
- Metrics Server RBAC permissions are insufficient

## How to Fix

### Check HPA Status

```bash
kubectl get hpa <hpa-name>
kubectl describe hpa <hpa-name>
```

### Verify Metrics Server

```bash
kubectl get deployment metrics-server -n kube-system
kubectl logs -n kube-system deployment/metrics-server
```

### Install Metrics Server

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

### Check HPA Events

```bash
kubectl get events --field-selector involvedObject.name=<hpa-name>
```

### Ensure Resource Requests Are Set

```yaml
resources:
  requests:
    cpu: "250m"
    memory: "256Mi"
  limits:
    cpu: "500m"
    memory: "512Mi"
```

### Test Metrics Directly

```bash
kubectl top pods
kubectl top nodes
```

### Configure HPA with Correct Target

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-hpa
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

- [Kubernetes Node NotReady]({{< relref "/tools/kubernetes/k8s-node-not-ready-v2" >}}) — node unhealthy
- [Kubernetes API Server Error]({{< relref "/tools/kubernetes/k8s-api-server-error-v2" >}}) — API server timeout
- [Kubernetes Pod Pending]({{< relref "/tools/kubernetes/k8s-pending-v2" >}}) — insufficient resources
