---
title: "[Solution] k8s: CrashLoopBackOff — Pod Keeps Restarting"
description: "Fix Kubernetes CrashLoopBackOff status. Resolve pod restart loops caused by application crashes, misconfigurations, and resource limits."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# k8s: CrashLoopBackOff — Pod Keeps Restarting

CrashLoopBackOff means a Kubernetes pod is repeatedly crashing and restarting. The pod status shows:

> "CrashLoopBackOff" in `kubectl get pods`

Or:

> "Back-off restarting failed container"

## What This Error Means

Kubernetes restarts a container that exits with a non-zero exit code. If the container crashes more than `backoffLimit` times (default: 5), the pod enters `CrashLoopBackOff` state with exponential backoff delays between restarts. The container starts, crashes, and Kubernetes waits longer each time before restarting.

## Common Causes

- Application bug causing immediate crash on startup
- Misconfigured environment variables or command/args
- Missing or invalid configuration file (ConfigMap, Secret mount)
- Application cannot connect to a required dependency
- Health probe failing before application is ready
- Insufficient memory (OOMKilled)
- Read-only filesystem where app writes data

## How to Fix

### Check Container Logs

```bash
# Logs from current container
kubectl logs <pod-name>

# Logs from previous (crashed) container
kubectl logs <pod-name> --previous

# Logs with timestamps
kubectl logs <pod-name> --timestamps

# Follow logs
kubectl logs -f <pod-name>
```

### Describe the Pod

```bash
kubectl describe pod <pod-name>
```

Look at the `Last State` section for exit code, reason, and message.

### Common Exit Codes

| Exit Code | Meaning |
|-----------|---------|
| 0 | Normal exit (but container didn't stay running) |
| 1 | Application error |
| 126 | Permission denied (not executable) |
| 127 | Command not found |
| 137 | OOMKilled (SIGKILL) |
| 139 | Segmentation fault (SIGSEGV) |
| 143 | Terminated by SIGTERM |

### Fix Configuration Issues

```bash
# Check environment variables
kubectl exec -it <pod-name> -- env

# Check mounted volumes
kubectl exec -it <pod-name> -- ls -la /mount/path

# Verify ConfigMap exists
kubectl get configmap <name>
kubectl describe configmap <name>
```

### Adjust Resource Limits

```yaml
resources:
  requests:
    memory: "256Mi"
    cpu: "250m"
  limits:
    memory: "512Mi"
    cpu: "500m"
```

### Add Startup Probe

```yaml
startupProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 10
  periodSeconds: 5
  failureThreshold: 30
```

## Related Errors

- [k8s Pod Pending]({{< relref "/os/linux/linux-k8s-pending" >}}) — Pod stuck in Pending state
- [k8s OOMKilled]({{< relref "/os/linux/linux-k8s-oom-killed" >}}) — Container killed by OOM
- [k8s Pod ImagePullBackOff]({{< relref "/os/linux/linux-k8s-image-pull" >}}) — Image pull failures
