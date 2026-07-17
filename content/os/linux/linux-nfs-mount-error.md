---
title: "[Solution] Linux NFS Mount Failed — Fix"
description: "Fix Linux 'mount.nfs: <share> failed' errors. Resolve NFS mount issues including export permissions, firewall, and protocol version mismatches."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Linux: mount.nfs: <share> failed

The `mount.nfs: <share> failed` error means the NFS mount command could not connect to the NFS share. This can happen due to server-side issues (export configuration), network issues, or client-side mount option mismatches.

## Common Causes

- NFS server not exporting the requested path
- Client IP not allowed in `/etc/exports`
- NFS service not running on the server
- Required NFS packages not installed
- NFS version mismatch (NFSv3 vs NFSv4)
- Firewall blocking NFS ports
- Kerberos authentication failure (sec=krb5)

## How to Fix

### 1. Check NFS Service on Server

```bash
# On the server, check NFS services
sudo systemctl status nfs-server
sudo systemctl status rpcbind

# Restart if needed
sudo systemctl restart nfs-server
sudo systemctl restart rpcbind
```

### 2. Check Exports on Server

```bash
# View active exports
sudo exportfs -v

# Check exports configuration
sudo cat /etc/exports

# Reload exports after changes
sudo exportfs -ra
```

Example `/etc/exports` entry:

```
/srv/nfs 192.168.1.0/24(rw,sync,no_subtree_check,no_root_squash)
```

### 3. List Remote Exports

```bash
# From the client, list the server's exports
showmount -e nfsserver

# If this fails, check connectivity
rpcinfo -p nfsserver
```

### 4. Check Firewall Rules

```bash
# On the server, open NFS ports
sudo firewall-cmd --add-service=nfs --permanent
sudo firewall-cmd --add-service=rpc-bind --permanent
sudo firewall-cmd --add-service=mountd --permanent
sudo firewall-cmd --reload

# If using iptables
sudo iptables -A INPUT -p tcp --dport 2049 -j ACCEPT
sudo iptables -A INPUT -p udp --dport 2049 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 111 -j ACCEPT
```

### 5. Install Required Packages

```bash
# Debian/Ubuntu (client)
sudo apt install nfs-common

# RHEL/CentOS/Fedora (client)
sudo dnf install nfs-utils

# Server
sudo apt install nfs-kernel-server    # Debian/Ubuntu
sudo dnf install nfs-utils            # RHEL/CentOS
```

### 6. Try Different Mount Options

```bash
# NFSv4 mount
sudo mount -t nfs4 nfsserver:/exported/path /mnt/nfs

# NFSv3 mount
sudo mount -t nfs -o vers=3 nfsserver:/exported/path /mnt/nfs

# With specific options
sudo mount -t nfs -o hard,intr,timeo=600,retrans=2 nfsserver:/exported/path /mnt/nfs

# Soft mount (returns error instead of hanging)
sudo mount -t nfs -o soft,timeo=10 nfsserver:/exported/path /mnt/nfs
```

### 7. Fix NFSv4 Domain Mismatch

```bash
# On both client and server, ensure NFSv4 domain matches
sudo nano /etc/idmapd.conf

# Set the domain
# Domain = example.com

# Restart idmapd
sudo systemctl restart nfs-idmapd

# Remount
sudo umount /mnt/nfs
sudo mount -t nfs4 nfsserver:/ /mnt/nfs
```

### 8. Check for Port Conflicts

```bash
# On the server, check which ports NFS is using
rpcinfo -p | grep nfs

# Ensure NFS is on port 2049 for NFSv4
# For NFSv3, ensure statd and mountd ports are accessible
```

## Examples

```bash
$ sudo mount -t nfs nfsserver:/srv/nfs /mnt/nfs
mount.nfs: access denied by server while mounting nfsserver:/srv/nfs

$ showmount -e nfsserver
Export list for nfsserver:
/srv/nfs 192.168.1.0/24

# Check client IP — it's 192.168.2.50, not in the allowed subnet
# Fix by adding the client IP to /etc/exports:
/srv/nfs 192.168.1.0/24(rw,sync) 192.168.2.50(rw,sync)

$ sudo exportfs -ra
$ sudo mount -t nfs nfsserver:/srv/nfs /mnt/nfs
# Mount succeeds
```

## Related Errors

- [NFS server not responding]({{< relref "/os/linux/nfs-error" >}}) — NFS timeout errors
- [Connection refused]({{< relref "/os/linux/connection-refused7" >}}) — Service not listening
- [/etc/fstab mount failed]({{< relref "/os/linux/linux-fstab-error" >}}) — Boot-time mount failures
