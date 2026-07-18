---
title: "[Solution] Kubectl Node Not Ready - Fix Node NotReady Kubelet Not Running"
description: "Fix Kubernetes Node NotReady status when kubelet is not running. Diagnose node health, kubelet logs, and resource pressure."
tools: ["kubectl"]
error-types: ["node-not-ready"]
severities: ["critical"]
weight: 5
---

This error means a Kubernetes node has entered the `NotReady` state. The kubelet on the node is either not running, cannot reach the API server, or the node is experiencing resource pressure.

## What This Error Means

When a node stops reporting its status, the control plane marks it as `NotReady`:

```
kubectl get nodes
NAME       STATUS     ROLES    AGE   VERSION
node-1     NotReady   <none>   30d   v1.28.0
```

Pods on the node may stop working, and new pods will not be scheduled there until it recovers.

## Why It Happens

- The kubelet process crashed or was stopped
- The node ran out of disk, memory, or PID resources
- The container runtime (Docker, containerd, CRI-O) is not responding
- Network connectivity between the node and API server is lost
- A certificate used by the kubelet has expired
- The node was rebooted and kubelet did not start automatically

## How to Fix It

### Check node conditions

```bash
kubectl describe node <node-name> | grep -A 5 "Conditions"
```

Look for `MemoryPressure`, `DiskPressure`, `PIDPressure`, or `NetworkUnavailable`.

### SSH into the node and check kubelet

```bash
ssh <node-name>
sudo systemctl status kubelet
sudo journalctl -u kubelet --since "10 minutes ago" --no-pager
```

Check for error messages in kubelet logs.

### Restart kubelet

```bash
sudo systemctl restart kubelet
```

This is the most common fix for NotReady nodes.

### Check container runtime

```bash
sudo systemctl status containerd
# or
sudo systemctl status docker
```

If the runtime is down, restart it:

```bash
sudo systemctl restart containerd
```

### Check disk space

```bash
df -h
```

If the disk is full, kubelet cannot write logs or manage containers. Clean up:

```bash
sudo crictl rmi --prune
sudo journalctl --vacuum-size=100M
```

### Verify kubelet certificates

```bash
sudo openssl x509 -in /var/lib/kubelet/pki/kubelet-client-current.pem -noout -dates
```

Expired certificates prevent kubelet from authenticating with the API server.

### Cordon and drain the node for maintenance

```bash
kubectl cordon <node-name>
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data
```

## Common Mistakes

- Not checking kubelet logs before assuming the node is unrecoverable
- Ignoring disk or memory pressure warnings until the node goes NotReady
- Not automating kubelet restart with systemd to survive reboots
- Forgetting that container runtime issues look like kubelet issues
- Not monitoring node health with alerts before pods are affected

## Related Pages

- [Kubectl Pod Stuck Terminating]({{< relref "/tools/kubectl/kubectl-stuck-terminating" >}}) -- stuck pod deletion
- [Kubectl OOMKilled]({{< relref "/tools/kubectl/kubectl-oomkilled" >}}) -- memory limit issues
- [Kubectl Connection Refused]({{< relref "/tools/kubectl/kubectl-connection-refused" >}}) -- API server connectivity
