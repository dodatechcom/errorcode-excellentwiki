---
title: "[Solution] Linux: systemd-watchdog-error — Service watchdog timeout triggered"
description: "Fix Linux systemd-watchdog-error errors. Service watchdog timeout triggered with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["runtime-error"]
weight: 12
---

# Linux: systemd-watchdog-error — Service watchdog timeout triggered

Fix Linux systemd-watchdog-error errors. This guide covers common causes, step-by-step fixes, real-world scenarios, and prevention tips.

## Common Causes

- Not sending keepalives
- Timeout too short
- Service deadlocked
- App bug

## How to Fix

### 1. Check
```bash
journalctl -u <service>.service | grep -i watchdog
systemctl show <service>.service -p WatchdogUSec
```

### 2. Increase Timeout
```bash
sudo systemctl edit <service>.service
[Service]
WatchdogSec=60
```

### 3. Disable for Debug
```bash
[Service]
WatchdogSec=0
```

### 4. Add to App
```bash
# sd_notify(0, "WATCHDOG=1")
```

## Common Scenarios

- Repeatedly restarting
- Watchdog timeout in logs
- App hangs causing restart

## Prevent It

- Set enough time for operations
- Implement watchdog notification
- Monitor to tune timeout
