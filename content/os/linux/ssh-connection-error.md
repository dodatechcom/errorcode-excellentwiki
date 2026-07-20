---
title: "[Solution] Linux: ssh-connection-error — SSH connection refused"
description: "Fix Linux ssh-connection-error errors. SSH connection refused with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 8
---

# Linux: SSH Connection Error Error

SSH connection error errors occur during SSH connection establishment due to configuration or authentication issues.

## Common Causes

- SSH server not running or not accessible
- Firewall blocking port 22
- Authentication method mismatch
- Host key verification failure
- Client configuration errors

## How to Fix

### 1. Check SSH Server Status

```bash
sudo systemctl status sshd
sudo ss -tlnp | grep :22
```

### 2. Check Firewall

```bash
sudo ufw status
sudo iptables -L -n | grep :22
```

### 3. Verbose Connection Debug

```bash
ssh -vvv user@remote-host 2>&1 | tail -30
```

### 4. Check SSH Configuration

```bash
cat /etc/ssh/sshd_config | grep -v "^#" | grep -v "^$"
cat ~/.ssh/config
```

## Examples

```bash
$ sudo systemctl status sshd
* sshd.service - OpenSSH server daemon
   Active: active (running)

$ ssh -vvv user@remote-host
debug1: Authentication succeeded (publickey).
debug1: channel 0: new [client-session]
$ ssh user@remote-host
Welcome to Ubuntu 22.04 LTS
```
