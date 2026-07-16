---
title: "[Solution] Kubernetes OOMKilled — Container exceeded memory limit"
description: "Fix Kubernetes OOMKilled errors. Learn why containers are killed for exceeding memory limits and how to prevent it."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["oomkilled", "memory", "resource-limits", "container", "eviction"]
weight: 5
---

# Kubernetes OOMKilled — Container exceeded memory limit

OOMKilled means the Linux kernel killed the container process because it exceeded its configured memory limit. Kubernetes reports this as the container's termination reason.

## Common Causes

- Memory limit set too low for the application's needs
- Memory leak in the application code
- Application legitimately needs more memory for large datasets
- Default memory limits not set, leading to node-level OOM

## How to Fix

### Check OOMKilled Events

```bash
kubectl describe pod <pod-name> | grep -A 5 "Last State"
# Last State: Terminated, Reason: OOMKilled, Exit Code: 137
```

### Increase Memory Limits

```yaml
resources:
  limits:
    memory: "1Gi"
  requests:
    memory: "512Mi"
```

### Monitor Memory Usage

```bash
kubectl top pod <pod-name>
kubectl top pod <pod-name> --containers
```

### Set Memory Requests and Limits

```yaml
apiVersion: apps/v1
kind: Deployment
spec:
  template:
    spec:
      containers:
        - name: app
          image: my-app:latest
          resources:
            requests:
              memory: "256Mi"
              cpu: "250m"
            limits:
              memory: "512Mi"
              cpu: "500m"
```

## Examples

```bash
# Example 1: Java app OOMKilled
kubectl describe pod java-app
# Last State: Terminated, Reason: OOMKilled
# Fix: increase memory limit to 1Gi and set JVM -Xmx flag

# Example 2: Node.js app leak
kubectl top pod node-app --containers
# NAME   CPU    MEMORY
# app    50m    490Mi (near limit)
# Fix: investigate heap usage, increase limit, or fix leak

# Example 3: Default container without limits
kubectl get pod <pod-name> -o jsonpath='{.spec.containers[*].resources}'
# Empty resources block
# Fix: always set resource limits in production
```

## Related Errors

- [Pod Evicted]({{< relref "/tools/kubernetes/pod-evicted" >}}) — pod evicted due to node memory pressure
- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crashloop-debug" >}}) — pod crashing after OOM kill
- [ImagePullBackOff]({{< relref "/tools/kubernetes/imagepullbackoff" >}}) — pod cannot pull the container image
