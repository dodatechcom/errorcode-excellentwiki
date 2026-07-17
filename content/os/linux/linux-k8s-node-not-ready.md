---
title: "[Solution] k8s: Node NotReady — Kubernetes Node Unavailable"
description: "Fix Kubernetes Node NotReady status. Resolve node heartbeat failures, kubelet crashes, and node readiness conditions."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["kubernetes", "k8s", "node", "notready", "kubelet", "heartbeat"]
weight: 5
---

# k8s: Node NotReady — Kubernetes Node Unavailable

A Node NotReady status means the Kubernetes API server has not received a heartbeat from the node's kubelet within the expected period. The status shows:

> "NotReady" in `kubectl get nodes`

Events show:

> "NodeNotReady node [name] status is now: NodeNotReady"

## What This Error Means

Each node runs a kubelet agent that periodically reports its status to the API server (default every 10 seconds). If the API server misses enough heartbeats (`node-monitor-grace-period`, default 40 seconds), it marks the node as `NotReady`. Pods on the node are evicted after the `pod-eviction-timeout` (default 5 minutes).

## Common Causes

- kubelet process crashed or is not running
- Node is out of resources (disk pressure, memory pressure, PID pressure)
- Network partition between node and API server
- Node is overloaded (too many pods, high CPU/memory usage)
- Certificate expired for kubelet
- Container runtime (containerd, CRI-O) is down

## How to Fix

### Check Node Conditions

```bash
kubectl describe node <node-name> | grep -A 20 "Conditions:"
```

Common conditions:
- `Ready=False` — kubelet not reporting
- `DiskPressure=True` — node disk full
- `MemoryPressure=True` — node out of memory
- `PIDPressure=True` — too many processes

### SSH into the Node and Check kubelet

```bash
sudo systemctl status kubelet
sudo journalctl -u kubelet --since "10 minutes ago"

# Restart kubelet
sudo systemctl restart kubelet
```

### Check Node Resources

```bash
df -h /
free -m
ps aux | wc -l
```

### Fix Disk Pressure

```bash
# Clean up unused images
sudo crictl rmi --prune

# Clean up old pods
sudo crictl rm $(sudo crictl pods -q)

# Check containerd logs
sudo journalctl -u containerd --since "10 minutes ago"
```

### Check Network Connectivity

```bash
# From the node
kubectl cluster-info
curl -k https://<api-server>:6443/healthz
```

### Renew kubelet Certificates

```bash
sudo kubeadm certs renew kubelet-client
sudo systemctl restart kubelet
```

## Related Errors

- [k8s API Server Error]({{< relref "/os/linux/linux-k8s-api-server-error" >}}) — API server issues
- [k8s kubelet Error]({{< relref "/os/linux/linux-k8s-kubelet-error" >}}) — kubelet problems
- [k8s Pod Pending]({{< relref "/os/linux/linux-k8s-pending" >}}) — Pods waiting for scheduling
