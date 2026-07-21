---
title: "[Solution] Ubuntu Server: system-timeout-starting"
description: "Fix Ubuntu system-timeout-starting. systemd service startup timeout exceeded."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd Timeout Starting

systemd service startup exceeds the configured timeout.

## Common Causes
- Service performing slow initialization
- Waiting for network that never comes
- Database or storage mount not ready
- Service blocked on external resource

## How to Fix
1. Check timeout configuration
```bash
systemctl show <service> | grep TimeoutStartSec
```
2. Increase timeout
```bash
sudo systemctl edit <service>
[Service]
TimeoutStartSec=300
```
3. Check what the service is waiting for
```bash
sudo systemctl status <service>
sudo journalctl -u <service> -f
```

## Examples
```bash
$ sudo systemctl status myservice
● myservice.service - My Service
   Active: activating (start) ...
   Job started. See systemctl
