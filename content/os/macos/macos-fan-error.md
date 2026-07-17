---
title: "[Solution] Mac Fan Speed Error"
description: "Fix fan speed errors on Mac when fans run at full speed constantly, don't spin up, or show incorrect RPM readings in diagnostics."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["fan", "cooling", "thermal", "smc", "temperature"]
weight: 5
---

# Mac Fan Speed Error Fix

Fan errors include fans running at maximum speed constantly, not spinning up when needed, or incorrect RPM readings. This can cause overheating or excessive noise.

## What This Error Means

macOS controls fan speed based on thermal sensor readings. When fans malfunction, it's usually an SMC (System Management Controller) issue or a hardware failure in the fan itself.

## Common Causes

- SMC corruption preventing proper fan control
- Thermal sensor failure providing incorrect readings
- Dust accumulation blocking airflow
- Fan motor failure
- Third-party app controlling fan speed incorrectly

## How to Fix

### 1. Reset the SMC

```bash
# Intel MacBooks:
# Shut down → Hold Shift+Control+Option+Power for 10 sec → Release → Power on

# Intel Mac desktops:
# Shut down → Unplug power for 15 sec → Plug in → Power on

# Apple Silicon Macs:
# Shut down → Hold power button for 10 sec → Release → Power on
```

### 2. Check fan speed readings

```bash
# Check current fan speeds
ioreg -c AppleSMCFan -r | grep -i "current\|speed"

# Or use powermetrics
sudo powermetrics --samplers smc -i 2000 -n 5
```

### 3. Monitor temperature sensors

```bash
# Check all temperature sensors
sudo powermetrics --samplers thermal -i 2000 -n 5

# Or use iStat (if installed)
istat temperatures
```

### 4. Clean dust from vents

```bash
# Shut down and unplug the Mac
# Use compressed air to clean vents and fan blades
# Ensure all vents are unobstructed
```

## Related Errors

- [Kernel Panic](kernel-panic) — crashes from overheating
- [Battery Error](macos-battery-error) — thermal management issues
- [SSD Error](macos-ssd-error) — heat-related storage failures
