---
title: "[Solution] Ubuntu Server: snap-snapd-not-running"
description: "Fix Ubuntu snap-snapd-not-running. snapd daemon is not running or responding."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Snap Snapd Not Running

snapd daemon is not running or has crashed.

## Common Causes
- snapd service disabled
- snapd crashed due to disk full
- snapd socket missing
- systemd failed to start snapd

## How to Fix
1. Check snapd status
```bash
sudo systemctl status snapd
sudo systemctl status snapd.socket
```
2. Start snapd
```bash
sudo systemctl start snapd
sudo systemctl start snapd.socket
sudo systemctl enable snapd
```
3. Check snapd logs
```bash
journalctl -u snapd -n 50
```

## Examples
```bash
$ sudo systemctl status snapd
● snapd.service - snapd service
   Loaded: loaded
   Active: failed (Result: exit-code)

$ sudo systemctl restart snapd
$ snap version
snap    2.57.6
snapd   2.57.6
```
