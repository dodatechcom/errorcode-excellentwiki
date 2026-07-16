---
title: "[Solution] Kubernetes CrashLoopBackOff — Pod X is in CrashLoopBackOff"
description: "Fix Kubernetes CrashLoopBackOff status. Diagnose why pods keep crashing and how to recover."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["crashloopbackoff", "pod", "restart", "crash", "container"]
weight: 5
---

# Kubernetes CrashLoopBackOff — Pod X is in CrashLoopBackOff

CrashLoopBackOff means a pod is repeatedly crashing and restarting. Kubernetes is backing off the restart delay after each failure, indicating the container process exits shortly after starting.

## Common Causes

- Application crashes on startup due to a bug or misconfiguration
- Missing environment variables or configuration files
- Insufficient memory or CPU resources causing OOMKilled
- Liveness probe failing because the app is not ready in time

## How to Fix

### Check Pod Logs

```bash
kubectl logs <pod-name>
kubectl logs <pod-name> --previous
```

### Describe the Pod for Events

```bash
kubectl describe pod <pod-name>
```

### Check Resource Limits

```bash
kubectl get pod <pod-name> -o yaml | grep -A 5 resources
```

### Increase Memory Limits

```yaml
resources:
  limits:
    memory: "512Mi"
  requests:
    memory: "256Mi"
```

### Fix Liveness Probe Timing

```yaml
livenessProbe:
  initialDelaySeconds: 30
  periodSeconds: 10
```

## Examples

```bash
# Example 1: Check why pod is crashing
kubectl logs my-app-pod
# Error: cannot connect to database at db:5432
# Fix: ensure the database service is running

# Example 2: OOMKilled
kubectl describe pod my-app-pod
# Last State: Terminated, Reason: OOMKilled
# Fix: increase memory limits in deployment spec

# Example 3: Missing environment variable
kubectl logs my-app-pod
# Error: DATABASE_URL not set
# Fix: add DATABASE_URL to deployment env vars
```

## Related Errors

- [Image Pull Error]({{< relref "/tools/kubernetes/image-pull" >}}) — pod cannot pull the container image
- [Probe Failed]({{< relref "/tools/kubernetes/probe-failed" >}}) — liveness/readiness probe failed
