---
title: "[Solution] Kubernetes API Server — request timeout"
description: "Fix Kubernetes API server request timeout. Resolve kube-apiserver performance and connectivity issues."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An API server request timeout means the kube-apiserver is too slow to respond to client requests. All cluster operations — from kubectl commands to controller loops — are affected.

## What This Error Means

The kube-apiserver is the central hub for all Kubernetes API requests. When it times out, it typically indicates the server is overloaded, etcd is slow, or there are too many resources in the cluster. Clients see `context deadline exceeded` or `request timed out` errors. This affects kubectl, controllers, the scheduler, and all cluster automation.

## Common Causes

- etcd latency too high (slow disk, network issues)
- Too many objects in the cluster overwhelming the API server
- API server resource exhaustion (CPU/memory)
- Slow database queries to etcd for large result sets
- Admission webhooks timing out
- TLS handshake overhead with many concurrent connections

## How to Fix

### Check API Server Status

```bash
kubectl get componentstatuses
kubectl cluster-info
```

### Check API Server Metrics

```bash
kubectl get --raw /metrics | grep apiserver_request_duration_seconds
```

### Check Request Latency

```bash
kubectl get --raw /metrics | grep apiserver_request_total
```

### Restart API Server

```bash
sudo systemctl restart kube-apiserver
```

### Check API Server Resource Usage

```bash
kubectl top pods -n kube-system -l component=kube-apiserver
```

### Increase API Server Processing Timeout

```bash
# In kube-apiserver manifest
--request-timeout=300s
--max-requests-inflight=400
--max-mutating-requests-inflight=200
```

### Audit Slow Requests

```bash
kubectl get --raw /metrics | grep apiserver_request_duration_seconds_bucket{le="1"}
```

### Check Admission Webhooks

```bash
kubectl get validatingwebhookconfigurations
kubectl get mutatingwebhookconfigurations
```

## Related Errors

- [Kubernetes etcd Error]({{< relref "/tools/kubernetes/k8s-etcd-error-v2" >}}) — etcd leader election failed
- [Kubernetes Node NotReady]({{< relref "/tools/kubernetes/k8s-node-not-ready-v2" >}}) — node unhealthy
- [Kubernetes Controller Error]({{< relref "/tools/kubernetes/k8s-controller-error-v2" >}}) — reconciliation error
