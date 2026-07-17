---
title: "[Solution] Kubernetes etcd — leader election failed"
description: "Fix Kubernetes etcd leader election failed. Resolve etcd cluster health and leader issues."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["kubernetes", "etcd", "leader", "election", "cluster", "datastore"]
weight: 5
---

An etcd leader election failure means the etcd cluster cannot maintain a stable leader, disrupting all Kubernetes API operations. The cluster enters a read-only or degraded state.

## What This Error Means

etcd is the distributed key-value store that holds all Kubernetes cluster state. In a multi-node etcd cluster, one node is elected leader to coordinate writes. When leader election fails, the cluster cannot accept write operations — no new pods, services, or configuration changes can be created. This is a critical control plane failure that affects the entire cluster.

## Common Causes

- etcd node is unreachable (network partition or crash)
- Clock skew between etcd cluster members exceeds 100ms
- Disk I/O latency too high for etcd to operate
- Insufficient disk space on etcd node
- Certificate expiry for inter-node communication
- Too many failed heartbeat responses

## How to Fix

### Check etcd Cluster Health

```bash
ETCDCTL_API=3 etcdctl endpoint health --cluster \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key
```

### Check Leader Status

```bash
ETCDCTL_API=3 etcdctl endpoint status --cluster \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key -w table
```

### Check etcd Logs

```bash
sudo journalctl -u etcd -f --lines=100
```

### Verify Time Synchronization

```bash
timedatectl
chronyc tracking
```

### Fix Clock Skew

```bash
sudo chronyc makestep
```

### Check Disk Performance

```bash
fio --name=bench --rw=write --bs=64k --size=1G --directory=/var/lib/etcd --numjobs=1 --runtime=30
```

### Remove Failed Member

```bash
ETCDCTL_API=3 etcdctl member list \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key

ETCDCTL_API=3 etcdctl member remove <member-id> \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key
```

## Related Errors

- [Kubernetes API Server Error]({{< relref "/tools/kubernetes/k8s-api-server-error-v2" >}}) — API server timeout
- [Kubernetes Node NotReady]({{< relref "/tools/kubernetes/k8s-node-not-ready-v2" >}}) — node unhealthy
- [Kubernetes Controller Error]({{< relref "/tools/kubernetes/k8s-controller-error-v2" >}}) — reconciliation error
