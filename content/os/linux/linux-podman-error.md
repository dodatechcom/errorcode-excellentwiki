---
title: "[Solution] Linux podman Namespace Error — Fix"
description: "Fix Linux 'podman: namespace error' and container failures. Resolve Podman namespace, rootless, and storage issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: podman: namespace error

The `podman: namespace error` message means Podman encountered a problem with Linux namespaces used for container isolation. Namespaces provide process and resource isolation for containers. When namespace setup fails, containers cannot start. This commonly happens with rootless Podman when user namespaces are not properly configured.

## What This Error Means

Podman uses Linux namespaces (PID, NET, MNT, UTS, IPC, USER) to isolate containers. In rootless mode, Podman creates a user namespace to map the container's root to the host user. When the system doesn't support user namespaces, subuid/subgid ranges aren't configured, or storage is misconfigured, namespace operations fail.

## Common Causes

- User namespace support not enabled in kernel
- Missing `/etc/subuid` and `/etc/subgid` entries
- Storage driver misconfiguration
- SELinux blocking namespace creation
- Kernel user namespace limit reached
- overlay filesystem not supported in user namespace
- Podman storage directory permissions wrong

## How to Fix

### 1. Check User Namespace Support

```bash
# Check if user namespaces are enabled
cat /proc/sys/kernel/unprivileged_userns_clone

# Enable if disabled
sudo sysctl kernel.unprivileged_userns_clone=1

# Make permanent
echo "kernel.unprivileged_userns_clone=1" | sudo tee /etc/sysctl.d/userns.conf
sudo sysctl --system
```

### 2. Configure subuid and subgid

```bash
# Add user to subuid and subgid ranges
sudo usermod --add-subuids 100000-165535 --add-subgids 100000-165535 $USER

# Verify
cat /etc/subuid
cat /etc/subgid

# Should show:
# username:100000:65536
```

### 3. Check Podman Storage Configuration

```bash
# Check storage configuration
cat /etc/containers/storage.conf

# Check user storage
cat ~/.config/containers/storage.conf

# Ensure driver is set correctly
# [storage]
# driver = "overlay"
```

### 4. Reset Podman Storage

```bash
# Remove all containers and images
podman system reset

# Reset storage completely
podman system reset --force

# Check storage status
podman system info
```

### 5. Fix SELinux for Podman

```bash
# Check SELinux context
ls -Z /var/lib/containers/storage/

# Restore context
sudo restorecon -Rv /var/lib/containers/

# Set SELinux booleans
sudo setsebool -P container_manage_cgroup on
```

### 6. Use fuse-overlayfs for Rootless

If overlay is not supported in user namespace:

```bash
# Install fuse-overlayfs
sudo apt install fuse-overlayfs    # Debian/Ubuntu
sudo dnf install fuse-overlayfs    # Fedora

# Configure Podman to use it
mkdir -p ~/.config/containers
cat > ~/.config/containers/storage.conf << EOF
[storage]
driver = "overlay"
[storage.options.overlay]
mount_program = "/usr/bin/fuse-overlayfs"
EOF
```

### 7. Check and Fix UID Mapping

```bash
# Check current user namespace
cat /proc/self/uid_map

# Check Podman user namespace
podman unshare cat /proc/self/uid_map

# Run container with specific UID mapping
podman run --uidmap=0:100000:100000 docker.io/library/alpine id
```

## Examples

```bash
$ podman run alpine echo "hello"
Error: cannot set up namespace mapping: cannot set up user namespace: No space left on device

# Check subuid/subgid
$ cat /etc/subuid
# Empty — no ranges configured

$ sudo usermod --add-subuids 100000-165535 --add-subgids 100000-165535 $USER
$ podman run alpine echo "hello"
hello
```

```bash
$ podman run docker.io/library/alpine echo "hello"
Error: error creating overlay mount: mount overlay: no such device

# overlay not supported in user namespace
$ sudo apt install fuse-overlayfs
$ podman system reset
$ podman run docker.io/library/alpine echo "hello"
hello
```

## Related Errors

- [Docker permission denied]({{< relref "/os/linux/linux-docker-error" >}}) — Docker daemon access issues
- [LXC container error]({{< relref "/os/linux/linux-lxc-error" >}}) — LXC container issues
- [Kernel module error]({{< relref "/os/linux/linux-kernel-module" >}}) — Missing namespace kernel modules
