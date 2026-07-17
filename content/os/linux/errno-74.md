---
title: "[Solution] Linux ETIMEDOUT (errno 74) — Connection Timed Out Fix"
description: "Fix Linux ETIMEDOUT (errno 74) Connection timed out error. Solutions for network timeout and connectivity issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux ETIMEDOUT (errno 74) — Connection Timed Out

ETIMEDOUT (errno 74) means the connection or operation timed out. This error occurs when a network connection attempt or data transfer does not complete within the expected time limit. It is distinct from ECONNREFUSED (errno 75) because ETIMEDOUT means no response was received at all, while ECONNREFUSED means the remote actively rejected the connection.

## Common Causes

- Remote host is down or unreachable
- Firewall silently dropping packets
- Network congestion causing excessive latency
- DNS resolution timing out
- TCP SYN retries exhausted

## How to Fix ETIMEDOUT

### 1. Test Network Connectivity

Check if the target is reachable:

```bash
ping -c 5 -W 2 server.example.com
traceroute server.example.com
```

### 2. Check DNS Resolution

Verify DNS is working:

```bash
nslookup server.example.com
dig server.example.com
```

### 3. Increase Timeout Values

Adjust system-level timeout parameters:

```bash
sudo sysctl -w net.ipv4.tcp_syn_retries=5
sudo sysctl -w net.ipv4.tcp_retries2=15
```

### 4. Check Firewall Rules

Ensure the firewall is not dropping packets:

```bash
sudo iptables -L -n -v | grep DROP
sudo ufw status
```

### 5. Use Connection Timeout in Applications

Set appropriate timeouts in application code:

```bash
# In curl
curl --connect-timeout 10 --max-time 30 http://server/api

# In ssh
ssh -o ConnectTimeout=10 user@server
```

## Verification

After adjusting timeouts, confirm the connection succeeds:

```bash
time curl http://server/api
ss -tnp state established
```

## Related Error Codes

- [ECONNREFUSED (errno 75)](/os/linux/errno-75/) — Connection refused
- [ECONNRESET (errno 68)](/os/linux/errno-68/) — Connection reset by peer
- [ENETUNREACH (errno 65)](/os/linux/errno-65/) — Network is unreachable
