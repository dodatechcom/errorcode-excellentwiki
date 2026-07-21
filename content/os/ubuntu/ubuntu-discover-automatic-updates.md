---
title: "Ubuntu Software Automatic Updates Error"
description: "Software & Updates automatic updates feature not working"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Software Automatic Updates Error

Software & Updates automatic updates feature not working

## Common Causes

- Automatic updates setting not enabled in Software & Updates
- unattended-upgrades service not running
- Download upgrades automatically option unchecked
- Configuration file /etc/apt/apt.conf.d/20auto-upgrades missing

## How to Fix

1. Check config: `cat /etc/apt/apt.conf.d/20auto-upgrades`
2. Enable: `echo 'APT::Periodic::Update-Package-Lists "1";' | sudo tee /etc/apt/apt.conf.d/20auto-upgrades`
3. Check service: `systemctl status unattended-upgrades`
4. View logs: `journalctl -u unattended-upgrades`

## Examples

```bash
# Check auto-upgrade config
cat /etc/apt/apt.conf.d/20auto-upgrades

# Enable automatic updates
echo 'APT::Periodic::Update-Package-Lists "1";' | sudo tee /etc/apt/apt.conf.d/20auto-upgrades
echo 'APT::Periodic::Unattended-Upgrade "1";' | sudo tee -a /etc/apt/apt.conf.d/20auto-upgrades
```
