---
title: "[Solution] Ubuntu Server: system-masked-service-error"
description: "Fix Ubuntu system-masked-service-error. Service is masked and cannot be started."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd Masked Service Error

A systemd service is masked and cannot be started.

## Common Causes
- Admin masked the service intentionally
- Package post-install script masked it
- Masked to prevent conflict with another service
- Residual from package removal

## How to Fix
1. Check if service is masked
```bash
sudo systemctl is-enabled <service>
ls -la /etc/systemd/system/<service>.service
```
2. Unmask the service
```bash
sudo systemctl unmask <service>
sudo systemctl enable <service>
```
3. Start the service
```bash
sudo systemctl start <service>
```

## Examples
```bash
$ sudo systemctl is-enabled mysql
masked

$ ls -la /etc/systemd/system/mysql.service
lrwxrwxrwx 1 root root 9 Mar 15 10:00 /etc/systemd/system/mysql.service -> /dev/null

$ sudo systemctl unmask mysql
$ sudo systemctl enable mysql
```
