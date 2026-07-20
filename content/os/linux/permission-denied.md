---
title: "[Solution] Linux: permission-denied — permission denied error"
description: "Fix Linux permission-denied errors. permission denied error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["process-error"]
weight: 6
---
# Linux: Permission Denied

Permission denied errors occur when a user or process tries to access a file or directory without the required permissions.

## Common Causes

- File/directory ownership mismatch (wrong user:group)
- File permissions too restrictive (chmod settings)
- Parent directory missing execute (x) permission preventing access
- Filesystem mounted with noexec, nosuid, or nodev options
- SELinux or AppArmor policy denying access
- Read-only filesystem

## How to Fix

### 1. Check Current Permissions

```bash
ls -la /path/to/file
stat /path/to/file
```

### 2. Check Filesystem Mount Options

```bash
mount | grep /mount/point
```

### 3. Fix Ownership

```bash
sudo chown user:group /path/to/file
```

### 4. Fix Permissions

```bash
chmod 644 /path/to/file   # Read/write for owner, read for others
chmod 755 /path/to/dir    # rwx for owner, rx for others
chmod 600 ~/.ssh/id_rsa   # Private key must be 600
```

### 5. Check SELinux Context

```bash
ls -Z /path/to/file
sudo restorecon -v /path/to/file
```

## Examples

```bash
$ cat /etc/shadow
cat: /etc/shadow: Permission denied

$ ls -la /etc/shadow
-rw-r----- 1 root shadow 1234 Jul 20 14:30 /etc/shadow

$ sudo cat /etc/shadow
# Works with sudo
```
