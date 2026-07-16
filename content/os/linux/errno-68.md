---
title: "[Solution] Linux ECONNRESET (errno 68) — Connection Reset by Peer Fix"
description: "Fix Linux ECONNRESET (errno 68) Connection reset by peer error. Solutions for connection reset and peer issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["econnreset", "connection", "errno-68", "reset", "peer"]
weight: 5
---

# Linux ECONNRESET (errno 68) — Connection Reset by Peer

ECONNRESET (errno 68) means the remote peer forcibly closed the connection. This error occurs when the remote side sends a TCP RST packet, indicating it has terminated the connection unexpectedly. It is distinct from ECONNABORTED (errno 67) because ECONNRESET is triggered by the remote peer, not the local machine.

## Common Causes

- Remote server crashed or restarted unexpectedly
- Remote application closed the connection prematurely
- Network device sent a reset (firewall, NAT, load balancer)
- Remote process ran out of resources

## How to Fix ECONNRESET

### 1. Check Server Status

Verify the remote server is running:

```bash
ping server.example.com
ssh server.example.com "systemctl status application"
```

### 2. Check Server Logs

Look for crashes or errors on the remote server:

```bash
ssh server.example.com "journalctl -u application --since '1 hour ago'"
ssh server.example.com "dmesg | tail -50"
```

### 3. Adjust Client-Side Keepalive

Enable keepalive on the client to detect dead connections:

```bash
ssh -o ServerAliveInterval=60 user@server
```

### 4. Check Firewall Rules

Ensure the firewall allows the connection:

```bash
sudo iptables -L -n | grep -i "80\|443\|8080"
sudo ufw status
```

### 5. Use Persistent Connections

For applications, implement connection pooling:

```bash
# In curl, use connection pooling
curl --keepalive-time 60 http://server/api
```

## Verification

After resolving the issue, confirm the connection works:

```bash
ss -t state established | grep server
curl -v http://server/api
```

## Related Error Codes

- [ECONNABORTED (errno 67)](/os/linux/errno-67/) — Software caused connection abort
- [ETIMEDOUT (errno 74)](/os/linux/errno-74/) — Connection timed out
- [ECONNREFUSED (errno 75)](/os/linux/errno-75/) — Connection refused
