---
title: "[Solution] Linux rsync Connection Error — Sync Fix"
description: "Fix Linux 'rsync: connection error' and transfer failures. Resolve SSH issues, permission errors, and rsync configuration problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["rsync", "connection-error", "sync", "transfer", "ssh", "backup"]
weight: 5
---

# Linux: rsync: connection error

The `rsync: connection error` message means rsync failed to establish or maintain a connection to the remote host. This can happen when using rsync over SSH (the default method) or when running the rsync daemon. The error may appear as `rsync: connection refused`, `rsync: error in socket IO`, or `rsync: failed to connect`.

## What This Error Means

rsync uses SSH as its default transport protocol for remote file transfers. When you run `rsync -avz source user@host:dest`, rsync establishes an SSH connection and uses the rsync protocol over that connection. Connection errors indicate the SSH connection failed, the rsync daemon isn't running, or network issues prevented communication.

## Common Causes

- SSH service not running on remote host
- Incorrect SSH credentials or key authentication
- Firewall blocking SSH port (22) or rsync daemon port (873)
- Remote host unreachable (network issue)
- rsync not installed on remote host
- SSH host key verification failing
- Too many concurrent rsync connections

## How to Fix

### 1. Verify SSH Connectivity First

```bash
# Test SSH connection to remote host
ssh user@remote-host echo "Connection OK"

# If SSH fails, fix SSH first
ssh -vvv user@remote-host
```

### 2. Check rsync Installation

```bash
# Check if rsync is installed locally
rsync --version

# Check if rsync is installed on remote host
ssh user@remote-host "rsync --version"

# Install rsync if missing
sudo apt install rsync        # Debian/Ubuntu
sudo dnf install rsync        # RHEL/CentOS/Fedora
```

### 3. Check Firewall Rules

```bash
# For rsync daemon (port 873)
sudo iptables -A INPUT -p tcp --dport 873 -j ACCEPT

# For rsync over SSH (port 22)
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# With ufw
sudo ufw allow 873/tcp

# With firewalld
sudo firewall-cmd --permanent --add-port=873/tcp
sudo firewall-cmd --reload
```

### 4. Use Verbose Mode to Debug

```bash
# Run rsync with maximum verbosity
rsync -avvvz source user@host:dest 2>&1 | head -50

# Show what rsync is doing
rsync -avv --progress source user@host:dest

# Dry run first
rsync -avzn source user@host:dest
```

### 5. Fix SSH Key Issues for rsync

```bash
# Use a specific SSH key
rsync -avz -e "ssh -i /path/to/key" source user@host:dest

# Disable strict host key checking (less secure)
rsync -avz -e "ssh -o StrictHostKeyChecking=no" source user@host:dest
```

### 6. Use rsync Daemon Mode

If using rsync daemon instead of SSH:

```bash
# Start rsync daemon on server
sudo rsync --daemon

# Check if rsync daemon is listening
sudo ss -tlnp | grep 873

# Connect to daemon
rsync -avz source host::module/dest

# Use specific port
rsync -avz --port=873 source host::module/dest
```

### 7. Increase Timeout and Retries

```bash
# Set connection timeout
rsync -avz --timeout=30 --contimeout=30 source user@host:dest

# Use SSH keepalive
rsync -avz -e "ssh -o ServerAliveInterval=60" source user@host:dest

# Retry on failure
rsync -avz --partial --append-verify source user@host:dest
```

## Examples

```bash
$ rsync -avz /data/ user@backup:/backup/
rsync: [sender] failed to connect to host: Connection refused (111)

$ ssh user@backup echo "OK"
ssh: connect to host backup port 22: Connection refused

# SSH not running on backup server
$ sudo systemctl start sshd

$ rsync -avz /data/ user@backup:/backup/
sending incremental file list
data/file1.txt
data/file2.txt

sent 1,234 bytes  received 56 bytes  2,580.00 bytes/sec
```

```bash
$ rsync -avz /data/ user@host:/backup/
rsync: error in socket IO: Connection reset by peer (104)

$ rsync -avz --timeout=30 /data/ user@host:/backup/
# Works with timeout setting
```

## Related Errors

- [SSH connection refused]({{< relref "/os/linux/linux-ssh-connection-refused-v2" >}}) — SSH server not running
- [SSH permission denied]({{< relref "/os/linux/linux-ssh-permission-denied" >}}) — SSH authentication failures
- [Connection refused]({{< relref "/os/linux/connection-refused7" >}}) — General connection issues
- [scp permission denied]({{< relref "/os/linux/linux-scp-error-v2" >}}) — SCP transfer errors
