---
title: "[Solution] systemd OnFailure not triggered"
description: "Fix systemd OnFailure not triggered. Resolve issues where failure handlers are not executed."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd OnFailure not triggered

## Error Description

myapp.service failed but the OnFailure= handler was not triggered.

The OnFailure= dependency was not activated on service failure.

## Common Causes

Common Causes:
- OnFailure= target or service does not exist
- The failure handler unit file is missing
- The service reached a different failure mode than expected

## How to Fix

How to Fix:
```bash
# Verify OnFailure= target exists
systemctl list-unit-files | grep failure-handler

# Create the handler if missing
sudo tee /etc/systemd/system/failure-handler.service <<'EOF'
[Unit]
Description=Failure Handler
After=myapp.service

[Service]
Type=oneshot
ExecStart=/usr/local/bin/notify-failure.sh

[Install]
WantedBy=multi-user.target
EOF

# Update the main service
sudo systemctl edit myapp
```

```ini
[Unit]
OnFailure=failure-handler.service
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