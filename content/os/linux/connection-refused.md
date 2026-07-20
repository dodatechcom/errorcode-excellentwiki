---
title: "[Solution] Linux: connection-refused — connection refused error"
description: "Fix Linux connection-refused errors. connection refused error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 6
---
# Linux: Connection Refused

"Connection refused" (ECONNREFUSED) means no process is listening on the target port, or the port is blocked by a firewall.

## Common Causes

- The target service is not running (not started or crashed)
- Service is listening on a different port or IP address
- Firewall (iptables, nftables) is blocking the connection
- hosts.deny or TCP wrappers blocking the client
- The port is filtered or blocked by intermediate firewall

## How to Fix

### 1. Check if Service is Listening

```bash
sudo ss -tlnp | grep :<port>
sudo netstat -tulpn | grep :<port>
```

### 2. Check Service Status

```bash
sudo systemctl status <service>
sudo systemctl start <service>
```

### 3. Check Firewall Rules

```bash
sudo iptables -L -n | grep <port>
sudo nft list ruleset | grep <port>
sudo firewall-cmd --list-all
```

### 4. Test Local Connectivity

```bash
telnet localhost <port>
nc -zv localhost <port>
```

## Examples

```bash
$ curl http://localhost:8080
curl: (7) Failed to connect to localhost port 8080: Connection refused

$ sudo ss -tlnp | grep 8080
# No output - nothing listening on port 8080

$ sudo systemctl start myapp
$ curl http://localhost:8080
# Now succeeds
```
