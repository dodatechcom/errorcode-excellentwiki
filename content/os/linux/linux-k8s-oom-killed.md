---
title: "[Solution] k8s: OOMKilled — Container Exceeded Memory Limit"
description: "Fix Kubernetes OOMKilled errors. Resolve container memory limit exceeded issues, increase memory limits, and debug memory leaks."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["kubernetes", "k8s", "oom", "oomkilled", "memory", "limits"]
weight: 5
---

# k8s: OOMKilled — Container Exceeded Memory Limit

OOMKilled means a Kubernetes container was terminated by the Linux OOM killer for exceeding its memory limit. The pod status shows:

> "OOMKilled" as the last state reason in `kubectl describe pod`

Events show:

> "Last State: Terminated Reason: OOMKilled Exit Code: 137"

## What This Error Means

Kubernetes enforces memory limits via Linux cgroups. When a container's memory usage exceeds its `resources.limits.memory`, the kernel sends `SIGKILL` to the container's main process (exit code 137). The container is restarted if the restart policy allows it.

## Common Causes

- Memory limit set too low for the application
- Memory leak in the application code
- JVM not configured for container memory limits
- Application loading more data than expected (large queries, caches)
- Default memory limit too low
- Sidecar containers sharing memory pool

## How to Fix

### Check Current Memory Usage

```bash
kubectl top pods
kubectl top pod <pod-name> --containers

# Check OOM history
kubectl describe pod <pod-name> | grep -A 5 "Last State"
```

### Increase Memory Limits

```yaml
resources:
  requests:
    memory: "512Mi"
  limits:
    memory: "1Gi"
```

### Configure JVM for Kubernetes

```bash
# Java 10+ auto-detects container limits
# For Java 8, set explicitly:
-XX:MaxRAMPercentage=75.0
-XX:+UseContainerSupport
```

### Monitor Memory Over Time

```bash
# Watch memory usage
kubectl top pod <pod-name> --containers -w

# Or use Prometheus/Grafana for historical data
```

### Fix Memory Leaks

Use profiling tools to identify the leak:

```bash
# For Java applications
kubectl exec -it <pod> -- jmap -dump:live,format=b,file=/tmp/heap.hprof 1

# For Go applications
kubectl exec -it <pod> -- wget -qO- http://localhost:6060/debug/pprof/heap > /tmp/heap.pprof
```

### Set Appropriate Requests and Limits

```yaml
resources:
  requests:
    memory: "256Mi"   # Guaranteed minimum
    cpu: "250m"
  limits:
    memory: "512Mi"   # Maximum before OOM
    cpu: "1000m"
```

## Related Errors

- [Docker Container OOM Killed]({{< relref "/os/linux/linux-docker-out-of-memory" >}}) — Docker-level OOM kills
- [k8s CrashLoopBackOff]({{< relref "/os/linux/linux-k8s-crashloop" >}}) — Pod crash loops
- [OOM Killer]({{< relref "/os/linux/oom-killer" >}}) — Linux OOM killer events
