---
title: "[Solution] Linux ECONNREFUSED (errno 75) — Connection Refused Fix"
description: "Fix Linux ECONNREFUSED (errno 75) Connection refused error. Solutions for connection refusal and server issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux ECONNREFUSED (errno 75) — Connection Refused

ECONNREFUSED (errno 75) means the remote host actively refused the connection. This error occurs when a client tries to connect to a port where no server is listening, or the server's backlog queue is full. It is distinct from ETIMEDOUT (errno 74) because ECONNREFUSED means the remote host sent a TCP RST, while ETIMEDOUT means no response was received.

## Common Causes

- No server process listening on the target port
- Server process crashed or was not started
- Server backlog queue is full
- Firewall rejecting connections with RST instead of dropping

## How to Fix ECONNREFUSED

### 1. Verify Server is Running

Check if the server process is active:

```bash
ss -tlnp | grep <port>
netstat -tlnp | grep <port>
systemctl status service_name
```

### 2. Start the Server

If the server is not running, start it:

```bash
sudo systemctl start service_name
sudo service service_name start
```

### 3. Check Server Bind Address

Ensure the server is listening on the correct interface:

```bash
ss -tlnp | grep <port>
# 0.0.0.0:port = all interfaces
# 127.0.0.1:port = localhost only
```

### 4. Increase Server Backlog

If the backlog is full, increase it:

```bash
sudo sysctl -w net.core.somaxconn=65535
sudo sysctl -w net.ipv4.tcp_max_syn_backlog=65535
```

### 5. Check Firewall Rules

Ensure the firewall allows connections on the port:

```bash
sudo iptables -L -n | grep <port>
sudo ufw status
sudo firewall-cmd --list-all
```

## Verification

After fixing the server, confirm the connection succeeds:

```bash
curl http://localhost:<port>/
ss -tlnp | grep <port>
```

## Related Error Codes

- [ETIMEDOUT (errno 74)](/os/linux/errno-74/) — Connection timed out
- [ECONNRESET (errno 68)](/os/linux/errno-68/) — Connection reset by peer
- [EADDRINUSE (errno 98)](/os/linux/errno-98/) — Address already in use
