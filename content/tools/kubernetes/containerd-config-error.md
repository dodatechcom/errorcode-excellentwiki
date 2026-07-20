---
title: "[Solution] containerd configuration error"
description: "Fix containerd configuration errors in Kubernetes. Resolve container runtime startup failures due to invalid config."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Containerd Configuration Error

`failed to load plugin "io.containerd.grpc.v1.cri": no such binary`

This error occurs when containerd cannot start because its configuration file has invalid entries.

### Common Causes

- containerd config.toml has syntax errors
- Missing or invalid plugin configuration
- Incompatible containerd version with config
- Missing required binaries (runc, cni plugins)
- Invalid sandbox image configuration

### How to Fix

Check containerd config:
```bash
sudo containerd config dump 2>&1 | head -50
```

Check the config file:
```bash
sudo cat /etc/containerd/config.toml
```

Validate and regenerate config:
```bash
sudo containerd config default > /etc/containerd/config.toml
sudo systemctl restart containerd
```

### Examples

```bash
# Backup and regenerate config
sudo cp /etc/containerd/config.toml /etc/containerd/config.toml.bak
sudo containerd config default | sudo tee /etc/containerd/config.toml
sudo systemctl restart containerd
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})