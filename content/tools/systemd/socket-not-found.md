---
title: "[Solution] systemd socket not found"
description: "Fix systemd socket not found errors. Resolve socket activation failures when the socket unit is missing."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd socket not found

## Error Description

Failed to activate myapp.service via socket: Socket unit myapp.socket not found.

The socket unit referenced by the service does not exist.

## Common Causes

Common Causes:
- The socket unit file was deleted
- The socket unit was not installed
- Typo in the socket name in the service unit

## How to Fix

How to Fix:
```bash
# Create the socket unit
sudo tee /etc/systemd/system/myapp.socket <<'EOF'
[Unit]
Description=My App Socket

[Socket]
ListenStream=8080

[Install]
WantedBy=sockets.target
EOF

sudo systemctl daemon-reload
sudo systemctl start myapp.socket
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