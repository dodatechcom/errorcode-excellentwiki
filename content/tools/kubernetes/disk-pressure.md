---
title: "[Solution] DiskPressure"
description: "Fix Kubernetes DiskPressure node condition. Resolve nodes that are under disk space pressure and may evict pods."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## DiskPressure

A node enters DiskPressure state when the local disk usage exceeds the configured threshold (default 85% for image filesystem, 90% for node filesystem). Pods may be evicted to reclaim disk space.

### Common Causes

- Node disk is nearly full
- Excessive container logs filling disk
- Docker/containerd image cache consuming space
- Application writing large files to the node filesystem
- Not enough inodes available

### How to Fix

SSH to the node and check disk usage:
```bash
df -h
du -sh /var/log/
du -sh /var/lib/docker/
```

Clean up unused images:
```bash
docker image prune -a -f
# or with crictl
crictl rmi --prune
```

Configure log rotation in kubelet config:
```yaml
containerLogMaxSize: 10Mi
containerLogMaxFiles: 5
```

### Examples

```bash
# Check disk on node
ssh <node> df -h
# /dev/sda1   50G   48G   2G   96% /

# Remove unused Docker images
ssh <node> docker image prune -a -f
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})