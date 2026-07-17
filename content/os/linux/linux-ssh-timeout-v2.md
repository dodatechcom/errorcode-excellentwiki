---
title: "[Solution] Linux SSH Connection Timed Out — Fix"
description: "Fix Linux SSH 'Connection timed out' errors. Resolve SSH connection timeouts caused by network, firewall, or server issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Linux: SSH — Connection timed out

The `Connection timed out` or `ssh: connect to host <host> port 22: Connection timed out` error means the TCP connection to the SSH server could not be established within the timeout period. This is different from a refused connection — the packets are being silently dropped.

## What This Error Means

SSH relies on a TCP connection to port 22 (by default). A timeout indicates the SYN packets sent to establish the connection are not receiving a response. The server may be unreachable, a firewall may be dropping packets, or the server process may not be listening on the expected interface or port.

## Common Causes

- Firewall blocking port 22 (iptables, nftables, cloud security groups)
- Server is down or network is unreachable
- SSH server listening on a different port
- DNS resolution pointing to the wrong IP address
- Routing issue between client and server
- SSH server overloaded or at connection limit
- VPN or proxy not routing traffic correctly

## How to Fix

### 1. Test Basic Connectivity

```bash
# Ping the host
ping -c 4 <host>

# Test the specific port with netcat
nc -zv <host> 22

# Or with nmap
nmap -p 22 <host>

# Traceroute to find where packets stop
traceroute <host>
```

### 2. Check Firewall on Server

```bash
# Check iptables rules
sudo iptables -L -n | grep 22

# Check firewalld
sudo firewall-cmd --list-all

# Check ufw
sudo ufw status

# Allow SSH port
sudo ufw allow 22/tcp
```

### 3. Verify SSH Server Is Running

```bash
# On the server
sudo systemctl status sshd

# Check what port it is listening on
sudo ss -tlnp | grep sshd

# Check if bound to specific IP
sudo ss -tlnp | grep ':22'
```

### 4. Check Cloud Security Groups (AWS/GCP/Azure)

```bash
# AWS CLI: check security group rules
aws ec2 describe-security-groups --group-ids sg-xxxxx

# Ensure inbound rule exists:
# Type: SSH, Port: 22, Source: 0.0.0.0/0 (or specific IP)
```

### 5. Try a Different Port

```bash
# If SSH runs on a non-standard port
ssh -p 2222 user@host

# Scan for open ports
nmap -p 1-65535 <host>

# Or check common SSH ports
for port in 22 2222 2200 8022; do
  nc -zv <host> $port 2>&1
done
```

### 6. Check DNS Resolution

```bash
# Verify DNS resolves correctly
dig <host>
nslookup <host>

# Try connecting by IP directly
ssh user@<ip-address>

# Check /etc/hosts for overrides
grep <host> /etc/hosts
```

### 7. Increase Client Timeout

```bash
# Set a longer timeout
ssh -o ConnectTimeout=30 user@host

# Or set in ~/.ssh/config
# Host myserver
#     ConnectTimeout 30
#     ServerAliveInterval 15
#     ServerAliveCountMax 3
```

## Examples

```bash
$ ssh user@192.168.1.100
ssh: connect to host 192.168.1.100 port 22: Connection timed out

$ nc -zv 192.168.1.100 22
nc: connect to 192.168.1.100 port 22 (tcp) timed out: Operation now in progress

$ ping -c 2 192.168.1.100
PING 192.168.1.100: 64 bytes, icmp_seq=1 timeout

# On server, firewall was blocking
$ sudo iptables -L INPUT -n
Chain INPUT (policy DROP)
tcp -- 0.0.0.0/0  0.0.0.0/0  tcp dpt:22 REJECT

$ sudo iptables -D INPUT -p tcp --dport 22 -j REJECT
$ nc -zv 192.168.1.100 22
Connection to 192.168.1.100 22 port [tcp/ssh] succeeded!
```

## Related Errors

- [SSH connection refused]({{< relref "/os/linux/linux-ssh-connection-refused" >}}) — Server actively refuses connections
- [SSH permission denied]({{< relref "/os/linux/linux-ssh-permission-denied-v2" >}}) — Authentication rejected
- [SSH host key]({{< relref "/os/linux/linux-ssh-host-key-v2" >}}) — Host key verification failed
