---
title: "[Solution] Ubuntu Server: systemd-dependency-cycle"
description: "Fix Ubuntu systemd-dependency-cycle. systemd detects a dependency cycle between services."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd Dependency Cycle

systemd detects an infinite dependency loop between services.

## Common Causes
- Service A Requires service B, and B Requires A
- WantedBy chain creates a loop
- After/Requires ordering circular
- Socket activation creating cycle

## How to Fix
1. Analyze dependencies
```bash
systemd-analyze dot <service> | dot -Tpng > /tmp/service.png
systemd-analyze verify <service>
```
2. Break the cycle
```bash
sudo systemctl edit <service>
# Change Requires to Wants or remove circular dep
```
3. Restart systemd daemon
```bash
sudo systemctl daemon-reload
```

## Examples
```bash
$ systemd-analyze verify nginx.service
nginx.service: Dependency cycle detected: nginx.service -> network.target -> nginx.service
```
