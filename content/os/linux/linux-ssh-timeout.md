---
title: "[Solution] Linux SSH Connection Timed Out — Fix"
description: "Fix Linux 'ssh: connect to host <host> port 22: Connection timed out' errors. Diagnose network path issues and firewall blocks."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: ssh: Connection timed out

The `ssh: connect to host <host> port 22: Connection timed out` error means the SSH client cannot reach the server at all. Unlike "connection refused," the TCP handshake never completed — the client sent SYN packets but never received a response.

## Common Causes

- Firewall blocking outbound or inbound port 22
- Server is powered off, crashed, or unreachable
- Network route to the server does not exist
- Wrong IP address or hostname
- NAT or VPN configuration issues
- ISP or cloud provider blocking the port

## How to Fix

### 1. Check Basic Connectivity

```bash
# Ping the server
ping -c 4 server

# Trace the network route
traceroute server

# Check if port 22 is reachable
nc -zv -w 5 server 22
```

### 2. Check Firewall on Both Sides

**On the client (outbound):**

```bash
# Check if local firewall allows outbound SSH
sudo iptables -L OUTPUT -n | grep 22
sudo ufw status

# Temporarily disable firewall for testing
sudo ufw disable    # Test only — re-enable after
```

**On the server (inbound):**

```bash
# Ensure port 22 is open
sudo iptables -L INPUT -n | grep 22

# If using firewalld
sudo firewall-cmd --list-all

# Allow SSH
sudo firewall-cmd --add-service=ssh --permanent
sudo firewall-cmd --reload

# If using ufw
sudo ufw allow ssh
```

### 3. Check Cloud Provider Security Groups (AWS/GCP/Azure)

```bash
# AWS: Check security group inbound rules
aws ec2 describe-security-groups --group-ids sg-xxxxx

# Ensure TCP port 22 is allowed from your IP
# Example: 22 (SSH) from 203.0.113.0/32
```

### 4. Try Different Ports or Protocols

```bash
# Try SSH on a different port
ssh -p 2222 user@server

# Try connecting over IPv4 or IPv6 explicitly
ssh -4 user@server
ssh -6 user@server
```

### 5. Check DNS Resolution

```bash
# Verify hostname resolves
nslookup server
dig server

# Try using the IP directly
ssh user@192.168.1.100
```

### 6. Increase SSH Timeout

```bash
# Set a longer connection timeout
ssh -o ConnectTimeout=30 user@server

# Or set in ~/.ssh/config
echo "Host *
    ConnectTimeout 30" >> ~/.ssh/config
```

### 7. Check NAT and VPN

```bash
# If behind a VPN, check the VPN connection
ip addr show tun0
ping -c 4 server

# Check NAT mappings
sudo iptables -t nat -L -n
```

## Examples

```bash
$ ssh user@server
ssh: connect to host server port 22: Connection timed out

$ ping -c 4 server
PING server (192.168.1.100) 56(84) bytes of data.
From 192.168.1.1 icmp_seq=1 Destination Host Unreachable

$ traceroute server
traceroute to server (192.168.1.100), 30 hops max
 1  192.168.1.1  1.234 ms  1.456 ms  1.567 ms
 2  * * *
 3  * * *

# Server is down or the route is blocked
```

```bash
$ nc -zv -w 5 server 22
nc: connect to server port 22 (tcp) timed out: Operation now in progress

$ ssh -o ConnectTimeout=5 user@server
ssh: connect to host server port 22: Connection timed out
```

## Related Errors

- [SSH connection refused]({{< relref "/os/linux/linux-ssh-connection-refused" >}}) — SSH server not listening
- [SSH permission denied]({{< relref "/os/linux/linux-ssh-permission-denied" >}}) — Authentication failures
- [NFS server not responding]({{< relref "/os/linux/nfs-error" >}}) — General network timeouts
