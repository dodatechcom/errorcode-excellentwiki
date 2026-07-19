---
title: "[Solution] Docker OCI Runtime Create Failed — OCI runtime create failed"
description: "Fix Docker OCI runtime create failed error. Resolve container runtime issues with runc and containerd."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 3
---

# OCI runtime create failed

This error occurs when the OCI (Open Container Initiative) runtime (typically runc) fails to create a container. It indicates a problem at the container runtime level.

## Common Causes

- Containerd or runc not installed properly
- Kernel features missing (namespaces, cgroups)
- Incorrect container configuration
- SELinux or AppArmor blocking container creation
- Corrupted container bundle
- Storage driver issues

## How to Fix

### Check Container Runtime

```bash
docker info | grep -i runtime
# Default: runc
```

### Verify runc Is Installed

```bash
runc --version
```

### Check Docker Daemon Logs

```bash
sudo journalctl -u docker.service --no-pager -n 50
```

### Restart Docker and Containerd

```bash
sudo systemctl restart containerd
sudo systemctl restart docker
```

### Check Kernel Features

```bash
# Required features
ls /proc/self/ns/
# Should show: cgroup ipc mnt net pid user uts
```

### Reinstall Docker

```bash
sudo apt-get install --reinstall docker-ce docker-ce-cli containerd.io
```

### Check AppArmor

```bash
aa-status
```

## Examples

```bash
# Example 1: Check runtime
docker info | grep Runtime
# Runtimes: runc

# Example 2: Check runc
runc --version
# runc version 1.0.0

# Example 3: Restart services
sudo systemctl restart containerd docker
```

## Related Errors

- [Could not select device driver]({{< relref "/tools/docker/could-not-select-device-driver" >}}) — related error
- [Container exited]({{< relref "/tools/docker/container-exited" >}}) — related error
