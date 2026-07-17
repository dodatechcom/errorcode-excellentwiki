---
title: "[Solution] Linux NFS Mount Failed — no such file or directory"
description: "Fix Linux NFS 'mount failed — no such file or directory' errors. Resolve NFS mount failures, export issues, and network file system problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Linux: NFS — mount failed — no such file or directory

The `mount.nfs: mounting <server>:<path> failed, reason given by server: No such file or directory` error means the NFS server rejected the mount request because the exported path does not exist, is not exported, or the client is not authorized to access it.

## What This Error Means

NFS mounts require the server to have an active export rule for the requested path and the client's IP/hostname must be authorized. The `No such file or directory` message can be misleading — it often means the export does not exist or the client is not in the allowed list, rather than a literal filesystem path issue.

## Common Causes

- Exported path does not exist on the NFS server
- Path not listed in `/etc/exports` on the server
- Client IP or hostname not in the allowed list
- NFS server not running or service stopped
- Firewall blocking NFS ports (2049, 111, 20048)
- Incorrect export options (e.g., `root_squash` blocking access)
- NFS version mismatch between client and server

## How to Fix

### 1. Verify the Export Exists on Server

```bash
# On the NFS server, check exports
cat /etc/exports

# Show active exports
sudo exportfs -v

# Verify the path exists
ls -la /export/path
```

### 2. Check Client Authorization

```bash
# On the server, check if client IP is allowed
grep -E 'client_ip|hostname' /etc/exports

# Example export entry:
# /export/data 192.168.1.0/24(rw,sync,no_subtree_check)

# Re-export after changes
sudo exportfs -ra
```

### 3. Test NFS Export with showmount

```bash
# From the client
showmount -e <nfs-server-ip>

# This lists all exports available to this client
# If empty, the server is not exporting to you
```

### 4. Check NFS Server Status

```bash
# On the server
sudo systemctl status nfs-server

# Start if not running
sudo systemctl start nfs-server
sudo systemctl enable nfs-server

# Check RPC services
sudo rpcinfo -p <nfs-server-ip>
```

### 5. Fix Firewall Rules

```bash
# Check if NFS ports are open
sudo firewall-cmd --list-ports
sudo iptables -L -n | grep -E '2049|111'

# Open NFS ports
sudo firewall-cmd --permanent --add-service=nfs
sudo firewall-cmd --reload

# Or with iptables
sudo iptables -A INPUT -p tcp --dport 2049 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 111 -j ACCEPT
```

### 6. Fix Mount Command

```bash
# Try the mount with verbose output
sudo mount -v -t nfs4 <server>:/export/data /mnt/data

# If version 4 fails, try version 3
sudo mount -t nfs -o vers=3 <server>:/export/data /mnt/data

# Add to /etc/fstab for persistent mount
echo '<server>:/export/data /mnt/data nfs4 defaults,_netdev 0 0' | sudo tee -a /etc/fstab
```

### 7. Fix Permissions and Squash Options

```bash
# On the server, check export options
exportfs -v | grep /export/data

# If root_squash is blocking, consider no_root_squash (use carefully)
# /export/data 192.168.1.0/24(rw,sync,no_subtree_check,no_root_squash)

# Or fix server-side directory permissions
sudo chmod 755 /export/data
sudo chown nobody:nogroup /export/data

sudo exportfs -ra
```

## Examples

```bash
$ sudo mount -t nfs4 nfsserver:/export/data /mnt/data
mount.nfs: mounting nfsserver:/export/data failed, reason given by server: No such file or directory

$ showmount -e nfsserver
Exports list on nfsserver:
/export/backup          192.168.1.0/24
# /export/data is missing from exports

# On server
$ sudo echo '/export/data 192.168.1.0/24(rw,sync,no_subtree_check)' >> /etc/exports
$ sudo exportfs -ra
$ sudo mount -t nfs4 nfsserver:/export/data /mnt/data
$ ls /mnt/data
files...
```

## Related Errors

- [NFS error]({{< relref "/os/linux/linux-nfs-error" >}}) — General NFS errors
- [systemd dependency failed]({{< relref "/os/linux/linux-systemd-dependency-v2" >}}) — NFS mount blocking boot
- [Permission denied]({{< relref "/os/linux/permission-denied10" >}}) — Permission issues
