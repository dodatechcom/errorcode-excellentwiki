---
title: "[Solution] Linux lxc Container Error — Fix"
description: "Fix Linux 'lxc: container error' and LXC startup failures. Resolve LXC configuration, namespace, and networking issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["lxc", "container", "lxc-start", "namespace", "cgroup", "apparmor"]
weight: 5
---

# Linux: lxc: container error

The `lxc: container error` message means the Linux Containers (LXC) runtime encountered a problem starting or managing a container. LXC provides system containers that run a full Linux OS. Errors can occur during container creation, startup, or networking setup.

## What This Error Means

LXC uses kernel features (namespaces, cgroups, AppArmor/SELinux profiles) to create isolated system containers. When any of these subsystems fail — missing kernel support, configuration errors, AppArmor profile issues, or networking misconfiguration — LXC reports a container error and the container fails to start.

## Common Causes

- LXC service not running or misconfigured
- Missing kernel namespace or cgroup support
- AppArmor profile blocking container operations
- Network bridge not configured
- Storage backend (zfs, lvm, btrfs, dir) misconfigured
- Container configuration file syntax errors
- Insufficient disk space or inodes
- UID/GID mapping issues

## How to Fix

### 1. Check LXC Service Status

```bash
# Check LXD status
sudo systemctl status lxd

# Start LXD if not running
sudo systemctl start lxd
sudo systemctl enable lxd

# Check LXD initialization
sudo lxd init
```

### 2. Verify System Requirements

```bash
# Check kernel version
uname -r

# Check namespace support
ls /proc/self/ns/

# Check cgroup version
cat /proc/filesystems | grep cgroup

# Check AppArmor status
sudo aa-status
```

### 3. Fix LXC Storage

```bash
# Check storage pools
sudo lxc storage list

# Check storage status
sudo lxc storage info default

# Create or fix storage pool
sudo lxc storage create default dir source=/var/lib/lxc/storage/paths/default

# Set storage backend
sudo lxc storage create default zfs zfs.pool_name=lxd
```

### 4. Fix Network Configuration

```bash
# Check network bridges
sudo lxc network list
brctl show

# Create or fix network bridge
sudo lxc network create lxdbr0

# Configure network settings
sudo lxc network set lxdbr0 ipv4.address 10.0.0.1/24
sudo lxc network set lxdbr0 ipv4.nat true
```

### 5. Fix Container Configuration

```bash
# Check container configuration
sudo lxc config show <container>

# Edit container configuration
sudo lxc config edit <container>

# Check container logs
sudo lxc info <container> --show-log
```

### 6. Reset and Recreate Container

```bash
# Stop and delete the container
sudo lxc stop <container>
sudo lxc delete <container>

# Recreate with correct settings
sudo lxc launch ubuntu:22.04 <container>

# Or with specific resources
sudo lxc launch ubuntu:22.04 <container> \
  -c limits.cpu=2 \
  -c limits.memory=2GB \
  -s default
```

### 7. Fix AppArmor Issues

```bash
# Check if AppArmor is blocking
sudo journalctl | grep -i "apparmor.*lxc"

# Set container to unconfined (less secure)
sudo lxc config set <container> security.apparmor false

# Or set a custom profile
sudo lxc config set <container> security.apparmor=unconfined
```

## Examples

```bash
$ sudo lxc start mycontainer
Error: Failed to start container: exit status 1

$ sudo lxc info mycontainer --show-log
lxc start mycontainer 20250101T120000.000000Z lxccontainer 0035.c  - lxc_start.c:356: start_secondary: 1030 - Failed to set up mount namespace
lxc start mycontainer 20250101T120000.000000Z lxccontainer 0035.c  - lxc_start.c:964: __lxc_start: 1356 - Failed to spawn container

# Check namespace support
$ ls /proc/self/ns/
cgroup  ipc  mnt  net  pid  user  uts

# Check cgroup
$ cat /sys/fs/cgroup/cgroup.controllers
# Output indicates cgroup v2 support
```

## Related Errors

- [Docker permission denied]({{< relref "/os/linux/linux-docker-error" >}}) — Docker container issues
- [Podman namespace error]({{< relref "/os/linux/linux-podman-error" >}}) — Podman container issues
- [Kernel module error]({{< relref "/os/linux/linux-kernel-module" >}}) — Missing kernel features
