---
title: "[Solution] Linux 'Connection Refused' — ECONNREFUSED Fix"
description: "Fix Linux 'Connection refused' errors. Resolve issues with services not running, firewall blocking, and port configuration problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: Connection Refused

The `Connection refused` error means the client attempted to connect to a server, but the server actively rejected the connection. This typically happens when no service is listening on the target port, a firewall is blocking the connection, or the service crashed. Unlike a timeout (which means nothing responded), "refused" means something answered but said "no."

## Common Causes

- Service is not running or crashed on the target port
- Service is bound to a different interface (e.g., localhost instead of 0.0.0.0)
- Firewall (iptables/nftables/firewalld) is blocking the port
- Service is listening on a different port than expected
- Too many connections and the service's backlog is full

## How to Fix

### 1. Check if the Service Is Running

```bash
# Check if the service is active
sudo systemctl status nginx
sudo systemctl status sshd

# Check all listening services
sudo ss -tlnp

# Or use netstat
sudo netstat -tlnp
```

Example output:

```
LISTEN  0  128  0.0.0.0:443  0.0.0.0:*  users:(("nginx",pid=1234,fd=6))
LISTEN  0  128  127.0.0.1:8080  0.0.0.0:*  users:(("myapp",pid=5678,fd=3))
```

If the service is not listed, start it:

```bash
sudo systemctl start nginx
```

### 2. Check the Binding Address

A service bound to `127.0.0.1` (localhost) only accepts connections from the local machine:

```bash
# Check what address the service is bound to
sudo ss -tlnp | grep :80
```

If it shows `127.0.0.1:80`, change the service configuration to bind to `0.0.0.0:80` (all interfaces) to accept remote connections.

### 3. Check Firewall Rules

```bash
# Check iptables rules
sudo iptables -L -n -v

# Check if the port is blocked
sudo iptables -L INPUT -n | grep PORT_NUMBER

# Allow a specific port through the firewall
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# With firewalld
sudo firewall-cmd --list-all
sudo firewall-cmd --add-port=80/tcp --permanent
sudo firewall-cmd --reload

# With ufw (Ubuntu)
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

### 4. Check the Service Logs

```bash
# Check service-specific logs
sudo journalctl -u nginx -f
sudo journalctl -u sshd -f

# Check for errors
sudo journalctl -u nginx --since "1 hour ago" | grep -i error
```

### 5. Test Connectivity

```bash
# Test if the port is open from the server
nc -zv localhost 80

# Test from a remote machine
nc -zv server-ip 80

# Check if the service responds
curl -v http://server-ip:80
telnet server-ip 80
```

### 6. Check Connection Limits

If the service is running but refusing connections due to capacity:

```bash
# Check current connections
ss -s

# Check if the service backlog is full
sudo ss -tlnp | grep :80
```

Increase the backlog in the service configuration if needed.

## Examples

```bash
$ curl http://localhost:8080
curl: (7) Failed to connect to localhost port 8080: Connection refused

$ sudo ss -tlnp | grep 8080
# No output — nothing listening on 8080

$ sudo systemctl start myapp
$ sudo ss -tlnp | grep 8080
LISTEN  0  128  0.0.0.0:8080  0.0.0.0:*  users:(("myapp",pid=1234,fd=3))

$ curl http://localhost:8080
{"status": "ok"}
```

## Related Errors

- [SSH connection issues]({{< relref "/os/linux/ssh-error" >}}) — SSH-specific connection problems
- [iptables errors]({{< relref "/os/linux/iptables-error" >}}) — Firewall rule problems
- [NFS not responding]({{< relref "/os/linux/nfs-error" >}}) — Network filesystem timeout
