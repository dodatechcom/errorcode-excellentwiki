---
title: "[Solution] Ubuntu Server: systemd-failed-to-start"
description: "Fix Ubuntu systemd-failed-to-start. systemd unit fails to start due to configuration or dependency."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd Failed To Start

A systemd service unit fails to start.

## Common Causes
- Service configuration file has syntax errors
- Missing dependency or target
- Wrong user/group for the service
- ExecStart path incorrect

## How to Fix
1. Check service status
```bash
sudo systemctl status <service>
```
2. View detailed logs
```bash
journalctl -u <service> -n 50 --no-pager
```
3. Check unit file
```bash
sudo systemctl cat <service>
sudo nano /etc/systemd/system/<service>.service
```

## Examples
```bash
$ sudo systemctl status nginx
● nginx.service - A high performance web server
   Loaded: loaded
   Active: failed (Result: exit-code)

$ journalctl -u nginx -n 20
nginx[1234]: nginx: [emerg] bind() to 0.0.0.0:80 failed (98: Address already in use)
```
