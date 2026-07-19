---
title: "[Solution] Docker Cgroups Error — cgroup mountpoint does not exist"
description: "Fix Docker cgroup mountpoint does not exist error. Configure cgroups for containers."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 6
---

# cgroups: cgroup mountpoint does not exist

This error occurs when Docker cannot find the cgroup (control groups) mountpoint. Cgroups are essential for container resource management and isolation.

## Common Causes

- Cgroups not mounted on the host
- Using cgroups v1 vs v2 mismatch
- Docker installed on non-container-compatible system
- Systemd not managing cgroups properly
- Docker daemon misconfigured for cgroup driver

## How to Fix

### Check Cgroup Mount

```bash
mount | grep cgroup
```

### Mount Cgroups Manually

```bash
# For cgroups v1
sudo mount -t cgroup -o cpu,cpuacct none /sys/fs/cgroup/cpu,cpuacct

# For cgroups v2
sudo mount -t cgroup2 none /sys/fs/cgroup
```

### Check Cgroup Version

```bash
stat -fc %T /sys/fs/cgroup/
# cgroup2fs = cgroups v2
# tmpfs = cgroups v1
```

### Configure Docker Cgroup Driver

```json
{
  "exec-opts": ["native.cgroupdriver=systemd"]
}
```

### Restart Docker

```bash
sudo systemctl restart docker
```

### Check Systemd Cgroup

```bash
systemd-cgls
```

## Examples

```bash
# Example 1: Check cgroup mount
mount | grep cgroup
# cgroup on /sys/fs/cgroup/systemd type cgroup

# Example 2: Check cgroup version
stat -fc %T /sys/fs/cgroup/
# cgroup2fs (v2)

# Example 3: Configure Docker
# /etc/docker/daemon.json
{"exec-opts": ["native.cgroupdriver=systemd"]}
sudo systemctl restart docker
```

## Related Errors

- [Docker out of memory]({{< relref "/tools/docker/docker-out-of-memory" >}}) — related error
- [Docker Desktop error]({{< relref "/tools/docker/docker-desktop-error" >}}) — related error
