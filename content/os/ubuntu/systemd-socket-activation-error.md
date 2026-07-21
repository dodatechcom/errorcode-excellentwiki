---
title: "Systemd Socket Activation Failure"
description: "Service using socket activation fails to start on demand"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Systemd Socket Activation Failure

Service using socket activation fails to start on demand

## Common Causes

- Socket unit file misconfigured
- Service not properly linked to socket
- Listen directive syntax error
- Multiple sockets conflicting

## How to Fix

1. Check socket: `systemctl status <socket-name>`
2. Verify service: `systemctl cat <service-name>.service`
3. Test: `systemd-socket-activate -l /run/test.sock echo test`
4. Check logs: `journalctl -u <socket-name>`

## Examples

```bash
# Check socket status
systemctl status mysocket.socket

# Test socket activation
systemd-socket-activate -l /tmp/test.sock echo 'activated'

# Check service is linked to socket
systemctl cat myservice.service | grep -i socket
```
