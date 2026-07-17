---
title: "[Solution] Kubernetes scheduler — failed to schedule pod"
description: "Fix Kubernetes scheduler failed to schedule pod. Resolve scheduling failures and pod placement issues."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A scheduler error means the kube-scheduler cannot find a suitable node for a pod. All new pods in the cluster remain in Pending until the scheduler can successfully assign them to nodes.

## What This Error Means

The kube-scheduler evaluates every unscheduled pod against available nodes to find a fit. When scheduling fails, it's typically because no node satisfies all constraints — resource requests, node selectors, taints/tolerations, affinity rules, or topology constraints. In severe cases, the scheduler itself may be unhealthy, affecting all cluster scheduling globally.

## Common Causes

- No nodes have sufficient resources for the pod's requests
- Node selector or affinity rules exclude all available nodes
- Taints on nodes without matching tolerations on pods
- Scheduler pod itself is down or unhealthy
- Too many pending pods overwhelming the scheduler
- Storage class topology constraints cannot be satisfied

## How to Fix

### Check Scheduler Status

```bash
kubectl get pods -n kube-system -l component=kube-scheduler
kubectl logs -n kube-system -l component=kube-scheduler --tail=100
```

### Check Pending Pods

```bash
kubectl get pods --field-selector status.phase=Pending
kubectl describe pod <pending-pod>
```

### Review Scheduling Events

```bash
kubectl get events --field-selector reason=FailedScheduling
```

### Check Scheduler Metrics

```bash
kubectl get --raw /metrics | grep scheduler_schedule_attempts_total
```

### Restart Scheduler

```bash
sudo systemctl restart kube-scheduler
```

### Check Node Constraints

```bash
kubectl describe nodes | grep -A 20 Taints
kubectl get nodes --show-labels
```

### Simplify Pod Constraints

```yaml
# Remove overly restrictive scheduling rules
spec:
  # Remove restrictive nodeSelector
  # Simplify affinity rules
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchLabels:
              app: my-app
          topologyKey: kubernetes.io/hostname
```

### Check Resource Availability

```bash
kubectl describe nodes | grep -A 5 "Allocated resources"
```

## Related Errors

- [Kubernetes Pod Pending]({{< relref "/tools/kubernetes/k8s-pending-v2" >}}) — insufficient resources
- [Kubernetes Controller Error]({{< relref "/tools/kubernetes/k8s-controller-error-v2" >}}) — reconciliation error
- [Kubernetes API Server Error]({{< relref "/tools/kubernetes/k8s-api-server-error-v2" >}}) — API server timeout
