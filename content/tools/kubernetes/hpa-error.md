---
title: "[Solution] Kubernetes HPA failed to get metrics"
description: "Fix Kubernetes HorizontalPodAutoscaler errors. Resolve failed metric collection and autoscaling issues."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["hpa", "autoscaler", "metrics", "scaling", "horizontal"]
weight: 5
---

# Kubernetes HPA — failed to get metrics

The HorizontalPodAutoscaler (HPA) fails when it cannot retrieve the metrics needed to make scaling decisions. This leaves the deployment stuck at its current replica count regardless of load.

## Common Causes

- Metrics Server not installed or not running
- Incorrect metric names or API endpoints in HPA spec
- RBAC permissions preventing HPA from reading metrics
- Custom metrics adapter not configured

## How to Fix

### Check HPA Status

```bash
kubectl get hpa
kubectl describe hpa <hpa-name>
```

### Verify Metrics Server is Running

```bash
kubectl get deployment metrics-server -n kube-system
kubectl top nodes
kubectl top pods
```

### Install Metrics Server

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

### Fix HPA Metric Configuration

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-app
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

### Check RBAC Permissions

```bash
kubectl describe clusterrolebinding metrics-server
```

## Examples

```bash
# Example 1: HPA shows unknown metrics
kubectl get hpa
# NAME     REFERENCE          TARGETS   MINPODS   MAXPODS   REPLICAS
# my-app   Deployment/my-app  <unknown>/70%   2         10        2
# Fix: install or restart metrics-server

# Example 2: Custom metric not found
kubectl describe hpa my-app
# Warning: failed to get cpu utilization: unable to fetch metrics
# Fix: verify metric name matches what your app exposes

# Example 3: Insufficient RBAC
kubectl get hpa my-app -o yaml | grep -A 10 events
# Warning: Unauthorized
# Fix: grant metrics-server permission to read pod metrics
```

## Related Errors

- [Pod Evicted]({{< relref "/tools/kubernetes/pod-evicted" >}}) — pod evicted due to resource pressure
- [OOMKilled]({{< relref "/tools/kubernetes/oomkilled" >}}) — container exceeded memory limit
- [Ingress Error]({{< relref "/tools/kubernetes/ingress-error" >}}) — no backend available for traffic
