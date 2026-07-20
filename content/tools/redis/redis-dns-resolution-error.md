---
title: "[Solution] Redis DNS Resolution Error"
description: "How to fix Redis DNS resolution failure when the hostname cannot be resolved"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- DNS server unreachable or misconfigured
- Hostname in connection string is incorrect
- `/etc/hosts` missing entry for Redis host
- Docker container cannot resolve hostnames
- DNS cache stale on client

## How to Fix

Test DNS resolution:

```bash
nslookup redis-host.example.com
```

Add entry to `/etc/hosts`:

```bash
echo "192.168.1.100 redis-host" | sudo tee -a /etc/hosts
```

Use IP address directly instead of hostname:

```bash
redis-cli -h 192.168.1.100 -p 6379 ping
```

Check DNS configuration:

```bash
cat /etc/resolv.conf
```

## Examples

```bash
# Test connectivity with IP
redis-cli -h 192.168.1.100 PING

# Flush DNS cache (systemd-resolved)
sudo systemd-resolve --flush-caches

# Verify with dig
dig redis-host.example.com
```
