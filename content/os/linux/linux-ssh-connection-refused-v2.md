---
title: "[Solution] Linux SSH Connection Refused — Port Fix v2"
description: "Fix Linux 'ssh: Connection refused' errors. Check SSH service status, firewall rules, and port configuration to restore remote access."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["ssh", "connection-refused", "sshd", "port-22", "firewall", "remote-access"]
weight: 5
---

# Linux: ssh: Connection refused

The `ssh: Connection refused` error means the SSH client attempted to connect to the server but the server actively rejected the connection. Unlike a timeout (which means nothing responded), "refused" means something answered but the port is not accepting connections. This typically means the SSH daemon is not running, is listening on a different port, or a firewall is blocking the connection.

## What This Error Means

When you run `ssh user@host`, the client sends a TCP SYN to port 22 on the target. If no service is listening on that port, the kernel responds with a TCP RST (reset), which your client interprets as "Connection refused." This is different from `Connection timed out` (no response at all) or `No route to host` (network unreachable).

## Common Causes

- sshd service is not running on the remote host
- sshd is listening on a non-standard port
- Firewall (iptables, ufw, firewalld) blocking port 22
- SSH configuration has `ListenAddress` bound to wrong interface
- Too many connections exceeding MaxStartups limit
- SELinux blocking sshd

## How to Fix

### 1. Check if SSH Service Is Running

On the remote server (if accessible):

```bash
# Check sshd status
sudo systemctl status sshd

# Start sshd if not running
sudo systemctl start sshd
sudo systemctl enable sshd

# Check if sshd is listening
sudo ss -tlnp | grep :22
```

### 2. Check Firewall Rules

```bash
# Check iptables
sudo iptables -L INPUT -n | grep 22

# Allow SSH through firewall
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# With ufw (Ubuntu)
sudo ufw allow ssh
sudo ufw allow 22/tcp

# With firewalld (RHEL/CentOS)
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

### 3. Check sshd Configuration

```bash
# Verify sshd is listening on the correct port and interface
sudo grep -E 'Port|ListenAddress' /etc/ssh/sshd_config

# Default is Port 22 and ListenAddress 0.0.0.0
# If changed, ensure the client connects to the right port
ssh -p <port> user@host
```

### 4. Verify Network Connectivity

```bash
# Test if port 22 is open
nc -zv host 22
telnet host 22

# Check if the host is reachable
ping host

# Check DNS resolution
nslookup host
```

### 5. Check MaxStartups Limit

```bash
# If too many concurrent SSH connections
sudo grep MaxStartups /etc/ssh/sshd_config

# Default is 10:30:100 — increase if needed
# MaxStartups 50:30:200
sudo systemctl restart sshd
```

### 6. Check SELinux (RHEL/CentOS/Fedora)

```bash
# Check if SELinux is blocking sshd
sudo ausearch -m AVC -ts recent | grep ssh

# Restore sshd SELinux context
sudo restorecon -Rv /etc/ssh
sudo restorecon -Rv /var/run/sshd
```

### 7. Restart sshd and Check Logs

```bash
# Restart sshd
sudo systemctl restart sshd

# Check logs for errors
sudo journalctl -u sshd --since "10 minutes ago"
sudo tail -f /var/log/auth.log
```

## Examples

```bash
$ ssh user@192.168.1.100
ssh: connect to host 192.168.1.100 port 22: Connection refused

$ nc -zv 192.168.1.100 22
nc: connect to 192.168.1.100 port 22 (tcp) failed: Connection refused

# On the remote server:
$ sudo systemctl status sshd
● sshd.service - OpenSSH server daemon
     Active: inactive (dead)

$ sudo systemctl start sshd
$ sudo systemctl status sshd
● sshd.service - OpenSSH server daemon
     Active: active (running)

# From client:
$ ssh user@192.168.1.100
user@192.168.1.100's password:
```

```bash
# SSH on non-standard port
$ ssh user@192.168.1.100
ssh: connect to host 192.168.1.100 port 22: Connection refused

$ ssh -p 2222 user@192.168.1.100
Welcome to Ubuntu 22.04!
```

## Related Errors

- [SSH permission denied]({{< relref "/os/linux/linux-ssh-permission-denied" >}}) — Authentication failures
- [SSH host key verification]({{< relref "/os/linux/linux-ssh-host-key-v2" >}}) — Host key mismatch
- [Connection refused]({{< relref "/os/linux/connection-refused7" >}}) — General connection refused errors
- [iptables errors]({{< relref "/os/linux/linux-iptables-error" >}}) — Firewall rule issues
