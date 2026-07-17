---
title: "[Solution] Linux NFS Server Not Responding — Mount Fix"
description: "Fix Linux 'NFS: server not responding' errors. Resolve NFS mount timeouts, server unreachable, and stale file handle issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["nfs", "server-not-responding", "network-filesystem", "mount", "stale-handle"]
weight: 5
---

# Linux: NFS: server not responding

The `NFS: server not responding` error means the NFS client cannot communicate with the NFS server. The client sends RPC requests but receives no response within the timeout period. This can cause processes to hang, files to become inaccessible, and system performance to degrade. The error often appears in `dmesg` output.

## What This Error Means

NFS (Network File System) uses RPC (Remote Procedure Call) over the network to access files on a remote server. When the client sends a request and the server doesn't respond within the timeout period (default varies by mount option), the kernel logs `server not responding` and may eventually declare the mount "stale." The system may hang waiting for NFS responses.

## Common Causes

- NFS server is down or unreachable
- Network connectivity issue between client and server
- Firewall blocking NFS ports (2049, 111, 20048)
- NFS server overloaded or hung
- Incorrect NFS mount options (hard mount without intr)
- Stale NFS file handles after server reboot
- DNS resolution failure for NFS server hostname

## How to Fix

### 1. Check NFS Server Status

```bash
# Check if NFS server is running
sudo systemctl status nfs-kernel-server    # Server
sudo systemctl status nfs-common           # Client

# Check if server is reachable
ping nfsserver

# Check NFS exports
showmount -e nfsserver
```

### 2. Check Network Connectivity

```bash
# Test NFS port connectivity
nc -zv nfsserver 2049
nc -zv nfsserver 111

# Check rpcbind
rpcinfo -p nfsserver

# Check if NFS service is registered
rpcinfo -p nfsserver | grep nfs
```

### 3. Fix Firewall Rules

```bash
# Allow NFS through firewall
sudo iptables -A INPUT -p tcp --dport 2049 -j ACCEPT
sudo iptables -A INPUT -p udp --dport 2049 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 111 -j ACCEPT
sudo iptables -A INPUT -p udp --dport 111 -j ACCEPT

# With ufw
sudo ufw allow 2049/tcp
sudo ufw allow 2049/udp
sudo ufw allow 111/tcp
sudo ufw allow 111/udp

# With firewalld
sudo firewall-cmd --permanent --add-service=nfs
sudo firewall-cmd --reload
```

### 4. Remount NFS with Better Options

```bash
# Remount with soft mount and intr (allows timeout)
sudo mount -o remount,soft,timeo=30,retrans=3 /mnt/nfs

# For hard mounts (default, can cause hangs)
# Add intr to allow interrupting
sudo mount -o remount,hard,intr,timeo=600 /mnt/nfs

# Check current mount options
mount | grep nfs
```

### 5. Fix Stale NFS File Handles

```bash
# Check for stale file handles
dmesg | grep -i "stale"

# Unmount the stale mount
sudo umount -f /mnt/nfs    # Force unmount
sudo umount -l /mnt/nfs    # Lazy unmount

# Remount
sudo mount /mnt/nfs
```

### 6. Increase NFS Timeouts

Edit `/etc/fstab` mount options:

```bash
# Add timeout options to fstab
# nfsserver:/export /mnt/nfs nfs defaults,hard,intr,timeo=600,retrans=2,_netdev 0 0

# Apply changes
sudo mount -a
```

### 7. Restart NFS Services

```bash
# On the server
sudo systemctl restart nfs-kernel-server
sudo systemctl restart rpcbind

# On the client
sudo systemctl restart nfs-common
```

### 8. Check NFS Server Configuration

```bash
# On the server, check exports
cat /etc/exports

# Reload exports
sudo exportfs -ra

# Check NFS server logs
sudo journalctl -u nfs-kernel-server
```

## Examples

```bash
$ dmesg | grep nfs
[12345.678] nfs: server nfsserver not responding, still trying
[12346.789] nfs: server nfsserver not responding, still trying
[12347.890] nfs: server nfsserver OK

$ mount | grep nfs
nfsserver:/export on /mnt/nfs type nfs4 (rw,relatime,vers=4.2,rsize=1048576,...)

$ sudo mount -o remount,soft,timeo=30 /mnt/nfs
$ dmesg | tail -5
# No more "server not responding" messages
```

## Related Errors

- [Connection refused]({{< relref "/os/linux/connection-refused7" >}}) — Network connectivity issues
- [/etc/fstab mount failed]({{< relref "/os/linux/linux-fstab-error" >}}) — Mount configuration errors
- [Read-only file system]({{< relref "/os/linux/readonly-filesystem" >}}) — NFS remounted read-only
- [systemd timeout]({{< relref "/os/linux/linux-systemd-timeout" >}}) — NFS mount timeout during boot
