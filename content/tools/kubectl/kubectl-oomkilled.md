---
title: "[Solution] Kubectl OOMKilled - Fix Container Terminated OOMKilled"
description: "Fix Kubernetes OOMKilled errors when containers exceed memory limits. Adjust resource limits, optimize memory usage, and prevent restarts."
tools: ["kubectl"]
error-types: ["oomkilled"]
severities: ["error"]
weight: 5
---

This error means a container was killed because it exceeded its memory limit. The Linux kernel's OOM killer terminated the container process to protect node stability.

## What This Error Means

When a container uses more memory than its `resources.limits.memory` allows, the kernel kills it:

```
kubectl get pod my-pod
NAME     READY   STATUS      RESTARTS   AGE
my-pod   0/1     OOMKilled   3          2m
```

The container may restart repeatedly if the memory leak persists, entering a CrashLoopBackOff cycle.

## Why It Happens

- The container's memory limit is set too low for the application's needs
- A memory leak in the application causes usage to grow over time
- The application loads large datasets into memory
- Java or Node.js applications do not respect container memory limits
- Multiple containers in a pod share memory without individual limits
- The node itself is under memory pressure

## How to Fix It

### Check current resource limits

```bash
kubectl describe pod my-pod | grep -A 5 "Limits"
```

Review the current memory limit for the affected container.

### Increase memory limits

```yaml
resources:
  limits:
    memory: "512Mi"
  requests:
    memory: "256Mi"
```

Adjust limits based on actual application usage.

### Monitor actual memory usage

```bash
kubectl top pod my-pod
kubectl top pod my-pod --containers
```

Compare actual usage to configured limits to set appropriate values.

### Fix Java memory settings

```yaml
env:
  - name: JAVA_OPTS
    value: "-XX:MaxRAMPercentage=75.0 -XX:+UseContainerSupport"
```

Java needs explicit container-aware memory configuration.

### Fix Node.js memory limits

```yaml
env:
  - name: NODE_OPTIONS
    value: "--max-old-space-size=384"
```

Set Node.js heap limit to ~75% of container memory limit.

### Analyze memory leaks

```bash
kubectl logs my-pod --previous
```

Check logs for memory-related errors or growing allocation patterns.

### Set requests and limits together

```yaml
resources:
  requests:
    memory: "256Mi"
    cpu: "250m"
  limits:
    memory: "512Mi"
    cpu: "500m"
```

Proper requests ensure the pod is scheduled on a node with enough resources.

## Common Mistakes

- Setting memory requests and limits far below actual usage
- Not accounting for JVM overhead when configuring Java containers
- Using only limits without requests, which affects scheduling
- Assuming OOMKilled means the application code is always at fault
- Not monitoring memory trends to catch leaks before they cause kills

## Related Pages

- [Kubectl Pod Crashloopbackoff]({{< relref "/tools/kubectl/kubectl-pod-crashloopbackoff" >}}) -- container restart loops
- [Kubectl Node Not Ready]({{< relref "/tools/kubectl/kubectl-node-not-ready" >}}) -- node resource pressure
- [Kubectl Pod Pending]({{< relref "/tools/kubectl/kubectl-pod-pending" >}}) -- scheduling failures
