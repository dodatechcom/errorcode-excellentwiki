---
title: "[Solution] Linux sudo: not in sudoers — Permission Fix"
description: "Fix Linux 'sudo: not in sudoers' errors. Add users to sudo group, edit sudoers file, and resolve privilege escalation issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["sudo", "not-in-sudoers", "privilege", "sudoers", "permission", "wheel"]
weight: 5
---

# Linux: sudo: not in sudoers

The `sudo: <user> is not in the sudoers file. This incident will be reported` error means the user is not authorized to use `sudo` for privilege escalation. The sudoers file (`/etc/sudoers`) defines which users can run commands as root. If a user is not listed, sudo refuses to grant elevated privileges.

## What This Error Means

The sudoers file is the central configuration for `sudo` access. It defines which users or groups can run which commands as root. The file is managed by `visudo` (which validates syntax before saving). Users are typically granted sudo access by being added to the `sudo` group (Debian/Ubuntu) or `wheel` group (RHEL/CentOS/Fedora).

## Common Causes

- User not added to the sudo or wheel group
- User removed from sudo group accidentally
- /etc/sudoers file corrupted or missing user entry
- Typo in username in sudoers configuration
- NIS/LDAP user not synced with local sudoers
- System was freshly installed and user not configured

## How to Fix

### 1. Add User to sudo Group (Easiest Method)

On a system where you have root access:

```bash
# Debian/Ubuntu
sudo usermod -aG sudo username

# RHEL/CentOS/Fedora
sudo usermod -aG wheel username

# Verify the change
groups username
```

Log out and back in for the group change to take effect.

### 2. Edit the sudoers File Safely

Always use `visudo` to edit the sudoers file — it validates syntax before saving:

```bash
# Edit sudoers as root
sudo visudo

# Add a line for the user:
# username ALL=(ALL:ALL) ALL

# Or for passwordless sudo:
# username ALL=(ALL) NOPASSWD: ALL
```

### 3. Add User via sudoers.d Drop-in

The recommended approach for adding individual users:

```bash
# Create a drop-in file
sudo visudo -f /etc/sudoers.d/username

# Add:
# username ALL=(ALL:ALL) ALL

# Set correct permissions
sudo chmod 440 /etc/sudoers.d/username
```

### 4. Emergency: Fix sudoers from Root Shell

If you're locked out and have root access via single-user mode or live USB:

```bash
# Boot to single-user mode or live USB
# Mount the filesystem
sudo mount /dev/sda1 /mnt

# Edit sudoers directly
sudo nano /etc/sudoers

# Or add user to sudo group via chroot
sudo chroot /mnt
usermod -aG sudo username
```

### 5. Verify sudo Configuration

```bash
# Check sudoers syntax
sudo visudo -c

# Check what groups the user belongs to
groups username

# Check if user has sudo access
sudo -l -U username

# Test sudo access
sudo whoami
# Should output: root
```

### 6. Fix Group Membership Issues

```bash
# Ensure the sudo group exists
getent group sudo    # Debian/Ubuntu
getent group wheel   # RHEL/CentOS

# Add group if missing
sudo groupadd sudo   # Debian/Ubuntu
sudo groupadd wheel  # RHEL/CentOS

# Add user to the group
sudo usermod -aG sudo username
```

### 7. Fix LDAP/NIS User Sudo Access

For network users, sudo must be configured to query NSS:

```bash
# Check sudoers configuration for NSS
sudo grep -i nsswitch /etc/nsswitch.conf

# Ensure sudoers has:
# sudoers: files ldap    (or nis)

# For LDAP sudo rules
sudo nano /etc/ldap.conf
# Add: sudoers_base ou=Sudoers,dc=example,dc=com
```

## Examples

```bash
$ sudo apt update
[sudo] password for user:
user is not in the sudoers file. This incident will be reported.

# Fix on another account with root access:
$ sudo usermod -aG sudo user
$ groups user
user : user sudo

# Log out and back in:
$ sudo apt update
[sudo] password for user:
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
```

```bash
$ sudo visudo -c
/etc/sudoers: parsed OK
/etc/sudoers.d/username: parsed OK

$ sudo -l -U user
User user may run the following commands on this host:
    (ALL : ALL) ALL
```

## Related Errors

- [PAM module error]({{< relref "/os/linux/linux-pam-error" >}}) — Authentication module issues
- [Login authentication failure]({{< relref "/os/linux/linux-login-error" >}}) — Login failures
- [Permission denied]({{< relref "/os/linux/connection-refused7" >}}) — General permission issues
