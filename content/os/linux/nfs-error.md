---
title: "[Solution] Linux NFS 'server not responding' — NFS Timeout Fix"
description: "Fix Linux NFS 'server not responding' errors. Resolve NFS timeouts, connection issues, and mount failures with these solutions."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Linux: NFS - server not responding

The `NFS: server not responding` error means the NFS client cannot communicate with the NFS server. This can be caused by network issues, the NFS server being down, firewall blocking NFS ports, or the NFS export being unavailable. The client will typically keep retrying, which can cause long hangs in terminal sessions.

## Common Causes

- NFS server is down or unreachable
- Network connectivity issues between client and server
- Firewall blocking NFS ports (2049, 111)
- NFS server export not configured for the client's IP
- DNS resolution failure for the NFS server hostname
- NFS server overloaded or experiencing disk issues

## How to Fix

### 1. Check Network Connectivity

```bash
# Ping the NFS server
ping -c 4 nfsserver

# Check if the NFS port is accessible
nc -zv nfsserver 2049

# Check RPC portmapper
rpcinfo -p nfsserver
```

### 2. Check NFS Server Status

```bash
# Check if NFS server is running (on the server)
sudo systemctl status nfs-server
sudo systemctl status rpcbind

# On the client, check if you can see exports
showmount -e nfsserver

# Check NFS server logs
sudo journalctl -u nfs-server -f
```

### 3. Check and Fix Firewall Rules

```bash
# Check if NFS ports are open
sudo iptables -L -n | grep -E '2049|111'

# Allow NFS traffic through firewall
sudo iptables -A INPUT -p tcp --dport 2049 -j ACCEPT
sudo iptables -A INPUT -p udp --dport 2049 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 111 -j ACCEPT
sudo iptables -A INPUT -p udp --dport 111 -j ACCEPT

# With firewalld
sudo firewall-cmd --add-service=nfs --permanent
sudo firewall-cmd --reload

# With ufw
sudo ufw allow 2049/tcp
sudo ufw allow 2049/udp
sudo ufw allow 111/tcp
```

### 4. Check NFS Mount Configuration

```bash
# View current NFS mounts
mount | grep nfs
cat /etc/fstab | grep nfs

# Check mount options
nfsstat -m
```

### 5. Remount NFS Share

```bash
# Force remount
sudo umount -f /mnt/nfs
sudo mount -t nfs nfsserver:/exported/path /mnt/nfs

# With specific options for better reliability
sudo mount -t nfs -o hard,intr,timeo=600,retrans=2 nfsserver:/exported/path /mnt/nfs
```

### 6. Use NFSv4 Instead of NFSv3

NFSv4 has better timeout handling and uses a single port:

```bash
# Mount with NFSv4
sudo mount -t nfs4 nfsserver:/exported/path /mnt/nfs

# Check NFS version
nfsstat -c
```

### 7. Fix DNS Resolution

```bash
# Add the server to /etc/hosts if DNS is unreliable
echo "192.168.1.100 nfsserver" | sudo tee -a /etc/hosts

# Test name resolution
getent hosts nfsserver
```

### 8. Set NFS Client Timeout

```bash
# Set shorter timeout values
sudo mount -o timeo=5,retrans=3 nfsserver:/export /mnt/nfs

# For soft mount (returns error instead of hanging — use with caution)
sudo mount -o soft,timeo=5 nfsserver:/export /mnt/nfs
```

## Examples

```bash
$ ls /mnt/nfs
ls: cannot access '/mnt/nfs': Connection timed out

$ dmesg | grep nfs
[  123.456] nfs: server nfsserver not responding, still trying

$ showmount -e nfsserver
clnt_create: RPC: Port mapper failure - Unable to receive: errno 113 (No route to host)

$ sudo iptables -A INPUT -p tcp --dport 2049 -j ACCEPT
$ sudo iptables -A INPUT -p tcp --dport 111 -j ACCEPT
$ showmount -e nfsserver
Exports list on nfsserver:
/exported/path          192.168.1.0/24
```

## Related Errors

- [Connection refused]({{< relref "/os/linux/connection-refused7" >}}) — Service not listening
- [Read-only file system]({{< relref "/os/linux/readonly-filesystem" >}}) — NFS remounted read-only
- [iptables errors]({{< relref "/os/linux/iptables-error" >}}) — Firewall configuration issues
