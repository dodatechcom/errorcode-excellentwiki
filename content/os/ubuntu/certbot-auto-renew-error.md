---
title: "Certbot Auto-Renewal Error"
description: "Certbot automatic renewal fails or does not run"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Certbot Auto-Renewal Error

Certbot automatic renewal fails or does not run

## Common Causes

- Certbot systemd timer not enabled
- Cron job missing or misconfigured
- Renewal hook script failing
- DNS challenge credentials expired

## How to Fix

1. Check timer: `systemctl status certbot.timer`
2. Test renewal: `certbot renew --dry-run`
3. Check cron: `crontab -l | grep certbot`
4. Review renewal logs: `journalctl -u certbot`

## Examples

```bash
# Check certbot timer
systemctl status certbot.timer

# Test renewal
sudo certbot renew --dry-run

# Check renewal logs
sudo journalctl -u certbot -n 50
```
