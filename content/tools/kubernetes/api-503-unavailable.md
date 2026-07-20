---
title: "[Solution] API 503 Service Unavailable"
description: "Fix Kubernetes API 503 Service Unavailable error. Resolve temporary API server unavailability during upgrades or overload."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## API 503 Service Unavailable

This HTTP status code occurs when the Kubernetes API server is temporarily unable to handle the request, typically during upgrades or overload.

### Common Causes

- API server is restarting (upgrade or crash)
- etcd leader election in progress
- etcd is overloaded or out of disk space
- API server is under heavy load
- Webhook endpoint is down causing timeouts

### How to Fix

Wait and retry with backoff:
```bash
while ! kubectl get nodes; do sleep 5; done
```

Check API server pods:
```bash
kubectl get pods -n kube-system -l component=kube-apiserver
```

### Examples

```bash
# Retry command with backoff
for i in 1 2 3 4 5; do kubectl get nodes && break; sleep $((i*2)); done
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})