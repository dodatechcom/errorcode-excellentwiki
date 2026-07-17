---
title: "[Solution] k8s: kubelet Error — Node Agent Failures"
description: "Fix Kubernetes kubelet errors. Resolve kubelet crashes, certificate issues, and node agent failures on Kubernetes nodes."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["kubernetes", "k8s", "kubelet", "node", "agent", "runtime", "cri"]
weight: 5
---

# k8s: kubelet Error — Node Agent Failures

A kubelet error occurs when the kubelet agent on a Kubernetes node fails to function correctly. The node may show NotReady, and pods may fail to start. The error reads:

> "Unable to register node with API server"

Or:

> "Failed to start ContainerManager"

## What This Error Means

kubelet is the node-level agent in Kubernetes. It manages pod lifecycle, pulls images, starts/stops containers, and reports node status to the API server. When kubelet fails, pods cannot be scheduled to the node, existing pods may lose health, and the node is marked NotReady.

## Common Causes

- kubelet configuration file has errors
- Container runtime (containerd, CRI-O) not running
- kubelet certificate expired
- Node has insufficient disk space or inodes
- kubelet cannot connect to the API server
- systemd unit for kubelet is in a failed state
- Too many pods on the node exceeding PIDs/filesystem limits

## How to Fix

### Check kubelet Status

```bash
sudo systemctl status kubelet
sudo journalctl -u kubelet --since "10 minutes ago"
```

### Check kubelet Configuration

```bash
cat /var/lib/kubelet/config.yaml
sudo kubelet --validate-config --config /var/lib/kubelet/config.yaml
```

### Check Container Runtime

```bash
sudo systemctl status containerd
sudo crictl info
sudo crictl pods
```

### Check kubelet Certificates

```bash
openssl x509 -in /var/lib/kubelet/pki/kubelet-client-current.pem -text -noout | grep "Not After"
openssl x509 -in /var/lib/kubelet/pki/kubelet-server-current.pem -text -noout | grep "Not After"
```

### Restart kubelet

```bash
sudo systemctl restart kubelet
```

### Check Disk Space and Inodes

```bash
df -h /var/lib/kubelet
df -i /var/lib/kubelet
df -h /var/lib/containerd
```

### Check Pod and PID Limits

```bash
# Check max pods setting
grep maxPods /var/lib/kubelet/config.yaml

# Check system PID limit
cat /proc/sys/kernel/pid_max

# Check file descriptors
cat /proc/sys/fs/file-max
```

### Reinitialize kubelet (Last Resort)

```bash
sudo kubeadm reset -f
sudo kubeadm join <master-ip>:6443 --token <token> --discovery-token-ca-cert-hash sha256:<hash>
```

## Related Errors

- [k8s Node NotReady]({{< relref "/os/linux/linux-k8s-node-not-ready" >}}) — Node readiness issues
- [k8s API Server Error]({{< relref "/os/linux/linux-k8s-api-server-error" >}}) — API server problems
- [k8s CrashLoopBackOff]({{< relref "/os/linux/linux-k8s-crashloop" >}}) — Pod crash loops
