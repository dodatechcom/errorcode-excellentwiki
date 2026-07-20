---
title: "[Solution] Linux: tcp-connection-error — TCP connection error"
description: "Fix Linux tcp-connection-error errors. TCP connection error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 8
---
# Linux: TCP Connection Error

TCP connection errors occur when the TCP handshake fails or connections are reset unexpectedly.

## Common Causes

- Firewall silently dropping SYN packets
- Server application not listening on the port
- TCP backlog queue full (listen(2) backlog exceeded)
- TCP window size or scaling issues
- Kernel parameter tcp_tw_reuse or tcp_tw_recycle misconfiguration

## How to Fix

### 1. Analyze TCP Connection State

```bash
# Check connection state
ss -tanp
# Count connections by state
ss -tan | awk '{print $1}' | sort | uniq -c
```

### 2. Check TCP Parameters

```bash
sysctl net.ipv4.tcp_syncookies
sysctl net.ipv4.tcp_fin_timeout
sysctl net.core.somaxconn
```

### 3. Increase Backlog

```bash
sudo sysctl -w net.core.somaxconn=65535
echo "net.core.somaxconn=65535" | sudo tee -a /etc/sysctl.conf
```

### 4. Capture Traffic

```bash
sudo tcpdump -i any host <target> and port <port>
```

## Examples

```bash
$ ss -tan | head -10
State      Recv-Q Send-Q  Local Address:Port   Peer Address:Port
SYN-SENT   0      1       192.168.1.100:45678  10.0.0.1:80
ESTAB      0      0       192.168.1.100:22     10.0.0.2:54321
TIME-WAIT  0      0       192.168.1.100:80     10.0.0.3:12345

$ ss -tan | awk '{print $1}' | sort | uniq -c
     12 ESTAB
      3 SYN-SENT
     45 TIME-WAIT
```
