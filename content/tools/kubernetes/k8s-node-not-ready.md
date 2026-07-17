---
title: "[Solution] Kubernetes Node NotReady — kubelet not ready"
description: "Fix Kubernetes Node NotReady status. Resolve kubelet readiness issues."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["node", "notready", "kubelet", "kubernetes"]
weight: 5
---

A Node NotReady status means the kubelet on the node is not communicating with the API server. Pods cannot be scheduled and existing pods may be evicted.

## Common Causes

- Kubelet service is stopped or crashed
- Node has run out of disk space or memory
- Network connectivity between node and API server is broken
- Certificate expiration on the node
- Container runtime (Docker/containerd) is not running

## How to Fix

### Check Node Status

```bash
kubectl get nodes
kubectl describe node <node-name>
```

### SSH into Node and Check Kubelet

```bash
sudo systemctl status kubelet
sudo journalctl -u kubelet -f
```

### Restart Kubelet

```bash
sudo systemctl restart kubelet
```

### Check Disk Space

```bash
df -h
```

### Check Container Runtime

```bash
sudo systemctl status containerd
sudo systemctl status docker
```

## Examples

```bash
# Example 1: Node NotReady
kubectl get nodes
# NAME     STATUS     ROLES    AGE   VERSION
# node-1   NotReady   worker   30d   v1.28.0
# Fix: SSH to node-1, restart kubelet

# Example 2: Disk pressure
kubectl describe node node-1
# Conditions: DiskPressure=True
# Fix: clean up Docker images on node
```

## Related Errors

- [Kubernetes Pending]({{< relref "/tools/kubernetes/k8s-pending" >}}) — pod stuck in Pending
- [Kubernetes Service Unavailable]({{< relref "/tools/kubernetes/k8s-service-unavailable" >}}) — service unavailable
