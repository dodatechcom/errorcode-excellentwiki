---
title: "[Solution] Linux: udev-rule-error -- udev rule syntax error"
description: "Fix Linux udev rule errors. Udev rule syntax or trigger error preventing device management."
os: ["linux"]
error-types: ["device-error"]
severities: ["error"]
---

# Linux: Udev Rule Error

Udev rule errors occur when device manager rules fail to match devices correctly.

## Common Causes

- Invalid udev rule syntax with mismatched braces
- RUN directive executing without proper permissions
- SYMLINK or NAME creating conflicting device nodes
- Rule matching wrong subsystem or kernel device
- udevadm test not returning expected result

## How to Fix

### 1. Test Rule

```bash
sudo udevadm test /sys/class/net/eth0 2>&1 | tail -20
sudo udevadm info /sys/class/net/eth0
```

### 2. Validate Syntax

```bash
udevadm verify /etc/udev/rules.d/99-custom.rules
sudo udevadm test /dev/sda 2>&1 | grep RUN
```

### 3. Apply and Reload

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

## Examples

```bash
$ sudo udevadm verify /etc/udev/rules.d/99-custom.rules
invalid rule 'SUBSYSTEM=="net", ATTR{address}=="aa:bb:cc:dd:ee:ff", NAME"myinterface"'
# Missing = after NAME
$ sudo udevadm control --reload-rules
```
