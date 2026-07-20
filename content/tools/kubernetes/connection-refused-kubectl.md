---
title: "[Solution] kubectl connection refused"
description: "Fix kubectl 'connection refused' error. Resolve API server port connectivity issues when the server is not listening."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Connection Refused

`Unable to connect to the server: dial tcp <ip>:6443: connect: connection refused`

This error occurs when the TCP connection to the API server port is actively refused. The server may not be listening on that port.

### Common Causes

- API server is not running
- API server is listening on a different port
- Firewall is blocking the port
- API server pod crashed or is restarting

### How to Fix

Check if the API server process is running (SSH to control plane):
```bash
ps aux | grep kube-apiserver
ss -tlnp | grep 6443
```

### Examples

```bash
# Check API server on control plane
ssh control-plane ss -tlnp | grep 6443
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})