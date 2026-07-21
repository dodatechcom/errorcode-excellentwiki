---
title: "Journald Forward to Syslog Not Working"
description: "Logs not forwarding from journald to rsyslog or syslog-ng"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Journald Forward to Syslog Not Working

Logs not forwarding from journald to rsyslog or syslog-ng

## Common Causes

- ForwardToSyslog=no in journald.conf
- rsyslog not reading journald socket
- Socket path /run/systemd/journal/syslog does not exist
- Permissions preventing journald from forwarding

## How to Fix

1. Enable forwarding: `ForwardToSyslog=yes` in /etc/systemd/journald.conf
2. Check rsyslog: `systemctl status rsyslog`
3. Verify socket: `ls -la /run/systemd/journal/syslog`
4. Restart services: `sudo systemctl restart systemd-journald rsyslog`

## Examples

```bash
# Enable syslog forwarding
sudo sed -i 's/#ForwardToSyslog=yes/ForwardToSyslog=yes/' /etc/systemd/journald.conf

# Restart journald
sudo systemctl restart systemd-journald

# Verify rsyslog
systemctl status rsyslog
```
