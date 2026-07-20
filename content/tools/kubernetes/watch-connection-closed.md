---
title: "[Solution] Watch connection closed unexpectedly"
description: "Fix Kubernetes watch connection closed errors. Resolve issues when watch requests are terminated unexpectedly."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Watch Connection Closed

`watch close: etcdserver: request timed out`

This error occurs when a watch request to the API server is terminated prematurely. Watches are used by controllers and kubectl get --watch to monitor resource changes.

### Common Causes

- etcd is slow or unhealthy
- Watch cache is too large
- Network connectivity issues
- Client has not processed events fast enough
- Watch timed out (default 5-10 minutes for idle connections)
- API server restart during upgrade

### How to Fix

This is often temporary. Retry the watch operation:
```bash
kubectl get pods --watch
```

If persistent, check etcd health:
```bash
kubectl get --raw /healthz/etcd
```

### Examples

```bash
# Reconnect watch
kubectl get pods --watch 2>&1 | head

# Keep watch alive with periodic requests
while true; do kubectl get pods --watch --request-timeout=300s; sleep 1; done
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})