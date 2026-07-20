---
title: "[Solution] systemd target not found"
description: "Fix systemd target not found errors. Resolve failures when referencing a non-existent target."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd target not found

## Error Description

Failed to isolate myapp.target: Unit myapp.target not found.

The specified target does not exist.

## Common Causes

Common Causes:
- Target unit file does not exist
- Typo in the target name
- Target was deleted but still referenced
- Package providing the target is not installed

## How to Fix

How to Fix:
```bash
# List available targets
systemctl list-unit-files --type=target

# Create a custom target
sudo tee /etc/systemd/system/myapp.target <<'EOF'
[Unit]
Description=My App Target
Requires=multi-user.target
After=multi-user.target
AllowIsolate=yes

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
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