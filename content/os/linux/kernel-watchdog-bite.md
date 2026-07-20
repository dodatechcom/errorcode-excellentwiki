---
title: "[Solution] Linux: kernel-watchdog-bite — NMI watchdog bite detected"
description: "Fix Linux kernel-watchdog-bite errors. NMI watchdog bite detected with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["kernel-error"]
weight: 14
---
# Linux: Watchdog Bite

A watchdog bite occurs when the hardware watchdog timer expires because the system stopped responding, causing a system reset.

## Common Causes

- Kernel hang or deadlock preventing watchdog refresh
- Systemd watchdog not configured to pet the hardware watchdog
- Hardware watchdog daemon (watchdog) not running
- System overload causing scheduling delays > watchdog timeout
- NFS or disk hangs preventing system progress

## How to Fix

### 1. Check Watchdog Status

```bash
# Check if watchdog is active
cat /proc/sys/kernel/watchdog
cat /proc/sys/kernel/nmi_watchdog

# Check hardware watchdog
sudo wdctl
```

### 2. Configure Softdog

```bash
sudo modprobe softdog
echo "softdog" | sudo tee /etc/modules
```

### 3. Configure systemd Watchdog

```bash
# Edit /etc/systemd/system.conf
# RuntimeWatchdogSec=30
# RebootWatchdogSec=30
```

### 4. Increase Watchdog Timeout

```bash
# For hardware watchdog
sudo wdctl --timeout 60
```

## Examples

```bash
$ sudo wdctl
Device:        /dev/watchdog0
Identity:      iTCO_wdt
Timeout:       30 seconds
Timeleft:      15 seconds
Pre-timeout:   0
FLAG           DESCRIPTION               STATUS
KeepAlive      keepalive daemon           active
MagicClose     magic close support        not supported

$ journalctl -k | grep -i watchdog
Jul 20 14:30:45 server kernel: watchdog: watchdog0: watchdog did not stop!
```
