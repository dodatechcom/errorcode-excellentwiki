---
title: "[Solution] Linux: systemd-masked-unit — Service is masked"
description: "Fix Linux systemd-masked-unit errors. Service is masked with these solutions."
platforms: ["linux"]
severities: ["info"]
error-types: ["config-error"]
weight: 6
---

# Linux: systemd-masked-unit — Service is masked

Fix Linux systemd-masked-unit errors. This guide covers common causes, step-by-step fixes, real-world scenarios, and prevention tips.

## Common Causes

- Manually masked
- Distribution shipped masked
- Preventing conflicts
- Debug leftover

## How to Fix

### 1. Check
```bash
systemctl is-enabled <service>.service
systemctl cat <service>.service
```

### 2. Unmask
```bash
sudo systemctl unmask <service>.service
sudo systemctl enable <service>.service
```

### 3. Unmask and Start
```bash
sudo systemctl unmask <service>.service
sudo systemctl start <service>.service
```

### 4. List All
```bash
systemctl list-unit-files | grep masked
```

## Common Scenarios

- Failed to start: Unit is masked
- Cannot enable or start
- Interfering with install

## Prevent It

- Understand mask vs disable
- Only mask permanently
- Clean up when done
