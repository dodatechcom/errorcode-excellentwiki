---
title: "[Solution] Linux Permission Denied (you must be root) — Fix"
description: "Fix Linux 'Permission denied (you must be root)' error. Learn how to use sudo, change file ownership, and fix permissions to resolve this common error."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: Permission Denied (you must be root)

The error `Permission denied (you must be root)` appears when you run a command that requires root (superuser) privileges but you are executing it as a regular user. Linux protects system-critical operations by restricting them to the root account. If you see this message, the system is telling you that the operation you are attempting requires elevated privileges.

## Common Causes

- Running a command that modifies system files without `sudo`
- Attempting to install or remove packages without root access
- Trying to modify files owned by root without proper privileges
- Attempting to bind to ports below 1024

## How to Fix

### 1. Use sudo

The most straightforward fix is to prepend the command with `sudo`:

```bash
# Instead of:
apt update

# Use:
sudo apt update
```

If your user is not in the sudoers file, you'll see `user is not in the sudoers file`. In that case, you need to log in as root directly or ask a system administrator to add you:

```bash
# As root, add your user to the sudo group (Debian/Ubuntu)
usermod -aG sudo yourusername

# On RHEL/CentOS/Fedora
usermod -aG wheel yourusername
```

### 2. Change File Ownership

If you own the file but it was created by root, change ownership to yourself:

```bash
sudo chown $(whoami) /path/to/file
```

For directories and all their contents:

```bash
sudo chown -R $(whoami) /path/to/directory
```

### 3. Adjust File Permissions

Use `chmod` to grant your user the necessary permissions:

```bash
# Give owner read/write, group and others read-only
chmod 644 /path/to/file

# Give owner full permissions, group and others read+execute
chmod 755 /path/to/directory

# Make a script executable
chmod +x /path/to/script.sh
```

### 4. Check if You're Using the Right User

Sometimes you need to switch to a different user entirely:

```bash
# Switch to root
su -

# Switch to another user
su - username
```

### 5. Use setcap for Specific Capabilities

Instead of granting full root, you can give a binary specific capabilities:

```bash
# Grant a binary the ability to bind to privileged ports
sudo setcap cap_net_bind_service=ep /usr/bin/myapp
```

## Examples

```bash
# This will fail without root:
apt install nginx
# Output: Permission denied (you must be root)

# Fix with sudo:
sudo apt install nginx

# This will fail:
service nginx restart
# Output: Permission denied (you must be root)

# Fix with sudo:
sudo service nginx restart

# Checking your user and groups:
id
groups $(whoami)
```

## Related Errors

- [EACCES (errno 13)]({{< relref "/os/linux/errno-13" >}}) — Permission denied at the file level
- [EPERM (errno 1)]({{< relref "/os/linux/errno-1" >}}) — Operation not permitted
- [sudoers errors]({{< relref "/os/linux/permission-denied10" >}}) — User not in sudoers file
