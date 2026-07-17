---
title: "[Solution] Linux ECONNABORTED (errno 67) — Software Caused Connection Abort Fix"
description: "Fix Linux ECONNABORTED (errno 67) Software caused connection abort error. Solutions for connection abort and timeout issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux ECONNABORTED (errno 67) — Software Caused Connection Abort

ECONNABORTED (errno 67) means a connection was aborted by the local software. This error occurs when the TCP stack on the local machine terminates a connection, often due to a timeout, resource limit, or protocol error. It is distinct from ECONNRESET (errno 68) because ECONNABORTED is triggered locally, not by the remote peer.

## Common Causes

- TCP keepalive timeout expired on an idle connection
- Application closed the socket before receiving a response
- Local firewall or security module terminated the connection
- Socket buffer overflow due to slow receiver

## How to Fix ECONNABORTED

### 1. Check for Firewall Rules

Look for rules that might be dropping connections:

```bash
sudo iptables -L -n
sudo nft list ruleset
```

### 2. Adjust TCP Keepalive Settings

Configure keepalive to detect dead connections earlier:

```bash
sudo sysctl -w net.ipv4.tcp_keepalive_time=600
sudo sysctl -w net.ipv4.tcp_keepalive_intvl=30
sudo sysctl -w net.ipv4.tcp_keepalive_probes=5
```

### 3. Increase Socket Buffer Sizes

Prevent buffer overflow on slow connections:

```bash
sudo sysctl -w net.core.rmem_max=16777216
sudo sysctl -w net.core.wmem_max=16777216
```

### 4. Check Application Logs

Look for application-level errors:

```bash
journalctl -u application-service --since "1 hour ago"
```

### 5. Use Connection Retry Logic

Implement automatic reconnection in applications:

```bash
#!/bin/bash
for i in $(seq 1 3); do
  curl --retry 3 --retry-delay 2 http://server/api
  if [ $? -eq 0 ]; then break; fi
done
```

## Verification

After applying fixes, confirm the connection succeeds:

```bash
ss -t state established
curl -v http://server/api
```

## Related Error Codes

- [ECONNRESET (errno 68)](/os/linux/errno-68/) — Connection reset by peer
- [ETIMEDOUT (errno 74)](/os/linux/errno-74/) — Connection timed out
- [ECONNREFUSED (errno 75)](/os/linux/errno-75/) — Connection refused
