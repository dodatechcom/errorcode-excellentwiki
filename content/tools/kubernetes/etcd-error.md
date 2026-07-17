---
title: "[Solution] Kubernetes etcd — leader election timeout"
description: "Fix Kubernetes etcd leader election timeout errors. Resolve etcd cluster instability and leader failover issues."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Kubernetes etcd — leader election timeout

An etcd leader election timeout means the etcd cluster cannot maintain a stable leader. This disrupts the entire control plane, preventing API server operations and cluster state changes.

## Common Causes

- Network latency between etcd nodes exceeding heartbeat timeout
- etcd node is overloaded or experiencing disk I/O bottlenecks
- Insufficient resources (CPU, memory) on etcd nodes
- Clock skew between etcd cluster members

## How to Fix

### Check etcd Health

```bash
ETCDCTL_API=3 etcdctl endpoint health \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key
```

### Check etcd Leader Status

```bash
ETCDCTL_API=3 etcdctl endpoint status \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  --write-out=table
```

### Optimize etcd Performance

```bash
# Check disk I/O latency
iostat -x 1 5

# Ensure SSD for etcd data directory
# etcd requires <10ms disk write latency
```

### Tune etcd Timeouts

```yaml
# /etc/kubernetes/manifests/etcd.yaml
spec:
  containers:
    - name: etcd
      command:
        - etcd
        - --heartbeat-interval=100
        - --election-timeout=1000
```

## Examples

```bash
# Example 1: Check leader
ETCDCTL_API=3 etcdctl endpoint status --write-out=table
# | ENDPOINT                    | ID   | LEADER | ...
# | https://10.0.1.10:2379      | 1    | true   | ...
# Fix: if no leader, restart etcd on one node first

# Example 2: High disk latency
iostat -x 1 5
# Device  await  svctm  %util
# sda     45ms   38ms   95%
# Fix: move etcd data to SSD or reduce write load

# Example 3: Clock skew
etcdctl check perf
# Warning: clock skew detected
# Fix: sync clocks with chrony or ntpd on all etcd nodes
```

## Related Errors

- [kube-apiserver Error]({{< relref "/tools/kubernetes/api-server-error" >}}) — API server issues
- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crashloop-debug" >}}) — control plane component crashing
- [Pod Evicted]({{< relref "/tools/kubernetes/pod-evicted" >}}) — etcd node resource pressure
