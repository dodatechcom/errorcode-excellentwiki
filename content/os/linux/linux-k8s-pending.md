---
title: "[Solution] k8s: Pod Stuck in Pending Status"
description: "Fix Kubernetes pods stuck in Pending status. Resolve scheduling failures, insufficient resources, and node selector issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# k8s: Pod Stuck in Pending Status

A pod in Pending status has been accepted by the Kubernetes scheduler but has not yet been placed on a node. The status shows:

> "Pending" in `kubectl get pods`

With events showing:

> "0/3 nodes are available: 3 Insufficient cpu."

## What This Error Means

The Kubernetes scheduler assigns pods to nodes based on resource requests, node selectors, taints/tolerations, and affinity rules. When no suitable node is available, the pod remains in Pending state. This is a scheduling constraint issue, not an application bug.

## Common Causes

- Insufficient CPU or memory on all nodes
- PersistentVolumeClaim cannot be bound
- Node selector/affinity rules matching no nodes
- Taints on all nodes without matching tolerations
- Pod disruption budget preventing scheduling
- StorageClass does not exist or is not provisioned

## How to Fix

### Check Pod Events

```bash
kubectl describe pod <pod-name> | grep -A 20 "Events:"
```

### Check Node Resources

```bash
kubectl top nodes
kubectl describe nodes | grep -A 5 "Allocated resources"
```

### Reduce Resource Requests

```yaml
resources:
  requests:
    cpu: "100m"
    memory: "128Mi"
```

### Check for PVC Issues

```bash
kubectl get pvc
kubectl describe pvc <pvc-name>
kubectl get storageclass
```

### Remove Node Selectors or Add Tolerations

```yaml
# Remove restrictive node selector
# nodeSelector:
#   disktype: ssd

# Or add tolerations for tainted nodes
tolerations:
  - key: "dedicated"
    operator: "Equal"
    value: "special-user"
    effect: "NoExecute"
```

### Add More Nodes

```bash
# Check current nodes
kubectl get nodes -o wide

# Scale up node pool (cloud-specific)
# AWS EKS
eksctl scale nodegroup --nodes=5 --cluster=mycluster --name=ng-1
```

## Related Errors

- [k8s CrashLoopBackOff]({{< relref "/os/linux/linux-k8s-crashloop" >}}) — Pod crash loops
- [k8s PVC Pending]({{< relref "/os/linux/linux-k8s-pvc-error" >}}) — PersistentVolumeClaim issues
- [k8s Node NotReady]({{< relref "/os/linux/linux-k8s-node-not-ready" >}}) — Node readiness issues
