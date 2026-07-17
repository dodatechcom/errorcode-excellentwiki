---
title: "[Solution] Linux 'login: authentication failure' — Fix"
description: "Fix Linux login authentication failures. Reset passwords, fix PAM configuration, and recover access to locked accounts."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Linux: login: authentication failure

The `login: authentication failure` error means the system's authentication system rejected your credentials. This can happen at the console, SSH, or GUI login.

## Common Causes

- Incorrect password (caps lock, wrong keyboard layout)
- Account locked due to too many failed attempts
- Account expired or disabled
- PAM configuration error
- Password hash corrupted in /etc/shadow
- Home directory not accessible (affects GUI login)
- SELinux or AppArmor blocking authentication

## How to Fix

### 1. Recover as Root

```bash
# If you can access root, reset the user password
# Boot to recovery mode from GRUB
# Or use sudo (if you have another sudo account)

sudo passwd username
```

### 2. Reset Password from Recovery Mode

```bash
# At GRUB, select "Advanced options" → "Recovery mode"
# Then select "root — Drop to root shell prompt"

# Remount root as read-write
mount -o remount,rw /

# Reset password
passwd username

# If the user doesn't exist
useradd -m username
passwd username
```

### 3. Check Account Status

```bash
# Check if account is locked or expired
sudo passwd -S username

# Locked accounts show "L" in status
# Unlock the account
sudo passwd -u username

# Check account expiry
sudo chage -l username

# Set no expiry
sudo chage -E -1 username
sudo chage -M 99999 username
```

### 4. Check PAM Configuration

```bash
# Check PAM login configuration
cat /etc/pam.d/login
cat /etc/pam.d/sshd
cat /etc/pam.d/common-auth

# Common PAM issues:
# - pam_unix.so not found
# - pam_tally2.so locking accounts
# - pam_deny.so blocking everything

# Test PAM configuration
sudo pam-auth-update
```

### 5. Check /etc/shadow

```bash
# Check if the password hash is valid
sudo cat /etc/shadow | grep username

# Valid format: username:$y$j9T...:19000:0:99999:7:::
# Invalid: username::19000:0:99999:7::: (empty password hash)

# Reset password to fix corrupted hash
sudo passwd username
```

### 6. Check /etc/passwd

```bash
# Check if the user has a valid shell
cat /etc/passwd | grep username

# The shell should exist, e.g., /bin/bash
# If it's /bin/false or /usr/sbin/nologin, the user cannot log in

# Fix the shell
sudo usermod -s /bin/bash username
```

### 7. Reset Failed Attempts Counter

```bash
# If pam_tally2 is configured, reset failed attempts
sudo pam_tally2 --user=username --reset

# For pam_faillock
sudo faillock --user username --reset
```

### 8. Boot into Single User Mode

```bash
# At GRUB, press 'e' to edit
# Find the "linux" line and add "single" or "init=/bin/bash" at the end
# Press Ctrl+X to boot

# Mount root as read-write
mount -o remount,rw /

# Fix the issue
passwd username
```

## Examples

```bash
$ sudo passwd -S username
username L 2025-06-15 0 99999 7 -1

# "L" means the account is locked

$ sudo passwd -u username
passwd: password expiry information changed.
$ sudo passwd -S username
username P 2025-06-15 0 99999 7 -1

# "P" means usable password — user can log in now
```

## Related Errors

- [PAM module error]({{< relref "/os/linux/linux-pam-error" >}}) — PAM configuration issues
- [SSH permission denied]({{< relref "/os/linux/ssh-error" >}}) — SSH authentication failures
- [/etc/shadow permission denied]({{< relref "/os/linux/linux-shadow-error" >}}) — Shadow file access issues
