---
title: "[Solution] Kubernetes Node Not Ready — node X not ready"
description: "Fix Kubernetes node not ready error. Diagnose and recover unhealthy cluster nodes."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["node-not-ready", "node", "ready", "cluster", "kubernetes"]
weight: 5
---

# Kubernetes Node Not Ready — node X not ready

A node enters NotReady status when the kubelet stops reporting healthy heartbeats. Pods on the node may be evicted or rescheduled.

## Common Causes

- Kubelet process crashed or stopped
- Node ran out of disk space or memory
- Network connectivity issues between node and control plane
- Node is under heavy resource pressure

## How to Fix

### Check Node Status

```bash
kubectl get nodes
```

### Describe the Node

```bash
kubectl describe node <node-name>
```

### Check Kubelet Status on Node

```bash
ssh <node>
systemctl status kubelet
```

### Restart Kubelet

```bash
ssh <node>
sudo systemctl restart kubelet
```

### Check Node Conditions

```bash
kubectl get node <node-name> -o json | jq '.status.conditions'
```

### Cordon and Drain Node

```bash
kubectl cordon <node-name>
kubectl drain <node-name> --ignore-daemonsets
```

## Examples

```bash
# Example 1: Kubelet stopped
kubectl get nodes
# NAME     STATUS     ROLES    AGE   VERSION
# node1    NotReady   worker   30d   v1.28.0
# Fix: ssh node1 && sudo systemctl restart kubelet

# Example 2: Disk pressure
kubectl describe node node1
# Conditions: DiskPressure=True
# Fix: clean up disk space on node

# Example 3: Evict pods from unhealthy node
kubectl drain node1 --ignore-daemonsets --delete-emptydir-data
```

## Related Errors

- [Pending Pod]({{< relref "/tools/kubernetes/pending-pod" >}}) — pod stuck in Pending state
- [PV Error]({{< relref "/tools/kubernetes/pv-error" >}}) — persistent volume error
