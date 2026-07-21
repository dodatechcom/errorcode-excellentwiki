---
title: "[Solution] Ubuntu Server: ufw-rate-limit-error"
description: "Fix Ubuntu ufw-rate-limit-error. UFW rate limiting blocks legitimate connections."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# UFW Rate Limit Error

UFW rate limiting blocks legitimate connections.

## Common Causes
- Rate limit threshold too low
- Too many legitimate connections from same IP
- SSH rate limit kicking in during normal use
- No way to whitelist trusted IPs from rate limit

## How to Fix
1. Check rate-limited rules
```bash
sudo ufw status | grep LIMIT
```
2. Remove rate limit and use allow instead
```bash
sudo ufw delete limit 22/tcp
sudo ufw allow from 192.168.1.0/24 to any port 22
```
3. Adjust fail2ban if using both
```bash
sudo ufw status
sudo fail2ban-client status
```

## Examples
```bash
$ sudo ufw status
[ 1] 22/tcp    LIMIT IN    Anywhere

# Replaced with allow from trusted subnet:
$ sudo ufw delete limit 22/tcp
$ sudo ufw allow from 192.168.1.0/24 to any port 22
```
