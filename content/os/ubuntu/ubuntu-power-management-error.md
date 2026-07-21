---
title: "Ubuntu Power Management Error"
description: "System power management features not functioning correctly"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Power Management Error

System power management features not functioning correctly

## Common Causes

- TLP or powertop not installed
- CPU governor not set to powersave
- Laptop lid close action not configured
- Power button action ignored

## How to Fix

1. Check governor: `cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor`
2. Install TLP: `sudo apt-get install tlp`
3. Configure lid: `grep LidSwitch /etc/systemd/logind.conf`
4. Check power: `upower -i /org/freedesktop/UPower/devices/battery_BAT0`

## Examples

```bash
# Check CPU governor
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor

# Install TLP
sudo apt-get install tlp tlp-rdw
sudo systemctl enable tlp

# Check battery status
upower -i /org/freedesktop/UPower/devices/battery_BAT0
```
