---
title: "[Solution] Kubectl CrashLoopBackOff — Fix Pod Crash Loop"
description: "Fix kubectl Pod CrashLoopBackOff errors. Diagnose application crashes, OOM kills, and configuration issues causing pod restarts."
---

## What This Error Means

CrashLoopBackOff means a pod is repeatedly starting and crashing. Kubernetes restarts the pod, but it fails again shortly after starting, creating a loop of crash-restart-crash cycles.

A typical output:

```
NAME                    READY   STATUS             RESTARTS      AGE
web-app-7f8b6c5d4-abc   0/1     CrashLoopBackOff   5 (30s ago)   3m
```

## Why It Happens

CrashLoopBackOff is caused by:

- **Application startup failure**: The application process crashes immediately after starting.
- **Out of memory (OOMKilled)**: The container exceeds its memory limit.
- **Missing configuration**: Required environment variables or config files are absent.
- **Invalid command or arguments**: The container runs an incorrect entrypoint or arguments.
- **Dependency failures**: The app depends on databases or services that are unavailable.
- **Port conflicts**: The application tries to bind to a port already in use.
- **Readiness/liveness probe failures**: Probes detect the app is unhealthy and kill it.

## How to Fix It

**Step 1: Check pod logs**

```bash
kubectl logs web-app-7f8b6c5d4-abc --previous
```

**Step 2: Describe the pod for events**

```bash
kubectl describe pod web-app-7f8b6c5d4-abc
```

**Step 3: Check resource limits**

```yaml
resources:
  requests:
    memory: "128Mi"
    cpu: "250m"
  limits:
    memory: "256Mi"
    cpu: "500m"
```

Increase memory limits if the container is OOMKilled:

```yaml
limits:
  memory: "512Mi"
```

**Step 4: Fix startup commands**

```yaml
spec:
  containers:
    - name: web-app
      command: ["/bin/sh", "-c"]
      args: ["echo 'Starting app' && /app/start.sh"]
```

**Step 5: Add a startup probe for slow-starting apps**

```yaml
startupProbe:
  httpGet:
    path: /healthz
    port: 8080
  failureThreshold: 30
  periodSeconds: 10
```

**Step 6: Debug interactively**

```bash
kubectl run debug --image=busybox --rm -it -- /bin/sh
kubectl exec -it web-app-7f8b6c5d4-abc -- /bin/sh
```

## Common Mistakes

- **Not checking previous logs**: Use `--previous` flag to see logs from the crashed container.
- **Setting memory limits too low**: Monitor actual memory usage with `kubectl top pod`.
- **Ignoring readiness probes**: A failing readiness probe prevents the pod from receiving traffic.
- **Not testing locally with Docker**: Run the container locally with the same command to reproduce the issue.

## Related Pages

- [Kubectl Pod Pending](/tools/kubectl/kubectl-pod-pending/) — Pod scheduling issues
- [Kubectl Image Pull Error](/tools/kubectl/kubectl-image-pull-error/) — Image pull failures
- [Ansible Task Failed](/tools/ansible/ansible-task-failed/) — Task execution errors
