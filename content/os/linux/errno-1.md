---
title: "[Solution] Linux EPERM (errno 1) — Operation Not Permitted Fix"
description: "Fix Linux EPERM (errno 1) Operation Not Permitted error. Solutions for permission denied issues with chmod, chown, and sudo commands."
platforms: ["linux"]
severities: ["error"]
error_types: ["runtime"]
tags: ["epERM", "permission", "errno-1", "sudo"]
weight: 10
---

# Linux EPERM (errno 1) — Operation Not Permitted

EPERM (errno 1) means the operating system denied a requested operation because the calling process does not have the required privileges. This error appears when you attempt a privileged action without sufficient rights, such as writing to a protected file, modifying system configurations, or managing kernel parameters. It is distinct from EACCES (errno 13) because EPERM typically involves operations requiring root or specific capabilities, not just file-level permissions.

## Common Causes

- Running a command that requires root without `sudo`
- Attempting to bind to a port below 1024 without privileges
- Modifying system files owned by root
- Changing kernel parameters without proper capabilities
- Writing to a filesystem mounted with `nosuid` or `nodev`
- Attempting operations blocked by SELinux or AppArmor policies

## How to Fix EPERM

### 1. Use sudo for Privileged Operations

Most EPERM errors on desktop Linux happen because the command requires root:

```bash
# Instead of:
apt update

# Use:
sudo apt update
```

To run an entire shell session as root:

```bash
sudo -i
```

### 2. Check File Permissions and Ownership

Inspect the target file to understand who owns it and what permissions are set:

```bash
ls -la /path/to/problem/file
```

Example output:

```
-rw------- 1 root root 4096 Jun 15 10:00 /etc/shadow
```

Change ownership if you own the file but it was created by root:

```bash
sudo chown $(whoami) /path/to/problem/file
```

### 3. Use chmod to Adjust Permissions

Grant yourself the necessary permissions:

```bash
# Give yourself read/write access
sudo chmod u+rw /path/to/problem/file

# Give owner full access, group and others read-only
sudo chmod 755 /path/to/problem/directory

# Make a script executable
chmod +x /path/to/script.sh
```

### 4. Check SELinux Context (RHEL/CentOS/Fedora)

SELinux can block operations even when Unix permissions are correct:

```bash
# Check SELinux status
getenforce

# View the security context of a file
ls -Z /path/to/problem/file

# Temporarily set SELinux to permissive mode for testing
sudo setenforce 0

# Restore correct SELinux context
sudo restorecon -Rv /path/to/problem/file
```

### 5. Check AppArmor Profiles (Ubuntu/Debian)

AppArmor may be restricting a program's access:

```bash
# Check AppArmor status
sudo aa-status

# Put a profile in complain mode (log violations instead of blocking)
sudo aa-complain /etc/apparmor.d/usr.sbin.nginx
```

### 6. Check File Capabilities

Some programs need specific Linux capabilities rather than full root:

```bash
# View capabilities on a binary
getcap /usr/bin/ping

# Grant a capability to a binary
sudo setcap cap_net_raw+ep /usr/bin/ping
```

### 7. Adjust ulimit Settings

The process may have hit a resource limit:

```bash
# View current limits
ulimit -a

# Check open files limit
ulimit -n

# Temporarily increase the limit
ulimit -n 65535

# For persistent changes, edit /etc/security/limits.conf
sudo nano /etc/security/limits.conf
```

Add a line like:

```
* soft nofile 65535
* hard nofile 65535
```

### 8. Check if Filesystem is Mounted Read-Only

A read-only filesystem will reject all write operations:

```bash
# Check mount options
mount | grep " / "

# Remount as read-write if needed
sudo mount -o remount,rw /
```

## Verification

After applying the appropriate fix, retry the command that originally failed. You can also verify your effective user and group with:

```bash
id
whoami
groups
```

## Related Error Codes

- [EACCES (errno 13)](/os/linux/errno-13/) — Permission denied at the file level
- [ENOENT (errno 2)](/os/linux/errno-2/) — File or directory not found
- [EIO (errno 5)](/os/linux/errno-5/) — Input/output error
