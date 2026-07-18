---
title: "[Solution] Linux: systemd-first-boot-error — First boot setup failed"
description: "Fix Linux systemd-first-boot-error errors. First boot setup failed with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["boot-error"]
weight: 8
---

# Linux: systemd-first-boot-error — First boot setup failed

Fix Linux systemd-first-boot-error errors. This guide covers common causes, step-by-step fixes, real-world scenarios, and prevention tips.

## Common Causes

- Already completed
- Directories missing
- machine-id/locale missing
- Wizard interrupted

## How to Fix

### 1. Check
```bash
ls /etc/first-boot-done 2>/dev/null
systemctl status systemd-first-boot
```

### 2. Force Again
```bash
sudo rm /etc/first-boot-done
sudo systemctl restart systemd-first-boot
```

### 3. Complete Manually
```bash
sudo systemd-first-boot --force
```

### 4. Fix Missing
```bash
sudo systemd-machine-id-setup
echo "en_US.UTF-8" | sudo tee /etc/locale.conf
timedatectl set-timezone UTC
```

## Common Scenarios

- Stuck in boot loop
- Wizard not appearing
- Services missing

## Prevent It

- Complete promptly
- Ensure /etc has required files
- Test in image building
