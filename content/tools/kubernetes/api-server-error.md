---
title: "[Solution] Kubernetes kube-apiserver — too many open files"
description: "Fix Kubernetes kube-apiserver too many open files errors. Resolve file descriptor limits and connection issues."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["apiserver", "too-many-open-files", "file-descriptors", "control-plane", "ulimit"]
weight: 5
---

# Kubernetes kube-apiserver — too many open files

The kube-apiserver hits the OS file descriptor limit when managing too many concurrent connections, watches, or open files. This blocks new API requests and degrades cluster performance.

## Common Causes

- Too many concurrent watch connections from controllers and kubelets
- Low ulimit settings on the control plane node
- Resource leak in an operator or controller creating excessive watches
- Large cluster with many nodes and pods exceeding default limits

## How to Fix

### Check Current File Descriptor Limits

```bash
# For the apiserver process
cat /proc/$(pgrep kube-apiserver)/limits | grep "Max open files"

# System-wide
cat /proc/sys/fs/file-nr
```

### Increase ulimit for kube-apiserver

```bash
# /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
[Service]
LimitNOFILE=1048576
LimitNPROC=65536
```

```bash
# Apply immediately
ulimit -n 1048576
```

### Set limits in kubeadm config

```yaml
apiVersion: kubeadm.k8s.io/v1beta3
kind: ClusterConfiguration
apiServer:
  extraArgs:
    max-requests-inflight: "400"
    watch-cache-sizes: "pods=500"
```

### Restart apiserver with Higher Limits

```bash
# If using static pods
systemctl restart kubelet

# Check new limits
cat /proc/$(pgrep kube-apiserver)/limits | grep "Max open files"
```

## Examples

```bash
# Example 1: Check open file count
ls /proc/$(pgrep kube-apiserver)/fd | wc -l
# Output: 65530 (near limit)
# Fix: increase LimitNOFILE or reduce watch connections

# Example 2: Watch resource leak
kubectl get --raw /metrics | grep apiserver_current_inflight_requests
# fix:2048 watch:8192
# Fix: identify controller creating excessive watches

# Example 3: Cluster too large
kubectl get nodes | wc -l
# 200 nodes, 50000 pods
# Fix: enable watch-cache, tune apiserver flags
```

## Related Errors

- [etcd Error]({{< relref "/tools/kubernetes/etcd-error" >}}) — etcd leader election timeout
- [Pod Evicted]({{< relref "/tools/kubernetes/pod-evicted" >}}) — control plane node resource pressure
- [Ingress Error]({{< relref "/tools/kubernetes/ingress-error" >}}) — service unavailable
