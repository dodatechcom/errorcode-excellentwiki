---
title: "[Solution] Kubernetes HPA Error — failed to get metric"
description: "Fix Kubernetes HorizontalPodAutoscaler errors. Resolve HPA metric collection failures."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["hpa", "autoscaler", "metrics", "scaling", "kubernetes"]
weight: 5
---

An HPA error occurs when the HorizontalPodAutoscaler cannot collect metrics to make scaling decisions. This prevents automatic scaling of pods.

## Common Causes

- Metrics server is not installed or not running
- Metric name or target is incorrect in HPA spec
- Custom metrics API is not available
- Pod does not expose the required metrics endpoint
- HPA target references a non-existent resource

## How to Fix

### Check Metrics Server

```bash
kubectl get deployment metrics-server -n kube-system
```

### Verify HPA Status

```bash
kubectl get hpa <name>
kubectl describe hpa <name>
```

### Check HPA Events

```bash
kubectl describe hpa <hpa-name>
```

### Install Metrics Server

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

### Test Metrics API

```bash
kubectl top nodes
kubectl top pods
```

## Examples

```bash
# Example 1: Metrics server not installed
kubectl get hpa my-hpa
# TARGETS   <unknown>/80%
# Fix: install metrics-server

# Example 2: Wrong metric name
kubectl describe hpa my-hpa
# Warning: failed to get cpu utilization
# Fix: verify metric name in HPA spec
```

## Related Errors

- [Kubernetes Node NotReady]({{< relref "/tools/kubernetes/k8s-node-not-ready" >}}) — node not ready
- [Kubernetes CrashLoopBackOff]({{< relref "/tools/kubernetes/k8s-crashloop" >}}) — pod keeps crashing
