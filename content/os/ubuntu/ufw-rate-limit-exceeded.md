---
title: "UFW Rate Limit Triggered"
description: "UFW rate limiting blocks legitimate traffic after threshold exceeded"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# UFW Rate Limit Triggered

UFW rate limiting blocks legitimate traffic after threshold exceeded

## Common Causes

- Rate limit rule applied too aggressively
- Legitimate high-traffic service hitting rate limit
- Wrong rate limit parameters configured
- Multiple connections from same source triggering limit

## How to Fix

1. Check rate limit rules: `sudo ufw status numbered`
2. Adjust rate limit: `sudo ufw limit <port>/tcp`
3. Remove rate limit and use allow: `sudo ufw delete limit <port>/tcp && sudo ufw allow <port>/tcp`
4. Check logs: `grep UFW /var/log/syslog | grep RATE`

## Examples

```bash
# Check current rules
sudo ufw status numbered

# Remove rate limit rule
sudo ufw delete limit 22/tcp

# Add allow rule without rate limit
sudo ufw allow 22/tcp
```
