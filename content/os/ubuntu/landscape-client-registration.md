---
title: "Landscape Client Registration Error"
description: "Landscape client fails to register with Landscape server"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Landscape Client Registration Error

Landscape client fails to register with Landscape server

## Common Causes

- Landscape server URL incorrect in client config
- Account or registration key invalid
- Network connectivity to Landscape server blocked
- SSL certificate verification failing

## How to Fix

1. Check client config: `cat /etc/landscape/client.conf`
2. Verify server URL and key
3. Test connectivity: `curl -k https://landscape-server.com/api/`
4. Check client logs: `sudo journalctl -u landscape-client`

## Examples

```bash
# Check Landscape client status
sudo systemctl status landscape-client

# View client logs
sudo journalctl -u landscape-client -n 50

# Check client configuration
cat /etc/landscape/client.conf
```
