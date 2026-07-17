---
title: "[Solution] Kubernetes controller-manager — reconciliation error"
description: "Fix Kubernetes controller-manager reconciliation errors. Resolve controller sync failures."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A controller-manager reconciliation error means a Kubernetes controller is failing to reconcile the desired state with the actual state. Resources may not be created, updated, or cleaned up as expected.

## What This Error Means

The kube-controller-manager runs multiple controllers (Deployment, ReplicaSet, Node, ServiceAccount, etc.). Each controller watches for changes and reconciles differences between desired and actual state. When reconciliation fails, controllers get stuck in retry loops — deployments may not scale, pods are not rescheduled, finalizers are not removed, and garbage collection stalls.

## Common Causes

- API server is too slow to process controller requests
- etcd latency preventing timely reads/writes
- Controller hit the retry limit and entered exponential backoff
- RBAC permissions missing for the controller's service account
- Too many resources for the controller to process (throttling)
- Admission webhook blocking controller operations

## How to Fix

### Check Controller Manager Status

```bash
kubectl get pods -n kube-system -l component=kube-controller-manager
kubectl logs -n kube-system -l component=kube-controller-manager --tail=100
```

### Check Controller Metrics

```bash
kubectl get --raw /metrics | grep workqueue_depth
kubectl get --raw /metrics | grep rest_client_requests_total{code="5"}
```

### Restart Controller Manager

```bash
sudo systemctl restart kube-controller-manager
```

### Check Work Queue Depth

```bash
kubectl get --raw /metrics | grep workqueue_queue_duration_seconds_bucket
```

### Check for Failed Reconciliations

```bash
kubectl get events --field-selector reason=FailedCreate --all-namespaces
kubectl get events --field-selector reason=ScalingReplicaSet --all-namespaces
```

### Increase Controller Workers

```yaml
# kube-controller-manager flags
--concurrent-replicaset-syncs=10
--concurrent-deployment-syncs=10
--concurrent-node-syncs=5
```

### Check Admission Webhooks

```bash
kubectl get validatingwebhookconfigurations -o wide
```

## Related Errors

- [Kubernetes API Server Error]({{< relref "/tools/kubernetes/k8s-api-server-error-v2" >}}) — API server timeout
- [Kubernetes etcd Error]({{< relref "/tools/kubernetes/k8s-etcd-error-v2" >}}) — etcd leader election failed
- [Kubernetes Scheduler Error]({{< relref "/tools/kubernetes/k8s-scheduler-error-v2" >}}) — failed to schedule pod
