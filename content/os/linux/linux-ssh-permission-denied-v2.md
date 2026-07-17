---
title: "[Solution] Linux SSH Permission Denied — publickey,password Fix"
description: "Fix Linux SSH 'Permission denied (publickey,password)' errors. Resolve SSH authentication failures and key-based login issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
tags: ["ssh", "permission-denied", "publickey", "authentication", "keys"]
weight: 5
---

# Linux: SSH — Permission denied (publickey,password)

The `Permission denied (publickey,password)` error means the SSH server rejected the client's authentication attempt. The server offered publickey and/or password authentication methods, but the client's credentials were not accepted.

## What This Error Means

SSH uses a challenge-response authentication system. The server checks whether the connecting user's public key is in `~/.ssh/authorized_keys` (for key auth) or whether the password matches the system password. If neither method succeeds, the server logs `Permission denied` and closes the connection.

## Common Causes

- Public key not added to `authorized_keys` on the server
- Incorrect file or directory permissions on `~/.ssh` or `authorized_keys`
- Wrong username specified in the SSH connection
- SSH server configured to disable password or key authentication
- SELinux or AppArmor blocking key file access
- Home directory permissions too open (e.g., 777 or group-writable)
- SSH key passphrase not provided or agent not loaded

## How to Fix

### 1. Verify Key Permissions on Server

```bash
# Correct permissions on server
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
chmod 700 ~

# Ownership
chown -R $USER:$USER ~/.ssh
```

### 2. Check authorized_keys

```bash
# Verify the key is present
cat ~/.ssh/authorized_keys

# Add your public key (from client)
cat ~/.ssh/id_rsa.pub | ssh user@server 'cat >> ~/.ssh/authorized_keys'

# Or copy it properly
ssh-copy-id user@server
```

### 3. Test with Verbose Mode

```bash
# Client-side: see exactly where authentication fails
ssh -vvv user@server

# Look for lines like:
# Offering public key: /home/user/.ssh/id_rsa
# Server accepts key: sha256:...
# Authentication succeeded (publickey)
```

### 4. Check SSH Server Configuration

```bash
# On the server, check sshd_config
sudo grep -E '^(PubkeyAuthentication|PasswordAuthentication|AuthorizedKeysFile|PermitRootLogin)' /etc/ssh/sshd_config

# Ensure key auth is enabled:
# PubkeyAuthentication yes
# AuthorizedKeysFile .ssh/authorized_keys

# Test configuration
sudo sshd -t

# Restart after changes
sudo systemctl restart sshd
```

### 5. Fix SELinux Context (RHEL/CentOS/Fedora)

```bash
# Restore correct context on .ssh directory
restorecon -Rv ~/.ssh

# Check if SELinux is blocking access
sudo ausearch -m AVC -ts recent | grep ssh
```

### 6. Generate and Copy a New Key Pair

```bash
# On client: generate a new key
ssh-keygen -t ed25519 -C 'your_email@example.com'

# Copy to server
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server

# Test login
ssh -i ~/.ssh/id_ed25519 user@server
```

## Examples

```bash
$ ssh user@example.com
user@example.com: Permission denied (publickey,password).

$ ssh -vvv user@example.com
...
Offering public key: /home/user/.ssh/id_rsa RSA SHA256:...
Server rejects key: /home/user/.ssh/id_rsa RSA SHA256:...
...
Permission denied (publickey).

# On the server
$ ls -la ~/.ssh/
drwx------ 2 user user 4096 .ssh/
-rw-r--r-- 1 user user  568 authorized_keys    # Wrong permissions

$ chmod 600 ~/.ssh/authorized_keys
$ ssh user@example.com
Welcome to Ubuntu 22.04 LTS
```

## Related Errors

- [SSH connection refused]({{< relref "/os/linux/linux-ssh-connection-refused" >}}) — Server not accepting connections
- [SSH timeout]({{< relref "/os/linux/linux-ssh-timeout-v2" >}}) — Connection timed out
- [SSH host key]({{< relref "/os/linux/linux-ssh-host-key-v2" >}}) — Host key verification failed
