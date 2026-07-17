---
title: "[Solution] Kubernetes OOMKilled — container exceeded memory"
description: "Fix Kubernetes OOMKilled errors. Resolve container out-of-memory kills."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["oomkilled", "memory", "limit", "container", "kubernetes"]
weight: 5
---

OOMKilled means a container was terminated by the Linux kernel because it exceeded its memory limit. The pod will restart based on the restart policy.

## Common Causes

- Memory limit set too low for the application
- Memory leak causing gradual memory increase
- Application requires more memory during specific operations
- JVM or runtime not configured to respect container memory limits
- Multiple processes in container competing for memory

## How to Fix

### Check Pod Status

```bash
kubectl get pod <pod-name> -o jsonpath='{.status.containerStatuses[*].lastState}'
```

### Increase Memory Limit

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
```

### Configure JVM for Container

```bash
# In Dockerfile or env
JAVA_OPTS: "-XX:MaxRAMPercentage=75.0"
```

### Check Node Memory

```bash
kubectl top nodes
```

## Examples

```bash
# Example 1: Check OOMKilled status
kubectl describe pod my-pod
# Last State: Terminated, Reason: OOMKilled, Exit Code: 137

# Example 2: Monitor memory
kubectl top pod my-pod --containers
# NAME   CPU    MEMORY
# app    50m    950Mi / 1Gi
# Fix: increase memory limit to 2Gi
```

## Related Errors

- [Kubernetes CrashLoopBackOff]({{< relref "/tools/kubernetes/k8s-crashloop" >}}) — pod keeps crashing
- [Docker Container OOM Killed]({{< relref "/tools/docker/docker-out-of-memory" >}}) — container OOM killed
