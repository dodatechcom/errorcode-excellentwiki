---
title: "[Solution] Linux: systemd-override-conf-error -- override conf syntax error"
description: "Fix Linux systemd override conf errors. Systemd drop-in override configuration has syntax error."
os: ["linux"]
error-types: ["systemd-error"]
severities: ["error"]
---

# Linux: Systemd Override Conf Error

Systemd override conf errors occur when drop-in configuration files contain invalid syntax.

## Common Causes

- Invalid INI syntax in drop-in override files
- Unknown directives in [Service] or [Unit] section
- Incorrect quoting of paths with spaces
- Missing required section headers
- Conflicting directives between main unit and override

## How to Fix

### 1. Validate Configuration

```bash
systemd-analyze verify <service_name>
systemd-analyze cat-config <service_name>
```

### 2. Check Drop-in Directory

```bash
ls /etc/systemd/system/<service_name>.service.d/
cat /etc/systemd/system/<service_name>.service.d/override.conf
```

### 3. Fix and Reload

```bash
sudo systemctl edit <service_name>
sudo systemctl daemon-reload
sudo systemctl restart <service_name>
```

## Examples

```bash
$ systemd-analyze verify myapp.service
myapp.service:5: Failed to parse line: ExecStart=/usr/bin/app --config "/path with spaces"
$ systemctl cat myapp.service
[Service]
ExecStart=/usr/bin/app --config "/path with spaces"
```
