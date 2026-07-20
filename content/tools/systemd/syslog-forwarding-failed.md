---
title: "[Solution] systemd syslog forwarding failed"
description: "Fix systemd syslog forwarding failed. Resolve remote syslog forwarding issues from journald."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd syslog forwarding failed

## Error Description

Failed to forward journal entries to remote syslog server: Connection refused

journald cannot forward logs to the remote syslog server.

## Common Causes

Common Causes:
- Remote syslog server is unreachable
- ForwardToSyslog=yes is set but rsyslog is not running
- Network firewall blocking syslog port (514)
- rsyslog configuration error

## How to Fix

How to Fix:
```bash
# Check rsyslog status
systemctl status rsyslog

# Configure journald forwarding
sudo tee /etc/systemd/journald.conf <<'EOF'
[Journal]
ForwardToSyslog=yes
ForwardToSyslogSocket=yes
EOF

sudo systemctl restart systemd-journald

# Or use rsyslog to read journald
sudo tee /etc/rsyslog.d/journald.conf <<'EOF'
module(load="imjournal")
input(type="imjournal")
EOF
```

## Examples

```bash
# Check systemd version
systemctl --version

# Verify unit file syntax
sudo systemd-analyze verify /etc/systemd/system/myapp.service

# Analyze system boot
systemd-analyze blame

# List failed units
systemctl --failed

# View service logs
journalctl -u myapp -n 50 --no-pager
```