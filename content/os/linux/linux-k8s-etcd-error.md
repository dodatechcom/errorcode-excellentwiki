---
title: "[Solution] k8s: etcd Error — etcd Cluster Unavailable"
description: "Fix Kubernetes etcd errors. Resolve etcd cluster failures, leader election issues, and data corruption in the Kubernetes backing store."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# k8s: etcd Error — etcd Cluster Unavailable

An etcd error occurs when the etcd cluster backing the Kubernetes API server becomes unavailable or corrupted. The error reads:

> "etcd cluster unavailable"

Or API server logs show:

> "failed to commit health: etcd cluster is unhealthy"

## What This Error Means

etcd is the distributed key-value store that stores all Kubernetes cluster state — pods, services, secrets, ConfigMaps, and all other resources. When etcd is unavailable, the API server cannot read or write any cluster data. The cluster becomes essentially unmanageable. In HA setups, etcd runs as a 3 or 5 node cluster using the Raft consensus protocol.

## Common Causes

- etcd member down (process crashed or node failed)
- etcd disk I/O latency too high (etcd is very sensitive to disk performance)
- etcd certificate expiration
- etcd data directory full or corrupted
- Network partition between etcd members
- Clock skew between etcd nodes
- Too many watch requests overwhelming etcd

## How to Fix

### Check etcd Status

```bash
# For kubeadm clusters
ETCDCTL_API=3 etcdctl \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  endpoint health

ETCDCTL_API=3 etcdctl \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  member list -w table
```

### Check etcd Pod Status

```bash
kubectl get pods -n kube-system -l component=etcd
kubectl logs -n kube-system etcd-<node-name>
```

### Fix Disk Performance

```bash
# Check disk I/O
iostat -x 1 5

# etcd requires <10ms fsync latency
# Move etcd to SSD if on HDD
```

### Check etcd Certificates

```bash
openssl x509 -in /etc/kubernetes/pki/etcd/server.crt -text -noout | grep "Not After"
```

### Backup etcd

```bash
ETCDCTL_API=3 etcdctl \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  snapshot save /backup/etcd-snapshot.db
```

### Defragment etcd

```bash
ETCDCTL_API=3 etcdctl \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  defrag
```

## Related Errors

- [k8s API Server Error]({{< relref "/os/linux/linux-k8s-api-server-error" >}}) — API server issues
- [k8s Node NotReady]({{< relref "/os/linux/linux-k8s-node-not-ready" >}}) — Node heartbeat failures
- [k8s controller-manager Error]({{< relref "/os/linux/linux-k8s-controller-manager" >}}) — Controller manager issues
