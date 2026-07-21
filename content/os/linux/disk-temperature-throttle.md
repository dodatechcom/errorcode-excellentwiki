---
title: "[Solution] Linux: disk-temperature-throttle -- disk thermal throttling"
description: "Fix Linux disk temperature throttling errors. Drive thermal throttling causing I/O drops."
os: ["linux"]
error-types: ["disk-error"]
severities: ["warning"]
---

# Linux: Disk Temperature Throttling

Disk temperature throttling occurs when drives reduce performance to prevent overheating.

## Common Causes

- Ambient temperature too high in server room
- Cooling fan failure or obstruction
- SSD sustained write causing thermal throttling
- NVMe drive hitting thermal junction limit
- RAID controller generating excessive heat

## How to Fix

### 1. Check Disk Temperature

```bash
sudo smartctl -A /dev/sda | grep -i temperature
sudo nvme smart-log /dev/nvme0 | grep temperature
sudo hddtemp /dev/sd*
```

### 2. Monitor Thermal Status

```bash
sudo smartctl -l scttemp /dev/sda
cat /sys/class/nvme/nvme0/device/hwmon/hwmon*/temp1_input
```

### 3. Improve Cooling

```bash
sudo ipmitool sensor list | grep -i fan
sensors
```

## Examples

```bash
$ sudo smartctl -A /dev/sda | grep Temperature
194 Temperature_Celsius  0x0022 038 038 000  Old_age Always - 38
$ sudo nvme smart-log /dev/nvme0 | grep temp
temperature : 72 C
# NVMe drives typically throttle at 70-80C
```
