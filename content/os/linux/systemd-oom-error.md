---
title: "[Solution] Linux: systemd-oom-error — systemd OOMD service failure"
description: "Fix Linux systemd-oom-error errors. systemd OOMD service failure with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["runtime-error"]
weight: 12
---

# Linux: systemd-oom-error — systemd OOMD service failure

Fix Linux systemd-oom-error errors. This guide covers common causes, step-by-step fixes, real-world scenarios, and prevention tips.

## Common Causes

- OOMD not running
- PSI not configured
- PSI not available
- Killing wrong processes

## How to Fix

### 1. Check Status
```bash
systemctl status systemd-oomd
journalctl -u systemd-oomd
```

### 2. Enable PSI
```bash
cat /proc/pressure/memory
```

### 3. Configure
```bash
sudo tee /etc/systemd/oomd.conf << EOF
[OOMPolicy]
OOMScoreAdjust=-900
SwapFreeLimitPercentage=20
EOF
```

### 4. Use earlyoom
```bash
sudo apt install earlyoom
sudo systemctl enable --now earlyoom
```

## Common Scenarios

- OOMD fails to start
- Wrong processes killed
- System freezes instead

## Prevent It

- Ensure kernel supports PSI
- Protect critical services
- Monitor OOMD decisions
