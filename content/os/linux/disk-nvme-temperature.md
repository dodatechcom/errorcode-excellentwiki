---
title: "[Solution] Linux: disk-nvme-temperature — NVMe disk temperature warning"
description: "Fix Linux disk-nvme-temperature errors. NVMe disk temperature warning with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 8
---
# Linux: NVMe Temperature Warning

NVMe SSDs report temperature through SMART data. Exceeding critical thresholds causes throttling or shutdown to prevent damage.

## Common Causes

- Inadequate airflow or cooling in the system chassis
- High ambient temperature in the server room
- Sustained heavy write workloads generating excess heat
- Missing or poorly installed thermal pads on the NVMe drive
- Dust accumulation blocking heat dissipation

## How to Fix

### 1. Check Temperature

```bash
sudo nvme smart-log /dev/nvme0 | grep -i temp
cat /sys/class/nvme/nvme0/device/temp
```

### 2. Monitor Over Time

```bash
watch -n 5 'sudo nvme smart-log /dev/nvme0 | grep -i temp'
```

### 3. Check Throttling

```bash
sudo nvme get-feature /dev/nvme0 -f 0x10 -c 0
```

### 4. Improve Cooling

```bash
# Check system fans and temperatures
sudo sensors
```

### 5. Reduce Workload During Hot Periods

```bash
# Pause heavy I/O operations
# Consider adding heatsinks to NVMe drives
```

## Examples

```bash
$ sudo nvme smart-log /dev/nvme0
Smart Log for NVME device:nvme0 namespace-id:ffffffff
temperature                         : 78 C
warning_temp_time                   : 120
critical_comp_time                  : 0

$ cat /sys/class/nvme/nvme0/device/temp
78
```
