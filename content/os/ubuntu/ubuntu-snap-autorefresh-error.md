---
title: "[Solution] Ubuntu Server: ubuntu-snap-autorefresh-error"
description: "Fix Ubuntu ubuntu-snap-autorefresh-error. snap auto-refresh fails or causes downtime."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Snap Autorefresh Error

snap auto-refresh fails or restarts services unexpectedly.

## Common Causes
- Auto-refresh during business hours
- Snap refresh requires restart
- Network connectivity during refresh

## How to Fix
1. Check snap refresh schedule
```bash
snap get system refresh.timer
```
2. Set refresh schedule
```bash
sudo snap set system refresh.timer=02:00-04:00
```
3. Hold refresh temporarily
```bash
sudo snap hold <package>
```

## Examples
```bash
$ snap get system refresh.timer
00:00~24:00
```