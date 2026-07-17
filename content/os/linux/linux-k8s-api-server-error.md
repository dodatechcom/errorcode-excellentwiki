---
title: "[Solution] k8s: API Server Error — kube-apiserver Unavailable"
description: "Fix Kubernetes API server errors. Resolve apiserver crashes, certificate issues, and high latency problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["kubernetes", "k8s", "api-server", "apiserver", "certificate", "latency"]
weight: 5
---

# k8s: API Server Error — kube-apiserver Unavailable

An API server error occurs when the Kubernetes API server (`kube-apiserver`) is unavailable or malfunctioning. The error reads:

> "The connection to the server <host>:6443 was refused"

Or:

> "Unable to connect to the server: x509: certificate has expired"

## What This Error Means

The API server is the central management entity in Kubernetes. All `kubectl` commands, controller operations, and kubelet heartbeats go through the API server. When it is down, the entire cluster becomes unmanageable. `kubectl` commands fail, controllers cannot reconcile, and nodes may be marked NotReady.

## Common Causes

- API server process crashed or not running
- TLS certificate expired or misconfigured
- etcd backing store unavailable
- Insufficient resources (CPU/memory) on the control plane node
- Too many concurrent requests (API flood)
- Admission webhook timing out
- Firewall blocking port 6443

## How to Fix

### Check API Server Status

```bash
kubectl cluster-info
kubectl get --raw /healthz
kubectl get --raw /readyz
```

### Check API Server Pod

```bash
kubectl get pods -n kube-system -l component=kube-apiserver
kubectl logs -n kube-system kube-apiserver-<node-name>
```

### Verify TLS Certificates

```bash
# Check API server certificate
openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout | grep "Not After"

# Check all control plane certs
kubeadm certs check-expiration
```

### Renew Expired Certificates

```bash
sudo kubeadm certs renew all
sudo systemctl restart kubelet
```

### Check API Server Flags

```bash
kubectl get pod -n kube-system kube-apiserver-<node-name> -o yaml | grep -A 50 "containers"
```

### Check Firewall Rules

```bash
# Ensure port 6443 is open
sudo iptables -L -n | grep 6443
sudo firewall-cmd --list-ports  # firewalld
```

### Increase API Server Resources

```yaml
# In kubeadm config or static pod manifest
resources:
  requests:
    cpu: "250m"
    memory: "512Mi"
  limits:
    cpu: "2000m"
    memory: "4Gi"
```

## Related Errors

- [k8s etcd Error]({{< relref "/os/linux/linux-k8s-etcd-error" >}}) — etcd cluster issues
- [k8s Node NotReady]({{< relref "/os/linux/linux-k8s-node-not-ready" >}}) — Node heartbeat failures
- [k8s RBAC Forbidden]({{< relref "/os/linux/linux-k8s-rbac-error" >}}) — RBAC permission issues
