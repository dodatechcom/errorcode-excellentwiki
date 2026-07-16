---
title: "[Solution] Kubernetes CrashLoopBackOff — How to debug with kubectl logs"
description: "Debug Kubernetes CrashLoopBackOff errors using kubectl logs. Step-by-step guide to identify why pods keep crashing."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["crashloopbackoff", "debugging", "kubectl-logs", "pod", "container"]
weight: 5
---

# Kubernetes CrashLoopBackOff — How to debug with kubectl logs

CrashLoopBackOff means a container is repeatedly crashing and restarting. The pod status shows CrashLoopBackOff while Kubernetes backs off the restart delay between each failure. Debugging with `kubectl logs` reveals the root cause.

## Common Causes

- Application throws an unhandled exception on startup
- Missing environment variables, config files, or secrets
- Liveness probe fails before the application is ready
- Insufficient resources causing OOMKilled restarts

## How to Fix

### Check Current Pod Status

```bash
kubectl get pods --field-selector=status.phase!=Running
kubectl describe pod <pod-name> | grep -A 10 "Last State"
```

### View Current and Previous Logs

```bash
# Current logs
kubectl logs <pod-name>

# Previous crashed container logs
kubectl logs <pod-name> --previous

# Logs from a specific container in a multi-container pod
kubectl logs <pod-name> -c <container-name> --previous
```

### Check Pod Events

```bash
kubectl describe pod <pod-name> | grep -A 20 Events
```

### Set Startup Probe for Slow Apps

```yaml
startupProbe:
  httpGet:
    path: /healthz
    port: 8080
  failureThreshold: 30
  periodSeconds: 10
```

### Run a Debug Container

```bash
kubectl debug pod/<pod-name> -it --image=busybox -- sh
```

## Examples

```bash
# Example 1: Application crash
kubectl logs my-app-pod --previous
# Output: Error: Cannot find module '/app/config.json'
# Fix: mount the config file or set CONFIG_PATH env var

# Example 2: Database connection failure
kubectl logs my-app-pod --previous
# Output: Connection refused: db-service:5432
# Fix: ensure the database service exists and is running

# Example 3: Port conflict
kubectl logs my-app-pod --previous
# Output: Error: listen EADDRINUSE :::8080
# Fix: change the application port or check for duplicate containers
```

## Related Errors

- [ImagePullBackOff]({{< relref "/tools/kubernetes/imagepullbackoff" >}}) — pod cannot pull the container image
- [OOMKilled]({{< relref "/tools/kubernetes/oomkilled" >}}) — container exceeded memory limit
- [Pod Evicted]({{< relref "/tools/kubernetes/pod-evicted" >}}) — pod evicted due to node pressure
