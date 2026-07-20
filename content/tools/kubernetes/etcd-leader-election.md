---
title: "[Solution] etcd leader election failed"
description: "Fix Kubernetes etcd leader election failures. Resolve etcd cluster health issues affecting the control plane."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## etcd Leader Election Failed

`etcdserver: no leader`

This error occurs when the etcd cluster cannot elect a leader. Without a leader, etcd cannot process writes.

### Common Causes

- etcd member(s) are down or unreachable
- Network partition between etcd members
- Disk I/O latency too high (slow disks)
- etcd cluster has lost quorum

### How to Fix

Check etcd member health:
```bash
kubectl get pods -n kube-system -l component=etcd
```

Check etcd logs:
```bash
kubectl logs -n kube-system etcd-<node>
```

### Examples

```bash
# Check etcd cluster status
kubectl exec -n kube-system etcd-control-plane -- etcdctl endpoint status --cluster
# https://node1:2379 is unhealthy

# Check disk latency
ssh control-plane dd if=/dev/zero of=/tmp/test bs=8k count=15000 oflag=direct
# Should be under 10ms for healthy etcd
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})