---
title: "[Solution] Kubernetes CrashLoopBackOff — Pod is in CrashLoopBackOff"
description: "Fix Kubernetes CrashLoopBackOff. Diagnose why pods keep crashing and restart in a loop."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

CrashLoopBackOff means a pod is repeatedly crashing and Kubernetes backs off the restart delay after each failure. The container process exits shortly after starting, and the pod never reaches a running state.

## What This Error Means

Kubernetes marks a pod as `CrashLoopBackOff` when its container exits with a non-zero exit code multiple times. After each crash, the kubelet waits an exponentially increasing delay before restarting (10s, 20s, 40s, up to 5 minutes). This state indicates a fundamental application issue rather than a transient failure.

## Common Causes

- Application crashes on startup due to a bug or misconfiguration
- Missing environment variables or configuration files
- Insufficient memory or CPU resources causing OOMKilled
- Liveness probe failing because the app is not ready in time
- Port conflicts within the container
- Missing dependencies (database, external services)

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

### Check Exit Codes

```bash
kubectl get pod <pod-name> -o jsonpath='{.status.containerStatuses[*].lastState.terminated.exitCode}'
```

## Related Errors

- [Kubernetes OOMKilled]({{< relref "/tools/kubernetes/k8s-oom-killed-v2" >}}) — container exceeded memory
- [Kubernetes ImagePullBackOff]({{< relref "/tools/kubernetes/k8s-image-pull-v2" >}}) — image pull failed
- [Kubernetes Pod Pending]({{< relref "/tools/kubernetes/k8s-pending-v2" >}}) — pod stuck in Pending
