---
title: "[Solution] Kubernetes Pod evicted — Node memory pressure"
description: "Fix Kubernetes pod eviction due to node memory pressure. Learn why pods are evicted and how to prevent evictions."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Kubernetes Pod evicted — Node memory pressure

Pod eviction occurs when a node runs low on memory or disk. The kubelet proactively evicts pods to reclaim resources and maintain node stability. Evicted pods are not automatically restarted.

## Common Causes

- Node memory usage exceeds the eviction threshold
- Too many pods scheduled on a single node
- Pods consuming more memory than their requests
- Disk pressure on the node's filesystem

## How to Fix

### Check Node Conditions

```bash
kubectl describe node <node-name> | grep -A 5 Conditions
# Look for MemoryPressure: True or DiskPressure: True
```

### List Evicted Pods

```bash
kubectl get pods --field-selector=status.phase=Failed | grep Evicted
```

### Clean Up Evicted Pods

```bash
kubectl get pods --field-selector=status.phase=Failed -o name | \
  xargs kubectl delete
```

### Set Resource Requests and Limits

```yaml
resources:
  requests:
    memory: "256Mi"
    cpu: "250m"
  limits:
    memory: "512Mi"
    cpu: "500m"
```

### Add Cluster Autoscaler

```bash
# Enable cluster autoscaler to add nodes when resources are low
eksctl create nodegroup --cluster=my-cluster \
  --nodes-min=2 --nodes-max=10 --nodes=3
```

## Examples

```bash
# Example 1: Check why pod was evicted
kubectl describe pod <evicted-pod>
# Events: Node became not ready: MemoryPressure
# Fix: add more nodes or reduce pod memory usage

# Example 2: View node memory usage
kubectl top node <node-name>
# NAME        CPU    MEMORY
# worker-1    450m   7800Mi/8192Mi
# Fix: move some pods to other nodes

# Example 3: Recreate evicted pod (Deployment will auto-recreate)
kubectl delete pod <evicted-pod>
# The Deployment controller creates a new pod
```

## Related Errors

- [OOMKilled]({{< relref "/tools/kubernetes/oomkilled" >}}) — container exceeded memory limit
- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crashloop-debug" >}}) — pod crashing repeatedly
- [HPA Error]({{< relref "/tools/kubernetes/hpa-error" >}}) — autoscaler failing to get metrics
