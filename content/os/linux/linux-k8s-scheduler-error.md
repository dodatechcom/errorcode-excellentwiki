---
title: "[Solution] k8s: Scheduler Error — Pod Scheduling Failures"
description: "Fix Kubernetes scheduler errors. Resolve kube-scheduler crashes, scheduling algorithm failures, and scheduler plugin errors."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# k8s: Scheduler Error — Pod Scheduling Failures

A scheduler error occurs when `kube-scheduler` fails to assign pods to nodes. Pods remain in Pending state with scheduling failures. The error reads:

> "0/N nodes are available: N Insufficient cpu"

Or scheduler logs show:

> "scheduler plugin error" or "Failed to reconcile"

## What This Error Means

The Kubernetes scheduler watches for pods with no `nodeName` assigned and runs them through a filtering and scoring pipeline to find the best node. When the scheduler is down, crashed, or its plugins are misconfigured, new pods cannot be scheduled.

## Common Causes

- kube-scheduler process crashed or not running
- Scheduler plugin misconfiguration
- Leader election failure in HA setup
- Scheduler unable to connect to the API server
- Node resources exhausted (scheduler correctly reports no nodes)
- Custom scheduler plugin bug
- Insufficient scheduler resources

## How to Fix

### Check Scheduler Status

```bash
kubectl get pods -n kube-system -l component=kube-scheduler
kubectl logs -n kube-system kube-scheduler-<node-name>
```

### Check Scheduler Leader Election

```bash
kubectl get endpoints kube-scheduler -n kube-system -o yaml
```

### Verify Scheduler Health

```bash
kubectl get --raw /healthz/poststarthook/scheduling/metrics
```

### Check Scheduler Configuration

```bash
kubectl get pod -n kube-system kube-scheduler-<node-name> -o yaml | grep -A 50 "containers"
```

### Restart Scheduler

```bash
# Static pod clusters
sudo systemctl restart kubelet
# Static pod will restart automatically
```

### Check for Resource Exhaustion

```bash
kubectl describe nodes | grep -A 5 "Allocated resources"
kubectl top nodes
```

### Use Default Scheduler Profile

```yaml
# Reset to default scheduling profile
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
  - schedulerName: default-scheduler
    plugins:
      score:
        disabled:
          - name: "*"
        enabled:
          - name: NodeResourcesFit
          - name: NodeAffinity
```

## Related Errors

- [k8s Pod Pending]({{< relref "/os/linux/linux-k8s-pending" >}}) — Pods waiting for scheduling
- [k8s API Server Error]({{< relref "/os/linux/linux-k8s-api-server-error" >}}) — API server issues
- [k8s Node NotReady]({{< relref "/os/linux/linux-k8s-node-not-ready" >}}) — Node readiness issues
