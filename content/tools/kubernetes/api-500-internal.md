---
title: "[Solution] API 500 Internal Server Error"
description: "Fix Kubernetes API 500 Internal Server Error. Resolve server-side failures in the Kubernetes API server."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## API 500 Internal Server Error

This HTTP status code occurs when the Kubernetes API server encounters an unexpected internal error.

### Common Causes

- etcd cluster is unhealthy or unreachable
- API server ran out of memory
- API server panic or crash
- Corrupted data in etcd
- Exceeded maximum request size

### How to Fix

Check API server health:
```bash
kubectl get --raw /healthz
kubectl get --raw /livez
kubectl get --raw /readyz
```

Check etcd health:
```bash
# SSH to control plane
ETCDCTL_ENDPOINTS=https://127.0.0.1:2379 etcdctl endpoint health
```

Check API server logs:
```bash
kubectl logs -n kube-system kube-apiserver-<node>
```

### Examples

```bash
# Check all API server health endpoints
kubectl get --raw /healthz && echo "OK" || echo "FAIL"
kubectl get --raw /livez && echo "OK" || echo "FAIL"
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})