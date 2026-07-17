---
title: "[Solution] Kubernetes OOMKilled — container memory exceeded"
description: "Fix Kubernetes OOMKilled. Resolve container out-of-memory kills by adjusting resource limits."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

OOMKilled means a container exceeded its memory limit and was terminated by the Linux kernel's OOM killer. The kubelet restarts the container, which may lead to a CrashLoopBackOff loop.

## What This Error Means

When a container's memory usage exceeds the `limits.memory` value in its resource specification, the Linux kernel OOM killer terminates the process. The kubelet marks the container's last state as `OOMKilled` and restarts it. Repeated OOM kills result in a CrashLoopBackOff state. This indicates the application requires more memory than currently allocated.

## Common Causes

- Memory limit set too low for the application's workload
- Memory leak in the application causing gradual increase
- Java/JVM heap not aligned with container memory limits
- Node itself running out of memory (node OOM)
- Multiple containers on a node consuming memory unexpectedly
- Missing or insufficient `requests.memory` causing overcommit

## How to Fix

### Check for OOMKilled Status

```bash
kubectl get pod <pod-name> -o jsonpath='{.status.containerStatuses[*].lastState.terminated.reason}'
```

### Check Current Memory Usage

```bash
kubectl top pod <pod-name>
```

### Increase Memory Limits

```yaml
resources:
  limits:
    memory: "1Gi"
  requests:
    memory: "512Mi"
```

### Set JVM Heap to Match Container Limits

```yaml
env:
  - name: JAVA_OPTS
    value: "-Xmx768m -Xms256m"
```

### Use QoS Class Guaranteed

```yaml
resources:
  requests:
    memory: "512Mi"
    cpu: "250m"
  limits:
    memory: "512Mi"
    cpu: "250m"
```

### Monitor Memory Usage Over Time

```bash
kubectl top pod <pod-name> --containers
```

## Related Errors

- [Kubernetes CrashLoopBackOff]({{< relref "/tools/kubernetes/k8s-crashloop-v2" >}}) — pod crash loop
- [Kubernetes Pod Pending]({{< relref "/tools/kubernetes/k8s-pending-v2" >}}) — insufficient resources
- [Kubernetes Node NotReady]({{< relref "/tools/kubernetes/k8s-node-not-ready-v2" >}}) — node unhealthy
