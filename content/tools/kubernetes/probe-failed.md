---
title: "[Solution] Kubernetes Probe Failed — Liveness/Readiness probe failed"
description: "Fix Kubernetes probe failed error. Diagnose and fix liveness and readiness probe failures."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["probe-failed", "liveness", "readiness", "health", "kubernetes"]
weight: 5
---

# Kubernetes Probe Failed — Liveness/Readiness probe failed

Probes fail when the health check endpoint doesn't respond as expected. Liveness probe failures cause container restarts; readiness probe failures remove the pod from service endpoints.

## Common Causes

- Application not ready within initialDelaySeconds
- Health check endpoint path or port is incorrect
- Application is hanging or too slow to respond
- Probe timeout is too short

## How to Fix

### Check Probe Configuration

```bash
kubectl get pod <pod-name> -o yaml | grep -A 10 probe
```

### Describe Pod for Events

```bash
kubectl describe pod <pod-name>
```

### Test Health Check Endpoint

```bash
kubectl exec -it <pod-name> -- curl -f http://localhost:8080/health
```

### Increase Initial Delay

```yaml
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 60
  periodSeconds: 10
```

### Use TCP Socket Probe

```yaml
livenessProbe:
  tcpSocket:
    port: 8080
  initialDelaySeconds: 15
  periodSeconds: 10
```

### Increase Timeout

```yaml
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  timeoutSeconds: 5
  failureThreshold: 3
```

## Examples

```bash
# Example 1: Liveness probe failing
kubectl describe pod my-app
# Warning  Unhealthy  Liveness probe failed: HTTP probe failed with statuscode: 500
# Fix: check application health endpoint

# Example 2: Readiness probe timing out
kubectl describe pod my-app
# Warning  Unhealthy  Readiness probe failed: Get "http://localhost:8080/ready": context deadline exceeded
# Fix: increase timeoutSeconds or optimize endpoint

# Example 3: Wrong port
kubectl describe pod my-app
# Warning  Unhealthy  probe failed: connection refused
# Fix: verify correct port in probe configuration
```

## Related Errors

- [Pod Crash]({{< relref "/tools/kubernetes/pod-crash" >}}) — CrashLoopBackOff error
- [Health Check Failed]({{< relref "/tools/docker/healthcheck-failed" >}}) — Docker health check failing
