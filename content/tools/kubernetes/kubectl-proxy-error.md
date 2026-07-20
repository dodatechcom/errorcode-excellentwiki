---
title: "[Solution] kubectl proxy error"
description: "Fix kubectl proxy errors. Resolve issues when running kubectl proxy to access the Kubernetes API locally."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## kubectl Proxy Error

`error: unable to listen on port 8001: Listen failed: listen tcp 127.0.0.1:8001: bind: address already in use`

This error occurs when kubectl proxy cannot start because the port is already in use.

### Common Causes

- Another kubectl proxy process is already running
- Another application is using port 8001
- Incorrect API server URL or unreachable
- TLS certificate issue with the proxy
- Permission denied to listen on the port

### How to Fix

Find and kill existing proxy:
```bash
pkill -f "kubectl proxy"
```

Use a different port:
```bash
kubectl proxy --port=8080
```

Check what is using the port:
```bash
lsof -i :8001
```

### Examples

```bash
# Kill existing proxy and restart on a different port
pkill -f "kubectl proxy" || true
kubectl proxy --port=8080 --accept-hosts='.*'

# Access API through proxy
curl http://localhost:8080/api/v1/namespaces
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})