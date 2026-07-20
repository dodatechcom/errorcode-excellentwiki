---
title: "[Solution] RegistryUnavailable"
description: "Fix Kubernetes RegistryUnavailable error. Resolve pod failures when the container image registry is unreachable from the node."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## RegistryUnavailable

This error occurs when the kubelet cannot connect to the container image registry. The registry may be down, unreachable, or the connection may be blocked.

### Common Causes

- Registry service outage
- Network connectivity issues between node and registry
- Firewall or security group blocking outbound connections
- DNS resolution failure for registry hostname
- Proxy configuration missing or incorrect

### How to Fix

Test connectivity from a node:
```bash
kubectl run test --image=busybox -it --rm -- wget -S https://registry-1.docker.io/v2/
```

Check DNS resolution:
```bash
kubectl run test --image=busybox -it --rm -- nslookup registry-1.docker.io
```

Configure image pull secrets or proxy settings on the node.

### Examples

```bash
# Test registry connectivity
kubectl run test --image=busybox -it --rm -- wget -S https://registry-1.docker.io/v2/

# Configure containerd proxy
# Edit /etc/systemd/system/containerd.service.d/http-proxy.conf
# [Service]
# Environment="HTTP_PROXY=http://proxy:8080"
# Environment="HTTPS_PROXY=http://proxy:8080"
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})