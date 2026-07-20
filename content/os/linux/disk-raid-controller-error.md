---
title: "[Solution] Linux: disk-raid-controller-error — disk RAID controller error"
description: "Fix Linux disk-raid-controller-error errors. disk RAID controller error with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["disk"]
weight: 12
---
# Linux: RAID Controller Error

RAID controller errors indicate problems with hardware RAID adapters or their kernel drivers (megaraid, mpt3sas, hpsa, smartpqi, etc.).

## Common Causes

- Hardware RAID adapter failure or firmware bug
- Battery backup unit (BBU) failed on the controller
- Cache module errors or memory corruption on the controller
- Driver incompatibility with current kernel version
- Incorrect controller mode (JBOD vs RAID)

## How to Fix

### 1. Identify the Controller

```bash
lspci | grep -i raid
sudo lshw -class storage
sudo storcli64 /c0 show all  # Broadcom/LSI
```

### 2. Check Controller Health

```bash
sudo storcli64 /c0 show health
sudo MegaCli64 -AdpAllInfo -aAll
sudo storcli64 /c0 /bbu show
```

### 3. Check Kernel Messages

```bash
dmesg | grep -iE "megaraid|mpt3sas|hpsa|smartpqi|aacraid" | tail -30
```

## Examples

```bash
$ sudo storcli64 /c0 show health
Controller = 0
Status = Critical
VDs = 1, DEGRADED = 1, OFFLINE = 0
BBU = FAILED

$ dmesg | grep megaraid
[ 1234.567] megaraid_sas: [0:00:00:0]: waiting for FW to boot
[ 1235.123] megaraid_sas: FW now in Ready state
```
