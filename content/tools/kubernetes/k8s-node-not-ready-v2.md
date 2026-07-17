---
title: "[Solution] Kubernetes Node NotReady — kubelet unhealthy"
description: "Fix Kubernetes Node NotReady. Resolve kubelet failures and node health issues."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["kubernetes", "nodenotready", "kubelet", "node", "health", "unhealthy"]
weight: 5
---

Node NotReady means the kubelet on a node has stopped reporting its status to the API server. Pods on this node may be evicted and no new pods can be scheduled onto it.

## What This Error Means

Kubernetes marks a node as `NotReady` when the kubelet fails to send heartbeats to the API server for a configurable period (default 40s). The node controller then begins evicting pods after the `pod-eviction-timeout` (default 5m). This can be caused by kubelet crashes, system resource exhaustion, network partitions, or disk pressure on the node.

## Common Causes

- Kubelet process crashed or stopped running
- Node is experiencing disk pressure or memory pressure
- Network connectivity lost between node and API server
- Systemd service for kubelet is in a failed state
- Node operating system is unresponsive
- Certificate expiry on the kubelet

## How to Fix

### Check Node Status

```bash
kubectl get nodes
kubectl describe node <node-name>
```

### Check Kubelet Logs on the Node

```bash
ssh <node-ip>
sudo journalctl -u kubelet -f --lines=100
```

### Restart Kubelet

```bash
sudo systemctl restart kubelet
sudo systemctl status kubelet
```

### Check Node Conditions

```bash
kubectl get node <node-name> -o jsonpath='{.status.conditions[*].type}'
```

### Drain and Cordon the Node

```bash
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data
kubectl cordon <node-name>
```

### Check Disk and Memory Pressure

```bash
df -h
free -m
```

## Related Errors

- [Kubernetes Pod Pending]({{< relref "/tools/kubernetes/k8s-pending-v2" >}}) — pod cannot be scheduled
- [Kubernetes kubelet Error]({{< relref "/tools/kubernetes/k8s-kubelet-error-v2" >}}) — pod lifecycle error
- [Kubernetes API Server Error]({{< relref "/tools/kubernetes/k8s-api-server-error-v2" >}}) — API server timeout
