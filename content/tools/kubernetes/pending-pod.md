---
title: "[Solution] Kubernetes Pending Pod — Pod stuck in Pending"
description: "Fix Kubernetes pod stuck in Pending status. Resolve scheduling and resource issues."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Kubernetes Pending Pod — Pod stuck in Pending

A pod remains in Pending state when Kubernetes cannot schedule it onto a node. This usually indicates resource constraints or unsatisfied scheduling requirements.

## Common Causes

- Insufficient CPU or memory resources on nodes
- Node selector or affinity rules don't match available nodes
- Persistent volume claim cannot be bound
- Taints on nodes preventing pod scheduling

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

### Check Pending Pods

```bash
kubectl get pods --field-selector status.phase=Pending
```

### Remove Node Selectors

```yaml
# Remove or update nodeSelector
nodeSelector: {}  # Remove specific selectors
```

### Add Tolerations for Tainted Nodes

```yaml
tolerations:
  - key: "dedicated"
    operator: "Equal"
    value: "special-user"
    effect: "NoSchedule"
```

### Scale Up Node Pool

```bash
kubectl scale nodepool <pool-name> --replicas=3
```

## Examples

```bash
# Example 1: Insufficient resources
kubectl describe pod my-app
# Events: Insufficient cpu
# Fix: reduce resource requests or add more nodes

# Example 2: Node selector mismatch
kubectl describe pod my-app
# Events: 0/3 nodes are available: 3 node(s) didn't match node selector
# Fix: update nodeSelector to match available nodes

# Example 3: PVC not bound
kubectl describe pod my-app
# Events: waiting for persistentvolumeclaim "data" to be bound
# Fix: ensure PV and PVC are correctly configured
```

## Related Errors

- [Node Not Ready]({{< relref "/tools/kubernetes/node-not-ready" >}}) — node in cluster is not ready
- [PV Error]({{< relref "/tools/kubernetes/pv-error" >}}) — persistent volume error
