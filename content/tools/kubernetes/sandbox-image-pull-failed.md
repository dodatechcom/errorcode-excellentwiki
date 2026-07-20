---
title: "[Solution] Sandbox image pull failed"
description: "Fix Kubernetes sandbox image pull failures. Resolve errors when the container runtime cannot pull the pause (sandbox) image."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Sandbox Image Pull Failed

`Failed to create pod sandbox: failed to get sandbox image "registry.k8s.io/pause:3.9": failed to pull image`

This error occurs when the container runtime cannot pull the pause/sandbox image required for pod isolation.

### Common Causes

- pause image is not available in the configured registry
- Network connectivity issues to registry.k8s.io
- registry.k8s.io is not accessible from the node
- containerd sandbox_image configuration is incorrect
- Image pull rate limiting for pause image
- containerd cannot reach the configured sandbox registry

### How to Fix

Check the sandbox image configuration:
```bash
sudo cat /etc/containerd/config.toml | grep sandbox_image
```

Pull the sandbox image manually:
```bash
sudo crictl pull registry.k8s.io/pause:3.9
```

Configure a mirror registry for containerd:
```toml
[plugins."io.containerd.grpc.v1.cri".registry.mirrors."registry.k8s.io"]
  endpoint = ["https://mirror.gcr.io"]
```

### Examples

```bash
# Check sandbox image
sudo crictl images | grep pause
# registry.k8s.io/pause:3.9

# Pull sandbox image if missing
sudo crictl pull registry.k8s.io/pause:3.9
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})