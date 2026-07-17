---
title: "[Solution] k8s: Controller Manager Error — Controller Failures"
description: "Fix Kubernetes controller-manager errors. Resolve controller reconciliation failures, leader election issues, and controller-manager crashes."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["kubernetes", "k8s", "controller-manager", "reconciliation", "leader-election", "control-plane"]
weight: 5
---

# k8s: Controller Manager Error — Controller Failures

A controller-manager error occurs when the `kube-controller-manager` fails to reconcile desired state with actual state. The error may show:

> "leader election lost" or

> "failed to sync: timed out waiting for the condition"

## What This Error Means

The controller-manager runs built-in controllers (Deployment, ReplicaSet, Node, ServiceAccount, etc.) that watch the API server and take actions to converge the cluster toward the desired state. When the controller-manager is down or unhealthy, resources like Deployments, ReplicaSets, and Services stop being reconciled.

## Common Causes

- controller-manager process crashed or not running
- Leader election failure (HA clusters)
- etcd latency too high for reconciliation
- Too many resources to reconcile (thundering herd)
- Admission webhooks blocking controller operations
- Certificate expiration
- Insufficient resources on the control plane node

## How to Fix

### Check Controller Manager Status

```bash
kubectl get pods -n kube-system -l component=kube-controller-manager
kubectl logs -n kube-system kube-controller-manager-<node-name>
```

### Check Leader Election

```bash
# Check who is the leader
kubectl get endpoints kube-controller-manager -n kube-system -o yaml
```

### Verify Certificates

```bash
kubeadm certs check-expiration
```

### Check Controller Manager Flags

```bash
kubectl get pod -n kube-system kube-controller-manager-<node-name> -o yaml | grep -A 50 "containers"
```

### Restart Controller Manager

```bash
# For static pod clusters
sudo systemctl restart kubelet

# For kubeadm clusters, the static pod will restart automatically
```

### Check for Admission Webhook Issues

```bash
kubectl get validatingwebhookconfigurations
kubectl get mutatingwebhookconfigurations
```

### Increase Controller Manager Resources

```yaml
resources:
  requests:
    cpu: "200m"
    memory: "256Mi"
  limits:
    cpu: "2000m"
    memory: "4Gi"
```

## Related Errors

- [k8s API Server Error]({{< relref "/os/linux/linux-k8s-api-server-error" >}}) — API server issues
- [k8s etcd Error]({{< relref "/os/linux/linux-k8s-etcd-error" >}}) — etcd cluster issues
- [k8s scheduler Error]({{< relref "/os/linux/linux-k8s-scheduler-error" >}}) — Scheduler issues
