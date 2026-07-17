---
title: "[Solution] Linux Kubernetes Pod Crashing — Exit Code 1"
description: "Fix Linux Kubernetes pod crashing with exit code 1. Diagnose container crashes, check logs, and resolve pod restart loops."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: Kubernetes — pod crashing with exit code 1

The Kubernetes `ExitCode 1` or `CrashLoopBackOff` error means the container process exited with a non-zero status code (1 = general application error). The kubelet restarts the container automatically, but if it keeps crashing, the pod enters a `CrashLoopBackOff` state with increasing backoff delays.

## What This Error Means

Exit code 1 indicates the application inside the container encountered a fatal error and terminated. Kubernetes treats any non-zero exit as a failure and restarts the container according to the `restartPolicy`. After repeated failures, the backoff interval increases from 10s to a maximum of 5 minutes. Common causes include configuration errors, missing environment variables, missing dependencies, or application bugs.

## Common Causes

- Application configuration error (missing env vars, wrong config path)
- Missing or inaccessible secrets/configmaps
- Application cannot reach required services (database, API)
- Image pulled is incorrect or corrupted
- Insufficient resources (OOMKill shows exit code 137, not 1)
- Liveness probe failing and triggering container restart
- Code bug causing unhandled exception or assertion failure

## How to Fix

### 1. Check Pod Status and Logs

```bash
# View pod status
kubectl get pods -o wide

# View detailed pod status
kubectl describe pod <pod-name>

# View container logs (current and previous crash)
kubectl logs <pod-name>
kubectl logs <pod-name> --previous

# View logs for a specific container
kubectl logs <pod-name> -c <container-name>
```

### 2. Check Events for Clues

```bash
# View pod events
kubectl describe pod <pod-name> | grep -A20 'Events:'

# View namespace events
kubectl get events -n <namespace> --sort-by='.lastTimestamp'
```

### 3. Debug with Interactive Shell

```bash
# If the container starts briefly before crashing
kubectl exec -it <pod-name> -- /bin/sh

# Or run a debug container
kubectl debug <pod-name> -it --image=busybox

# Check environment variables
env | sort

# Check if required files exist
ls -la /app/config/
cat /app/config/settings.yaml
```

### 4. Fix Environment Variables and Secrets

```bash
# Verify env vars are set
kubectl get pod <pod-name> -o jsonpath='{.spec.containers[0].env}'

# Check if secrets exist
kubectl get secret <secret-name> -n <namespace>

# Check if configmaps exist
kubectl get configmap <configmap-name> -n <namespace>
```

### 5. Fix Resource Issues

```bash
# Check if pod has resource limits
kubectl get pod <pod-name> -o yaml | grep -A5 resources

# View node resource usage
kubectl top nodes
kubectl top pods

# Check for OOMKilled (exit code 137)
kubectl get pod <pod-name> -o jsonpath='{.status.containerStatuses[*].lastState.terminated.reason}'
```

### 6. Fix Liveness Probe

```bash
# Check liveness probe configuration
kubectl get pod <pod-name> -o yaml | grep -A10 livenessProbe

# If the probe is too aggressive, increase initial delay
# Edit deployment
kubectl edit deployment <deployment-name>

# Or increase timeout
# livenessProbe:
#   httpGet:
#     path: /healthz
#     port: 8080
#   initialDelaySeconds: 30
#   periodSeconds: 10
```

### 7. Roll Back to Previous Version

```bash
# Undo the last rollout
kubectl rollout undo deployment/<deployment-name>

# View rollout history
kubectl rollout history deployment/<deployment-name>

# Check status of rollout
kubectl rollout status deployment/<deployment-name>
```

## Examples

```bash
$ kubectl get pods
NAME                    READY   STATUS             RESTARTS      AGE
myapp-7f8b4c6d9-x2k4z   0/1     CrashLoopBackOff   5 (20s ago)   2m

$ kubectl logs myapp-7f8b4c6d9-x2k4z --previous
Error: Cannot find module '/app/config/database.yml'
    at Function.Module._resolveFilename (internal/modules/cjs/loader.js:815:15)

$ kubectl get configmap myapp-config
Error from server (NotFound): configmaps "myapp-config" not found

$ kubectl create configmap myapp-config --from-file=config/database.yml
$ kubectl rollout restart deployment/myapp
$ kubectl get pods
NAME                    READY   STATUS    RESTARTS   AGE
myapp-7f8b4c6d9-m3j5n   1/1     Running   0          30s
```

## Related Errors

- [K8s OOM killed]({{< relref "/os/linux/linux-k8s-oom-killed" >}}) — Out of memory kills
- [K8s image pull error]({{< relref "/os/linux/linux-k8s-image-pull" >}}) — Image pull failures
- [K8s pending pod]({{< relref "/os/linux/linux-k8s-pending" >}}) — Pod stuck in pending state
