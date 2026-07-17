---
title: "[Solution] Kubectl Pod Pending — Fix Stuck Pod Scheduling"
description: "Fix kubectl Pod stuck in Pending state. Resolve resource constraints, node selectors, and scheduling failures with practical solutions."
---

## What This Error Means

A pod in `Pending` state means Kubernetes has accepted the pod but cannot schedule it to a node. The pod remains in the queue until a suitable node becomes available or the scheduling constraints are resolved.

A typical output:

```
NAME                    READY   STATUS    RESTARTS   AGE
web-app-7f8b6c5d4-abc   0/1     Pending   0          5m
```

## Why It Happens

Pods get stuck in Pending due to:

- **Insufficient resources**: No node has enough CPU or memory to satisfy the pod's requests.
- **Node selectors or affinity**: The pod requires nodes with specific labels that no node matches.
- **Taints and tolerations**: All available nodes have taints the pod does not tolerate.
- **Persistent volume claims**: The pod requires a PVC that cannot be bound.
- **Node not ready**: All candidate nodes are in NotReady state.
- **Image pull pending**: The image cannot be pulled, delaying pod startup.

## How to Fix It

**Step 1: Check pod events for scheduling details**

```bash
kubectl describe pod web-app-7f8b6c5d4-abc
```

Look for events like:

```
Events:
  Warning  FailedScheduling  0/3 nodes are available: 3 Insufficient cpu.
```

**Step 2: Check node resources**

```bash
kubectl top nodes
kubectl describe nodes | grep -A 5 "Allocated resources"
```

**Step 3: Reduce resource requests**

```yaml
resources:
  requests:
    cpu: "100m"     # Reduced from 1000m
    memory: "128Mi" # Reduced from 512Mi
```

**Step 4: Add or fix node selectors**

```yaml
nodeSelector:
  disktype: ssd
```

Verify nodes have the required labels:

```bash
kubectl get nodes --show-labels
kubectl label nodes node1 disktype=ssd
```

**Step 5: Fix PersistentVolumeClaims**

```bash
kubectl get pvc
kubectl describe pvc my-pvc
```

Ensure a matching PersistentVolume exists or use dynamic provisioning.

**Step 6: Check for tainted nodes**

```bash
kubectl describe nodes | grep Taints
```

Add tolerations if needed:

```yaml
tolerations:
  - key: "dedicated"
    operator: "Equal"
    value: "web"
    effect: "NoSchedule"
```

## Common Mistakes

- **Setting resource requests too high**: Monitor actual usage with `kubectl top pod` and adjust requests.
- **Forgetting to label nodes**: Node selectors require properly labeled nodes.
- **Not checking PVC binding**: A pending PVC will block pod scheduling indefinitely.
- **Ignoring cluster autoscaler**: If using cluster autoscaler, verify it is configured and running.

## Related Pages

- [Kubectl Pod CrashLoopBackOff](/tools/kubectl/kubectl-pod-crashloopbackoff/) — Pod crash restart issues
- [Kubectl Resource Not Found](/tools/kubectl/kubectl-resource-not-found/) — Missing resources
- [Kubectl Image Pull Error](/tools/kubectl/kubectl-image-pull-error/) — Image pull failures
