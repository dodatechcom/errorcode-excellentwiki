---
title: "[Solution] Linux PAM Module Error — Authentication Fix"
description: "Fix Linux PAM 'module error' and authentication failures. Resolve PAM configuration issues, module loading errors, and login problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["pam", "module-error", "authentication", "login", "pam_unix", "pam_deny"]
weight: 5
---

# Linux: PAM: module error

The `PAM: module error` message means the Pluggable Authentication Module (PAM) system encountered a problem loading or executing an authentication module. PAM handles authentication for login, sudo, ssh, and other services. When a PAM module fails, users may be unable to log in, use sudo, or authenticate to services.

## What This Error Means

PAM is a framework that allows system administrators to configure authentication methods without recompiling applications. PAM modules (`.so` files in `/lib/security/` or `/lib/x86_64-linux-gnu/security/`) are loaded by configuration files in `/etc/pam.d/`. When a module file is missing, has wrong permissions, has dependency issues, or its configuration is invalid, PAM reports a module error.

## Common Causes

- PAM module file missing or corrupted
- Wrong permissions on PAM module files
- Missing shared library dependencies for PAM module
- Syntax error in PAM configuration file (`/etc/pam.d/`)
- Module version mismatch with PAM library
- Disk full preventing module loading
- Conflicting PAM modules from different packages

## How to Fix

### 1. Check PAM Module Files

```bash
# List installed PAM modules
ls /lib/security/pam_*.so 2>/dev/null
ls /lib/x86_64-linux-gnu/security/pam_*.so 2>/dev/null

# Check if the specific module exists
ls -la /lib/security/pam_unix.so

# Check module permissions
ls -la /lib/security/pam_*.so | head -10
# Should be: -rw-r--r-- (readable by all)
```

### 2. Fix Module Permissions

```bash
# PAM modules should be readable by all
sudo chmod 644 /lib/security/pam_*.so
sudo chmod 644 /lib/x86_64-linux-gnu/security/pam_*.so
```

### 3. Check PAM Configuration Files

```bash
# Check the PAM configuration for the service
cat /etc/pam.d/common-auth
cat /etc/pam.d/system-auth

# Look for syntax errors or typos
# Common format: <type> <control> <module> [options]
# Example: auth sufficient pam_unix.so

# Validate the PAM configuration
sudo pam_tally2 --user=root --reset  # Reset login counters
```

### 4. Reinstall PAM Packages

```bash
# Debian/Ubuntu
sudo apt install --reinstall libpam0g libpam-modules libpam-modules-bin

# RHEL/CentOS/Fedora
sudo dnf reinstall pam
```

### 5. Fix Missing Module Dependencies

```bash
# Check what libraries the module needs
ldd /lib/security/pam_unix.so

# Install missing libraries
sudo apt install libnss-files    # For pam_unix
sudo apt install libpam-cap      # For pam_cap
```

### 6. Fix Common PAM Configuration Errors

```bash
# Common mistake: missing required module
# Wrong: only sufficient modules, no required
# auth sufficient pam_permit.so
# auth sufficient pam_deny.so     # This denies everyone

# Correct: ensure at least one required module
# auth required pam_unix.so
# auth sufficient pam_permit.so

# Fix the configuration
sudo nano /etc/pam.d/common-auth
```

### 7. Debug PAM Issues

```bash
# Enable PAM debug logging
# Add to /etc/pam.d/<service>:
# auth optional pam_debug.so

# Check system logs for PAM errors
sudo journalctl | grep -i pam
sudo grep pam /var/log/auth.log
```

### 8. Emergency PAM Recovery

If locked out of the system:

```bash
# Boot from live USB
sudo mount /dev/sda1 /mnt
sudo chroot /mnt

# Fix PAM configuration
nano /etc/pam.d/common-auth

# Or temporarily allow root login
# Add: auth sufficient pam_permit.so
# at the top of /etc/pam.d/common-auth
```

## Examples

```bash
$ sudo su
su: Authentication failure

$ sudo journalctl | grep pam
Jun 15 10:00:00 host sshd[1234]: PAM: Authentication failure for user from 192.168.1.100

$ ls -la /lib/security/pam_unix.so
-rw-r--r-- 1 root root 53248 Jan  1 00:00 /lib/security/pam_unix.so

$ sudo apt install --reinstall libpam-modules
$ sudo systemctl restart sshd
```

```bash
$ sudo nano /etc/pam.d/common-auth
# Found: auth sufficient pam_deny.so
# This blocks all authentication!

# Fix: change to
# auth required pam_unix.so
# auth requisite pam_deny.so

$ sudo login
# Login works now
```

## Related Errors

- [Login authentication failure]({{< relref "/os/linux/linux-login-error" >}}) — Authentication failures
- [sudo not in sudoers]({{< relref "/os/linux/linux-sudo-error" >}}) — Permission issues
- [Permission denied]({{< relref "/os/linux/connection-refused7" >}}) — General access issues
