---
title: "[Solution] Node disk full"
description: "Fix Kubernetes node disk full errors. Resolve pod failures and node issues caused by exhausted disk space."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Node Disk Full

`No space left on device`

This error occurs when the node's disk is completely full. Pods may fail to start, crash, or be evicted.

### Common Causes

- Container logs filling up disk space
- Docker/containerd image cache consuming space
- Application logs not rotated
- Node has small root partition

### How to Fix

SSH to the node and check disk usage:
```bash
df -h
du -sh /var/log/
du -sh /var/lib/docker/
```

Clean up disk space:
```bash
docker system prune -a -f
sudo journalctl --vacuum-size=500M
sudo find /var/log -name "*.log" -mtime +7 -delete
```

### Examples

```bash
# Check disk space on node
ssh <node> df -h
# /dev/sda1   50G   48G   2G   96% /

# Prune Docker system
ssh <node> "docker system prune -a -f"
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})