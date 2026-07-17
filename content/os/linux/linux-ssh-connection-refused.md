---
title: "[Solution] Linux SSH Connection Refused — Fix"
description: "Fix Linux 'ssh: connect to host <host> port 22: Connection refused' errors. Ensure SSH server is running and accessible."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: ssh: Connection refused

The `ssh: connect to host <host> port 22: Connection refused` error means the SSH client reached the host but no service is listening on the specified port. This is different from a timeout — the TCP handshake completed but was immediately rejected because nothing is listening on port 22.

## Common Causes

- SSH server (sshd) not installed or not running
- SSH service not started after installation
- SSH daemon crashed or failed to start
- Firewall blocking port 22
- SSH configured to listen on a non-default port
- Host is not the intended target (wrong IP)

## How to Fix

### 1. Check If SSH Server Is Running

```bash
# On the server, check sshd status
sudo systemctl status sshd
# or
sudo systemctl status ssh

# Try connecting locally
ssh localhost
```

### 2. Start or Enable the SSH Server

```bash
# Debian/Ubuntu
sudo systemctl start ssh
sudo systemctl enable ssh

# RHEL/CentOS/Fedora
sudo systemctl start sshd
sudo systemctl enable sshd
```

### 3. Install SSH Server If Missing

```bash
# Debian/Ubuntu
sudo apt update && sudo apt install openssh-server

# RHEL/CentOS/Fedora
sudo dnf install openssh-server
# or
sudo yum install openssh-server
```

### 4. Check Which Port SSH Is Listening On

```bash
# Check if sshd is listening
sudo ss -tlnp | grep ssh

# Check the configured port
sudo grep Port /etc/ssh/sshd_config

# If using a non-default port, connect with -p
ssh -p 2222 user@host
```

### 5. Check Firewall Rules

```bash
# Check iptables
sudo iptables -L -n | grep 22

# Check firewalld
sudo firewall-cmd --list-all | grep ssh

# Check ufw
sudo ufw status | grep 22

# Allow SSH through the firewall
sudo ufw allow ssh
sudo firewall-cmd --add-service=ssh --permanent
sudo firewall-cmd --reload
```

### 6. Check if Another Service Is on Port 22

```bash
# Check what's using port 22
sudo ss -tlnp | grep :22

# If something else is using port 22, resolve the conflict
```

## Examples

```bash
$ ssh user@server
ssh: connect to host server port 22: Connection refused

$ sudo systemctl status sshd
● sshd.service - OpenSSH server daemon
     Loaded: loaded (/usr/lib/systemd/system/sshd.service; disabled)
     Active: inactive (dead)

$ sudo systemctl start sshd
$ sudo systemctl enable sshd
$ ssh user@server
Welcome to Ubuntu 22.04!
```

```bash
$ ssh -p 2222 user@server
ssh: connect to host server port 2222: Connection refused

$ sudo grep Port /etc/ssh/sshd_config
#Port 22
# Port 2222 (if uncommented, this is the port being used)
```

## Related Errors

- [SSH permission denied]({{< relref "/os/linux/ssh-error" >}}) — Authentication failures
- [SSH host key verification failed]({{< relref "/os/linux/linux-ssh-host-key" >}}) — Host key mismatch
- [SSH connection timed out]({{< relref "/os/linux/linux-ssh-timeout" >}}) — Network unreachable
