---
title: "[Solution] Kubectl Cordon Error — Fix Node Cordoning"
description: "Fix kubectl cordon and uncordon node errors. Resolve node drain issues, pod eviction, and maintenance mode problems with solutions."
---

## What This Error Means

Cordon errors occur when kubectl cannot mark a node as unschedulable (cordon) or when cordoning triggers unexpected issues. This command is used during node maintenance to prevent new pods from being scheduled.

A typical error:

```
Error from server (NotFound): node "node1" not found
```

Or when draining:

```
error: unable to drain node "node1", aborting command.
There are pending evictions:
  pod/web-app-7f8b6c5d4-abc
Are you sure you want to continue? [y/n]
```

## Why It Happens

Cordon and drain errors occur when:

- **Node name is wrong**: The specified node name does not exist in the cluster.
- **Node already cordoned**: Attempting to cordon a node that is already in maintenance mode.
- **Pods cannot be evicted**: Pods with `pod disruption budgets` or `local persistent volumes` block eviction.
- **RBAC restrictions**: The user lacks permissions to modify node status.
- **Node not ready**: The node is already in NotReady state and draining may not work properly.
- **DaemonSet pods**: DaemonSet-managed pods cannot be evicted normally.

## How to Fix It

**Step 1: Verify the node exists**

```bash
kubectl get nodes
kubectl describe node node1
```

**Step 2: Cordoning a node**

```bash
kubectl cordon node1
```

This marks the node as unschedulable but does not evict existing pods.

**Step 3: Draining a node for maintenance**

```bash
# Drain with graceful eviction
kubectl drain node1 --ignore-daemonsets --delete-emptydir-data --force

# Skip specific pods
kubectl drain node1 --ignore-daemonsets --delete-emptydir-data --force --pod-selector='app!=critical-app'
```

**Step 4: Handle Pod Disruption Budgets**

```bash
# Check PDBs
kubectl get pdb --all-namespaces

# Override PDB constraints (use cautiously)
kubectl drain node1 --ignore-daemonsets --delete-emptydir-data --force --disable-eviction
```

**Step 5: Uncordon after maintenance**

```bash
kubectl uncordon node1
```

**Step 6: Verify node status**

```bash
kubectl get node node1
kubectl describe node node1 | grep -A 5 "Conditions"
```

## Common Mistakes

- **Forgetting `--ignore-daemonsets`**: DaemonSet pods will block draining. Always use this flag unless you want to remove them.
- **Not using `--delete-emptydir-data`**: Pods with emptyDir volumes need this flag to be evicted.
- **Draining all nodes at once**: Never drain multiple control plane nodes simultaneously.
- **Not checking PDBs first**: Review Pod Disruption Budgets before draining to avoid blocking evictions.
- **Cordoning production nodes without coordination**: Always schedule maintenance windows and notify teams.

## Related Pages

- [Kubectl Pod Pending](/tools/kubectl/kubectl-pod-pending/) — Pod scheduling after cordon
- [Kubectl Resource Not Found](/tools/kubectl/kubectl-resource-not-found/) — Node or resource lookup issues
- [Terraform State Lock Error](/tools/terraform/terraform-state-locked/) — Concurrent operation conflicts
