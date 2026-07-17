---
title: "[Solution] Kubernetes Pod Stuck in Pending — insufficient resources"
description: "Fix Kubernetes Pod stuck in Pending state. Resolve insufficient resources and scheduling issues."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A pod stuck in `Pending` means Kubernetes cannot schedule it onto any node. The scheduler cannot find a node with sufficient resources or matching node selectors to run the pod.

## What This Error Means

When a pod remains in `Pending` state, the kube-scheduler has not assigned it to a node. Kubernetes continuously retries scheduling but fails because no node meets the pod's requirements — whether due to insufficient CPU/memory, unmet node selectors, taints, or persistent volume constraints.

## Common Causes

- Cluster nodes do not have enough CPU or memory available
- `nodeSelector` or `affinity` rules do not match any node
- Taints on nodes prevent pod placement without matching tolerations
- PersistentVolumeClaim cannot find a matching PersistentVolume
- Resource quotas in the namespace are exhausted
- Pod exceeds node maximum resource capacity

## How to Fix

### Check Pod Events

```bash
kubectl describe pod <pod-name> | grep -A 10 Events
```

### Check Node Resource Usage

```bash
kubectl top nodes
kubectl describe nodes | grep -A 5 "Allocated resources"
```

### Check Pending Pods

```bash
kubectl get pods --field-selector status.phase=Pending
```

### Increase Node Resources

```bash
kubectl label nodes <node-name> dedicated=general
```

### Remove Node Selectors

```yaml
# Remove or adjust restrictive nodeSelector
spec:
  nodeSelector:
    node-type: general
```

### Check Resource Quotas

```bash
kubectl describe resourcequota -n <namespace>
```

## Related Errors

- [Kubernetes Node NotReady]({{< relref "/tools/kubernetes/k8s-node-not-ready-v2" >}}) — node is unhealthy
- [Kubernetes PVC Error]({{< relref "/tools/kubernetes/k8s-pvc-error-v2" >}}) — no PersistentVolume available
- [Kubernetes CrashLoopBackOff]({{< relref "/tools/kubernetes/k8s-crashloop-v2" >}}) — pod crash loop
