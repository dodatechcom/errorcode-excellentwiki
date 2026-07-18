---
title: "[Solution] Kubectl CrashLoopBackOff Error — How to Fix"
description: "Fix kubectl CrashLoopBackOff errors by checking application logs, diagnosing startup failures, fixing resource limits, resolving dependency connectivity, and adjusting liveness probes."
tools: ["kubectl"]
error-types: ["crash-loop-error"]
severities: ["error"]
weight: 5
comments: true
---

A `CrashLoopBackOff` error occurs when a container in a pod starts, crashes, and is repeatedly restarted by Kubernetes. The kubelet detects the crash and restarts the container with exponential backoff, but the cycle continues indefinitely.

## What This Error Means

Kubernetes automatically restarts containers that exit with a non-zero exit code. When a container keeps crashing after restart, Kubernetes increases the delay between restarts (backoff). The pod status shows `CrashLoopBackOff` to indicate the container is stuck in a crash-restart loop.

This is different from `ImagePullBackOff` (image cannot be pulled) or `ErrImagePull` (registry issues). CrashLoopBackOff means the image was pulled successfully, but the application inside the container fails to start or crashes immediately.

## Why It Happens

- Application startup fails due to missing environment variables or config files
- The application crashes because of a code bug or unhandled exception
- Resource limits are too low (out of memory, CPU throttling)
- The application cannot connect to required services (database, API)
- Liveness or readiness probes fail, causing Kubernetes to kill and restart
- The command or entrypoint specified in the pod spec is incorrect
- Configuration files or secrets are not mounted correctly
- The application exits because it is designed as a batch job but deployed as a long-running service

## Common Error Messages

```
CrashLoopBackOff: pod "my-pod-5d4f8b6c7-abc12" is crashing
# or
Back-off restarting failed container
# or
container "my-container" has exited with code 1
# or
Error: failed to start container: context deadline exceeded
```

## How to Fix It

### 1. Check Container Logs

```bash
# View the logs of the crashed container
kubectl logs my-pod-5d4f8b6c7-abc12

# View logs from the previous (crashed) instance
kubectl logs my-pod-5d4f8b6c7-abc12 --previous

# Stream logs while watching the crash
kubectl logs -f my-pod-5d4f8b6c7-abc12

# If the pod has multiple containers, specify the container name
kubectl logs my-pod-5d4f8b6c7-abc12 -c my-container
```

### 2. Describe the Pod for Events

```bash
# Detailed pod information including exit codes and events
kubectl describe pod my-pod-5d4f8b6c7-abc12

# Focus on the container status section
kubectl get pod my-pod-5d4f8b6c7-abc12 -o jsonpath='{.status.containerStatuses[0].state}' | jq .
```

### 3. Check Exit Codes

```bash
# Exit code 0 = success (unexpected for long-running containers)
# Exit code 1 = general error (application crash)
# Exit code 137 = SIGKILL (OOM killed)
# Exit code 139 = SIGSEGV (segmentation fault)
# Exit code 143 = SIGTERM (graceful shutdown)

kubectl get pod my-pod -o jsonpath='{.status.containerStatuses[0].state.waiting.reason}'
# Should be "CrashLoopBackOff"

kubectl get pod my-pod -o jsonpath='{.status.containerStatuses[0].lastState.terminated.exitCode}'
```

### 4. Fix Missing Configuration

```python
# Example: Python app crashes if DATABASE_URL is missing
import os

# Debug by checking all required env vars at startup
required_vars = ['DATABASE_URL', 'REDIS_URL', 'SECRET_KEY']
for var in required_vars:
    if var not in os.environ:
        print(f"CRITICAL: Missing environment variable: {var}")
        # Don't exit, provide a helpful default or crash with context
```

### 5. Adjust Resource Limits

```bash
# Check current resource limits
kubectl get pod my-pod -o jsonpath='{.spec.containers[0].resources}'

# If limits are too low, update the deployment
kubectl set resources deployment/my-app \
    --limits=cpu=500m,memory=512Mi \
    --requests=cpu=250m,memory=256Mi
```

```yaml
# Example deployment with reasonable resource limits
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  template:
    spec:
      containers:
      - name: my-app
        image: my-app:latest
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
```

### 6. Fix Liveness and Readiness Probes

```bash
# If probes fail, Kubernetes restarts the container
# Check probe configuration
kubectl get pod my-pod -o yaml | grep -A 15 "livenessProbe\|readinessProbe"

# Temporarily disable probes for debugging
kubectl edit deployment my-app
# Remove livenessProbe section, save, and see if the pod stays up
```

```yaml
# Example of correct probe configuration
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 30  # Give app time to start
  periodSeconds: 10
  timeoutSeconds: 5
  failureThreshold: 3

readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

### 7. Execute Commands in a Temporary Debug Container

```bash
# Run a debug container sharing the same environment
kubectl debug my-pod-5d4f8b6c7-abc12 -it --image=busybox --copy-to=my-pod-debug

# Or create a standalone pod with the same image
kubectl run debug --image=my-app:latest --rm -it --restart=Never -- /bin/sh

# Test commands manually
# Check if config files exist
# Test environment variables
# Test network connectivity
```

### 8. Fix Entrypoint Issues

```bash
# Check the command and args in the pod spec
kubectl get pod my-pod -o yaml | grep -A 5 "command:\|args:"

# Override entrypoint for debugging
kubectl run debug --image=my-app:latest --rm -it --restart=Never -- /bin/sh

# If the entrypoint is wrong, update the deployment:
# spec.template.spec.containers[0].command: ["/usr/local/bin/my-app"]
# spec.template.spec.containers[0].args: ["--config", "/etc/config/app.yaml"]
```

## Common Scenarios

### Application Crashes Due to Missing Database

A Node.js application starts, tries to connect to PostgreSQL, fails because `DATABASE_URL` is not set, and exits with code 1. Kubernetes restarts it, and the cycle repeats. Check `kubectl logs` to see the connection error, then add the missing config var or ConfigMap.

### OOM Killed Container

A Java application requires 1GB of heap memory but the pod has a 512MB memory limit. The Java process hits the limit, gets OOM killed (exit code 137), and Kubernetes restarts it. Increase the memory limit to 1GB or reduce the JVM heap size with `-Xmx`.

### Probes Fail Because Initialization Takes Too Long

A Rails application takes 45 seconds to start, but the liveness probe starts checking after 5 seconds with `initialDelaySeconds: 5`. The probe fails, Kubernetes kills the container, and it restarts into the same failure. Increase `initialDelaySeconds` to 60 to give the application time to initialize.

## Prevent It

- Set `initialDelaySeconds` on probes to accommodate application startup time
- Use startup probes for applications with variable initialization times
- Configure appropriate memory and CPU requests/limits based on application profiling
- Add comprehensive startup logging to diagnose initialization failures
- Implement health check endpoints that verify dependencies before reporting healthy
- Use `terminationMessagePath` to capture crash output
- Test container startup locally with the same configuration as Kubernetes
- Set up pod disruption budgets to maintain availability during rolling updates

## Related Pages

- [Kubectl Image Pull Backoff Error](/tools/kubectl/kubectl-image-pull-error)
- [Kubectl Pod Logs Error](/tools/kubectl/kubectl-logs-error)
- [Kubectl ConfigMap Mount Error](/tools/kubectl/kubectl-configmap-error)
