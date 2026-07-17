---
title: "[Solution] Linux SSH Permission Denied — Authentication Fix"
description: "Fix Linux SSH 'Permission denied (publickey)' errors. Resolve key authentication issues, password login failures, and sshd configuration problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: SSH Permission denied

The `Permission denied (publickey)` error means the SSH server rejected all authentication methods offered by the client. This typically means your SSH key was not accepted (not in `authorized_keys`), or password authentication is disabled.

## Common Causes

- SSH public key not added to `~/.ssh/authorized_keys` on the server
- Incorrect permissions on `~/.ssh` or `authorized_keys` on either side
- `PasswordAuthentication` set to `no` in sshd_config
- `PubkeyAuthentication` set to `no` in sshd_config
- Wrong username used for authentication
- SELinux blocking SSH key access

## How to Fix

### 1. Check SSH Server Configuration

```bash
# On the server, check authentication settings
sudo grep -E 'PubkeyAuthentication|PasswordAuthentication|PermitRootLogin|AuthorizedKeysFile' /etc/ssh/sshd_config

# Ensure these settings:
# PubkeyAuthentication yes
# PasswordAuthentication yes  (if you want password login)
# AuthorizedKeysFile .ssh/authorized_keys
```

### 2. Fix SSH Directory and File Permissions

**On the server:**

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
chmod 755 ~
```

**On the client:**

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_rsa.pub
```

### 3. Add Your SSH Key to the Server

```bash
# Use ssh-copy-id (simplest)
ssh-copy-id user@server

# Or manually
cat ~/.ssh/id_rsa.pub | ssh user@server "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"

# Verify the key was added
ssh user@server "cat ~/.ssh/authorized_keys"
```

### 4. Verify the Key Pair

```bash
# Check that the public and private keys match
ssh-keygen -y -f ~/.ssh/id_rsa | diff - ~/.ssh/id_rsa.pub

# If they don't match, regenerate:
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N ""
```

### 5. Use Verbose Mode to Debug

```bash
# Run SSH with maximum verbosity
ssh -vvv user@server

# Look for:
# - Which keys are offered
# - Whether the server accepts them
# - Which authentication methods are allowed
```

### 6. Check SELinux Contexts (RHEL/CentOS/Fedora)

```bash
# On the server, check SELinux context of ~/.ssh
ls -Z ~/.ssh/authorized_keys

# Restore SELinux context if needed
sudo restorecon -Rv ~/.ssh

# Check for SELinux denials
sudo ausearch -m AVC -ts recent | grep ssh
```

### 7. Check Home Directory Permissions

```bash
# The home directory must not be writable by group/others
chmod go-w ~/

# The .ssh directory must be owned by the user
chown -R $USER:$USER ~/.ssh
```

## Examples

```bash
$ ssh -vvv user@server
debug1: Authentications that can continue: publickey
debug1: Next authentication method: publickey
debug1: Offering public key: /home/user/.ssh/id_ed25519
debug1: Server accepts key: /home/user/.ssh/id_ed25519
debug1: Authentication succeeded (publickey).
Welcome to Ubuntu 22.04!

# If it fails:
debug1: Authentications that can continue: publickey
debug1: Trying private key: /home/user/.ssh/id_rsa
debug1: No more authentication methods to try.
Permission denied (publickey).
```

## Related Errors

- [SSH connection refused]({{< relref "/os/linux/linux-ssh-connection-refused" >}}) — SSH server not running
- [SSH host key verification failed]({{< relref "/os/linux/linux-ssh-host-key" >}}) — Host key mismatch
- [SELinux denied]({{< relref "/os/linux/selinux-denied" >}}) — SELinux blocking access
