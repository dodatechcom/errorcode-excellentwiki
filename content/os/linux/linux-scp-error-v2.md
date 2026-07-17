---
title: "[Solution] Linux scp Permission Denied — Transfer Fix v2"
description: "Fix Linux 'scp: permission denied' errors. Resolve file transfer permission issues, SSH configuration problems, and path errors."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["scp", "permission-denied", "file-transfer", "ssh", "remote-copy"]
weight: 5
---

# Linux: scp: permission denied

The `scp: permission denied` error means the SCP (Secure Copy Protocol) transfer was rejected due to insufficient permissions. This can happen on either the source or destination side, and may be caused by file permissions, directory permissions, SSH configuration restrictions, or SELinux policies.

## What This Error Means

SCP uses SSH to transfer files between hosts. A permission denied error during SCP can mean: the remote user doesn't have write permission to the destination directory, the local user can't read the source file, SSH is configured to deny the operation, or SELinux is blocking the file access.

## Common Causes

- Remote user doesn't have write permission to destination directory
- Source file not readable by local user
- SSH `AllowUsers` or `DenyUsers` restricts access
- SELinux blocking file access on remote host
- Remote home directory has wrong permissions
- Trying to copy to a system directory without root access
- SSH `ChrootDirectory` restricting file paths

## How to Fix

### 1. Check Destination Directory Permissions

```bash
# On the remote host, check destination directory permissions
ls -la /path/to/destination/

# Ensure the remote user has write access
sudo chown remoteuser:remoteuser /path/to/destination/
sudo chmod 755 /path/to/destination/
```

### 2. Check Source File Permissions

```bash
# Check if you can read the source file
ls -la /path/to/source/file

# Ensure read permission
chmod 644 /path/to/source/file
chmod 755 /path/to/source/directory/
```

### 3. Use Verbose Mode to Diagnose

```bash
# Run SCP with verbose output
scp -v localfile user@remote:/path/

# This shows exactly where the permission is denied
```

### 4. Check SSH Configuration

```bash
# On the remote host, check sshd_config
sudo grep -E 'AllowUsers|DenyUsers|ChrootDirectory|ForceCommand' /etc/ssh/sshd_config

# If AllowUsers is set, ensure your user is listed
# AllowUsers user1 user2

# Restart sshd after changes
sudo systemctl restart sshd
```

### 5. Fix SELinux Context (RHEL/CentOS/Fedora)

```bash
# Check if SELinux is blocking the transfer
sudo ausearch -m AVC -ts recent | grep scp

# Restore context on destination directory
sudo restorecon -Rv /path/to/destination/

# Check SELinux booleans for SCP
getsebool -a | grep ssh
```

### 6. Use Correct SCP Syntax

```bash
# Copy file TO remote
scp localfile user@remote:/path/to/dest/

# Copy file FROM remote
scp user@remote:/path/to/file /local/dest/

# Copy directory recursively
scp -r localdir user@remote:/path/to/dest/

# Use specific SSH key
scp -i /path/to/key localfile user@remote:/path/
```

### 7. Use rsync Instead of scp

rsync is more robust and handles permission issues better:

```bash
# Use rsync with SSH
rsync -avz -e ssh localfile user@remote:/path/to/dest/

# rsync preserves permissions and handles errors more gracefully
```

## Examples

```bash
$ scp file.txt user@remote:/var/www/
scp: /var/www/file.txt: Permission denied

$ ssh user@remote "ls -la /var/www/"
drwxr-xr-x 2 root root 4096 Jun 15 10:00 .
# User doesn't have write permission

$ ssh user@remote "sudo chown user:user /var/www/"
$ scp file.txt user@remote:/var/www/
file.txt                            100%  1234   1.2KB/s   00:00
```

```bash
$ scp -v file.txt user@remote:/tmp/
...
debug1: Sending command: scp -v -t /tmp/
sink: /tmp/file.txt
scp: /tmp/file.txt: Permission denied
lost connection

# SELinux is blocking — check:
$ ssh user@remote "sudo ausearch -m AVC -ts recent | grep scp"
type=AVC ... avc: denied { write } for ...
```

## Related Errors

- [SSH permission denied]({{< relref "/os/linux/linux-ssh-permission-denied" >}}) — SSH authentication failures
- [SSH connection refused]({{< relref "/os/linux/linux-ssh-connection-refused-v2" >}}) — SSH server not running
- [SELinux denied]({{< relref "/os/linux/linux-selinux-denied" >}}) — SELinux blocking access
- [rsync error]({{< relref "/os/linux/linux-rsync-error" >}}) — rsync transfer failures
