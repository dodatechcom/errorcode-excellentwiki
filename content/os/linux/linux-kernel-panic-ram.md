---
title: "[Solution] Linux Kernel Panic — Memory Error (RAM Failure)"
description: "Fix Linux kernel panic caused by RAM memory errors. Diagnose memory failures, run memtest, and resolve kernel panics from bad RAM."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Linux: Kernel panic — memory error — RAM failure

The `kernel panic — not syncing: Fatal exception` or `Memory error at address` messages indicate the kernel encountered a memory-related failure so severe it could not continue. RAM failures cause data corruption, undefined behavior, and security vulnerabilities, so the kernel halts immediately.

## What This Error Means

When the kernel detects a memory error — such as accessing an invalid physical address, a parity error on ECC memory, or a page fault in kernel space — it triggers a kernel panic. Hardware ECC (Error Correcting Code) memory can report correctable and uncorrectable errors. Uncorrectable errors in kernel space cause an immediate panic since the data cannot be trusted.

## Common Causes

- Physically faulty RAM module (bit flips, stuck cells)
- Overheating RAM causing intermittent errors
- Improperly seated RAM sticks
- Incompatible RAM modules (different speeds, timings)
- Overclocking pushing RAM beyond stable limits
- Failing memory controller on the motherboard or CPU

## How to Fix

### 1. Check Kernel Logs for Memory Errors

```bash
# Look for MCE (Machine Check Exception) errors
sudo dmesg | grep -i -E 'mce|memory|ecc|hardware error'

# Check for specific memory error addresses
sudo journalctl -k | grep -i 'memory error\|page fault\|bad area'

# Check EDAC (Error Detection And Correction) logs
sudo dmesg | grep -i edac
```

### 2. Run memtest86+

```bash
# Install memtest86+
sudo apt install memtest86+

# Reboot and select memtest from GRUB
# Let it run for at least 4 passes (may take hours)

# Or boot from a live USB with memtest86+ built in
```

### 3. Identify Faulty RAM Module

```bash
# Check which DIMM slots are populated
sudo dmidecode -t memory | grep -A5 'Memory Device'

# Check for ECC errors via EDAC
cat /sys/devices/system/edac/mc/mc0/ce_count    # Correctable errors
cat /sys/devices/system/edac/mc/mc0/ue_count    # Uncorrectable errors

# Per-dimm error count (if EDAC loaded)
for mc in /sys/devices/system/edac/mc/mc*/; do
  echo "$(basename $mc): CE=$(cat ${mc}ce_count) UE=$(cat ${mc}ue_count)"
done
```

### 4. Test RAM with memtest from Linux

```bash
# Use memtester for userspace testing
sudo apt install memtester
sudo memtester 1G 1    # Test 1GB for 1 pass

# Or use stress-ng
sudo apt install stress-ng
stress-ng --vm 4 --vm-bytes 2G --timeout 60s --metrics-brief
```

### 5. Reseat and Replace RAM

```bash
# Power off, open the case, and reseat each RAM module
# Ensure modules are fully clicked into their slots

# If a specific module fails memtest, replace it
# Check manufacturer warranty for replacement

# If system has mixed RAM, try using only matched pairs
```

### 6. Check BIOS Settings

```bash
# In BIOS/UEFI:
# - Reset to default BIOS settings
# - Disable XMP/DOCP if overclocking
# - Run memory diagnostics tool built into BIOS
# - Check memory speed is within spec for motherboard
```

### 7. Monitor Memory Health

```bash
# Install EDAC tools
sudo apt install edac-utils

# Check EDAC status
edac-ctl --status

# Monitor correctable errors over time
watch -n 60 'cat /sys/devices/system/edac/mc/mc0/ce_count'

# If correctable errors increase rapidly, replace RAM soon
```

## Examples

```bash
$ sudo dmesg | grep -i mce
[    2.345678] mce: [Hardware Error]: Machine check events logged
[    2.345679] EDAC MC0: UE row 0, channel-a, label "DIMM_A1": Memory error at 0x7f800000

$ cat /sys/devices/system/edac/mc/mc0/ue_count
5

$ sudo memtester 512M 1
memtester version 4.6.5 (64-bit)
Loop 1/1:
  Stuck Address: ok
  Random Value: ok
  XOR: ok
  SUB: ok
  MUL: ok
  DIV: ok
  OR: ok
  AND: ok
  Sequential Compare: ok
  Solid Divide: Error!
# Replace the DIMM labeled DIMM_A1
```

## Related Errors

- [Kernel panic]({{< relref "/os/linux/linux-kernel-panic" >}}) — General kernel panic
- [OOM killer]({{< relref "/os/linux/oom-killer" >}}) — Out of memory killer
- [Cannot allocate memory]({{< relref "/os/linux/cannot-allocate-memory" >}}) — Memory allocation errors
