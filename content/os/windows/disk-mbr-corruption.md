---
title: "[Solution] MBR Master Boot Record Corruption Fix"
description: "Fix corrupted Master Boot Record (MBR) on Windows when the system fails to boot. Resolve MBR corruption and boot sector errors on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] MBR Master Boot Record Corruption Fix

MBR corruption prevents Windows from booting because the master boot record contains invalid or damaged partition and boot code. The system displays boot errors or enters recovery mode.

## Common Causes
- Malware overwriting the MBR with malicious code
- Power loss during disk write operations
- Incorrect disk partitioning operations
- Bad sectors on the first sector of the disk
- Dual-boot configuration changes corrupting MBR

## How to Fix

### Solution 1: Boot from Windows Installation Media

Boot from the Windows installation USB/DVD and select Repair your computer > Command Prompt.

### Solution 2: Rebuild MBR

```cmd
bootrec /fixmbr
bootrec /fixboot
bootrec /scanos
bootrec /rebuildbcd
```

### Solution 3: Check Disk for Errors

```cmd
chkdsk C: /f /r
```

### Solution 4: Use Startup Repair

Boot from installation media and select Startup Repair to automatically fix boot issues.

### Solution 5: Convert to GPT

Consider converting from MBR to GPT for better reliability:

```cmd
mbr2gpt /validate /disk:0 /allowFullOS
mbr2gpt /convert /disk:0 /allowFullOS
```

## Examples
```powershell
Get-Disk | Select-Object Number, PartitionStyle, Size
bcdedit /enum all
```
