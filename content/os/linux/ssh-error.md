---
title: "[Solution] Linux SSH 'Permission denied' / 'Connection reset' Fix"
description: "Fix Linux SSH 'Permission denied' and 'Connection reset by peer' errors. Resolve SSH authentication, key, and configuration issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["ssh", "permission-denied", "connection-reset", "authentication", "sshd"]
weight: 5
---

# Linux: SSH - Permission denied / Connection reset

The SSH `Permission denied (publickey,password)` error means the SSH server rejected your login attempt because the authentication failed. The `Connection reset by peer` error means the server abruptly closed the connection, often due to misconfiguration, too many authentication attempts, or security policy violations. Both are common SSH access issues.

## Common Causes

- Incorrect password or username
- SSH key not configured or not authorized on the server
- `PermitRootLogin` set to `no` in sshd_config
- `PubkeyAuthentication` disabled on the server
- Incorrect permissions on `~/.ssh` directory or keys
- Too many failed attempts triggering fail2ban or firewall
- `MaxAuthTries` exceeded

## How to Fix

### 1. Check SSH Server Logs

```bash
# On the server, check SSH logs
sudo journalctl -u sshd -f
sudo tail -f /var/log/auth.log    # Debian/Ubuntu
sudo tail -f /var/log/secure      # RHEL/CentOS
```

Look for messages like `Failed password`, `Invalid user`, or `Connection closed`.

### 2. Fix SSH Key Permissions

```bash
# On the client
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_rsa.pub

# On the server
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
chmod 755 ~
```

### 3. Copy SSH Key to Server

```bash
# From the client machine
ssh-copy-id -i ~/.ssh/id_rsa.pub user@server

# Or manually
cat ~/.ssh/id_rsa.pub | ssh user@server "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"

# Set correct permissions on server
ssh user@server "chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys"
```

### 4. Check SSH Server Configuration

```bash
# On the server, check sshd_config
sudo grep -E 'PermitRootLogin|PubkeyAuthentication|PasswordAuthentication|MaxAuthTries' /etc/ssh/sshd_config

# Ensure these settings allow your login method
# PermitRootLogin yes              (or "prohibit-password" for key-only)
# PubkeyAuthentication yes
# PasswordAuthentication yes       (or "no" for key-only)
# MaxAuthTries 6

# After changes, restart sshd
sudo systemctl restart sshd
```

### 5. Check for fail2ban or Firewall Blocks

```bash
# Check fail2ban status
sudo fail2ban-client status sshd

# Unban an IP if accidentally banned
sudo fail2ban-client set sshd unbanip 192.168.1.100

# Check iptables for SSH blocks
sudo iptables -L -n | grep 22

# Remove a blocking rule
sudo iptables -D INPUT -s 192.168.1.100 -j DROP
```

### 6. Debug SSH Connection

```bash
# Run SSH in verbose mode
ssh -vvv user@server

# This shows exactly where the authentication fails
# Look for: "Offering public key", "Server accepts key", "Authentication succeeded"
```

### 7. Fix Connection Reset Issues

```bash
# Check if MaxSessions or MaxStartups is reached
sudo grep -E 'MaxSessions|MaxStartups|LoginGraceTime' /etc/ssh/sshd_config

# Increase limits if needed
sudo sed -i 's/#MaxSessions 10/MaxSessions 50/' /etc/ssh/sshd_config
sudo sed -i 's/#MaxStartups 10:30:100/MaxStartups 50:30:200/' /etc/ssh/sshd_config
sudo systemctl restart sshd
```

### 8. Generate New SSH Keys

If keys are corrupted:

```bash
# Generate a new Ed25519 key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Copy the new key to the server
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server
```

## Examples

```bash
$ ssh user@server
Permission denied (publickey,password).

$ ssh -vvv user@server
...
debug1: Authentications that can continue: publickey,password
debug1: Next authentication method: publickey
debug1: Trying private key: /home/user/.ssh/id_rsa
debug1: Trying private key: /home/user/.ssh/id_ed25519
debug1: No more authentication methods to try.
Permission denied (publickey,password).

# Fix: copy the key
$ ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server
$ ssh user@server
Welcome to Ubuntu 22.04!
```

## Related Errors

- [Permission denied]({{< relref "/os/linux/permission-denied10" >}}) — General permission issues
- [Connection refused]({{< relref "/os/linux/connection-refused7" >}}) — SSH service not running
- [Too many open files]({{< relref "/os/linux/too-many-open-files" >}}) — SSH connection limit reached
