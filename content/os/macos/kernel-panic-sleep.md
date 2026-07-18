---
title: "[Solution] macOS Kernel Panic Sleep — Wake from Sleep Crash"
description: "Fix macOS kernel panic on wake: Mac crashes when waking from sleep, lid opened, or after prolonged idle period."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 97
---

# Kernel Panic Sleep — Wake from Sleep Crash

Fix macOS kernel panic on wake: Mac crashes when waking from sleep, lid opened, or after prolonged idle period.

## Common Causes

- External device preventing Mac from entering proper sleep state
- Corrupted sleep image or hibernation file on disk
- Third-party kernel extension interfering with sleep/wake cycle
- Power management settings misconfigured or SMC issue

## How to Fix

### 1. Check Sleep Wake Logs

```bash
pmset -g log | grep -i 'wake\|sleep' | tail -20
pmset -g
pmset -g assertions
```

### 2. Disable Wake for Network and Power Nap

```bash
sudo pmset -a womp 0
sudo pmset -a powernap 0
sudo pmset -a btba 0
```

### 3. Reset SMC and NVRAM

```bash
# Intel: Shut down → hold Control+Option+Shift 7s → power 7s
sudo shutdown -r now
```

### 4. Fix Sleep Image and Hibernate Mode

```bash
sudo rm -f /var/vm/sleepimage
sudo pmset -a hibernatemode 0
```

## Common Scenarios

This error commonly occurs when:

- Mac kernel panics every time lid is opened after sleep
- Panic log shows AppleACPIPlatform or IOPMrootDomain crash
- Sleep/wake panic occurs only when USB devices are connected
- Kernel panic happens after Mac sleeps for extended period

## Prevent It

- Disable unnecessary wake triggers in System Settings → Battery/Energy
- Disconnect external peripherals before closing MacBook lid
- Reset SMC periodically if sleep issues become frequent
- Keep macOS updated to receive power management improvements
