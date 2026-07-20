---
title: "[Solution] kubectl port-forward failed"
description: "Fix 'kubectl port-forward' errors. Resolve port forwarding failures between local machine and Kubernetes pods."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Port Forward Failed

`error: unable to listen on port <port>: Listen failed: listen tcp <addr>: bind: address already in use`

This error occurs when kubectl port-forward cannot bind to the local port or connect to the remote pod.

### Common Causes

- Local port is already in use by another process
- Pod is not running or in CrashLoopBackOff
- Pod is not ready (not passing readiness probes)
- Wrong pod name or namespace

### How to Fix

Check if the local port is in use:
```bash
lsof -i :<port>
```

Use a different local port:
```bash
kubectl port-forward pod/<pod-name> <local-port>:<remote-port>
```

### Examples

```bash
# Use different local port
kubectl port-forward pod/my-app 8081:80

# Port forward with timeout
kubectl port-forward --pod-running-timeout=1m pod/my-app 8080:80
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})