---
title: "[Solution] Linux EREMCHG (errno 57) — Remote Address Changed Fix"
description: "Fix Linux EREMCHG (errno 57) Remote address changed error. Solutions for stale remote connection issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux EREMCHG (errno 57) — Remote Address Changed

EREMCHG (errno 57) means the remote address of a network connection has changed. This error occurs when a connected socket detects that the remote peer's address has changed, typically in mobile or roaming network environments. It is distinct from ECONNRESET (errno 104) because EREMCHG specifically refers to an address change, not a connection reset.

## Common Causes

- Mobile device changed network (Wi-Fi to cellular)
- VPN reconnected with a different exit IP
- Load balancer redirected connection to a different backend
- Network reconfiguration changed remote endpoint address

## How to Fix EREMCHG

### 1. Re-establish the Connection

Close and reopen the network connection:

```bash
# For SSH sessions
ssh user@server.example.com

# For persistent connections
sudo systemctl restart ssh
```

### 2. Check Network Configuration

Verify current network settings:

```bash
ip addr show
ip route show
```

### 3. Restart Network Services

Restart the application's network connections:

```bash
sudo systemctl restart application-service
```

### 4. Use Connection Retry Logic

Implement automatic reconnection in applications:

```bash
#!/bin/bash
while true; do
  ssh user@server.example.com && break
  echo "Connection lost, retrying in 5 seconds..."
  sleep 5
done
```

## Verification

After re-establishing the connection, confirm connectivity:

```bash
ping server.example.com
ss -t state established
```

## Related Error Codes

- [ECONNRESET (errno 68)](/os/linux/errno-68/) — Connection reset by peer
- [ENOTCONN (errno 71)](/os/linux/errno-71/) — Not connected
- [ETIMEDOUT (errno 74)](/os/linux/errno-74/) — Connection timed out
