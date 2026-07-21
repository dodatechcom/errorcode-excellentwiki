---
title: "[Solution] Linux: timezone-error -- timezone configuration error"
description: "Fix Linux timezone errors. Timezone configuration or database error on system."
os: ["linux"]
error-types: ["time-error"]
severities: ["warning"]
---

# Linux: Timezone Error

Timezone errors cause incorrect time display, log timestamps, and task execution.

## Common Causes

- /etc/localtime symlink broken or missing
- tzdata package not installed
- Container not sharing host timezone
- Dual-boot systems with Windows overwriting timezone
- timedatectl not persisting across reboots

## How to Fix

### 1. Check Timezone

```bash
timedatectl
cat /etc/timezone
ls -la /etc/localtime
readlink /etc/localtime
```

### 2. Set Timezone

```bash
sudo timedatectl set-timezone America/New_York
sudo ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime
```

### 3. Fix Container Timezone

```bash
docker run -v /etc/localtime:/etc/localtime:ro ubuntu
docker run -e TZ=America/New_York ubuntu
```

## Examples

```bash
$ timedatectl
               Local time: Thu 2026-07-20 14:00:00 UTC
                 Time zone: UTC (UTC, +0000)
$ sudo timedatectl set-timezone Europe/London
$ timedatectl
                 Time zone: Europe/London (BST, +0100)
```
