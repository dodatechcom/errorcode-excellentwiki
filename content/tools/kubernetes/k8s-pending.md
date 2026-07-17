---
title: "[Solution] Kubernetes Pod Pending — Pod stuck in Pending state"
description: "Fix Kubernetes Pending pod status. Resolve why pods are stuck in Pending state."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["pending", "pod", "scheduling", "kubernetes"]
weight: 5
---

A Pending pod means Kubernetes has accepted the pod but it cannot be scheduled onto a node. The pod waits for resources or conditions to be met.

## Common Causes

- No nodes have sufficient resources (CPU, memory) to run the pod
- Node selector or affinity rules match no available nodes
- PersistentVolumeClaim is pending and cannot be bound
- Taints on nodes prevent scheduling
- The cluster has no worker nodes

## How to Fix

### Check Pod Events

```bash
kubectl describe pod <pod-name>
```

### Check Node Resources

```bash
kubectl top nodes
kubectl describe nodes | grep -A 5 "Allocated resources"
```

### Remove Resource Requests (temporary)

```yaml
resources:
  requests:
    cpu: "100m"
    memory: "128Mi"
```

### Check PVC Status

```bash
kubectl get pvc
```

### Add a Worker Node

```bash
kubectl label nodes <node-name> role=worker
```

## Examples

```bash
# Example 1: Insufficient resources
kubectl describe pod my-pod
# Events: FailedScheduling 0/3 nodes are available
# Fix: scale up cluster or reduce resource requests

# Example 2: PVC pending
kubectl get pvc
# STATUS: Pending
# Fix: ensure a matching StorageClass and PersistentVolume exist
```

## Related Errors

- [Kubernetes PVC Error]({{< relref "/tools/kubernetes/k8s-pvc-error" >}}) — PersistentVolumeClaim pending
- [Kubernetes Node NotReady]({{< relref "/tools/kubernetes/k8s-node-not-ready" >}}) — node not ready
