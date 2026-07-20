---
title: "[Solution] systemd unit file syntax error"
description: "Fix systemd unit file syntax errors. Resolve parse failures in .service, .socket, .timer, and .target unit files."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd unit file syntax error

## Error Description

$ sudo systemctl daemon-reload
Failed to reload daemon: Unit file contains a syntax error: /etc/systemd/system/myapp.service:3: Failed to parse service type 'simplee'.

systemd cannot parse the unit file because it contains a syntax error. This prevents the unit from being loaded.

## Common Causes

Common Causes:
- Typo in a directive name (e.g., `Type=simplee` instead of `Type=simple`)
- Missing `=` sign after a directive
- Unknown or deprecated directive
- Invalid value for a known directive
- Encoding issues (BOM, non-UTF-8 characters)

## How to Fix

How to Fix:
```bash
# Check unit file syntax
sudo systemd-analyze verify /etc/systemd/system/myapp.service

# Reload after fixing
sudo systemctl daemon-reload

# View the specific line with the error
sudo systemd-analyze verify /etc/systemd/system/myapp.service 2>&1
```

Example of a corrected unit file:
```ini
[Unit]
Description=My Application
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/myapp
Restart=on-failure

[Install]
WantedBy=multi-user.target
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