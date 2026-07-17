---
title: "[Solution] BSOD KERNEL_LOCK_ENTRY_LEAKED_ON_THREAD_TERMINATION Windows 11/10 — Fixed"
description: "Fix Blue Screen KERNEL_LOCK_ENTRY_LEAKED_ON_THREAD_TERMINATION on Windows 10 and 11. Resolve stop code 0x167 with driver updates and system repairs."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD KERNEL_LOCK_ENTRY_LEAKED_ON_THREAD_TERMINATION Windows 11/10 — Fixed

KERNEL_LOCK_ENTRY_LEAKED_ON_THREAD_TERMINATION is a critical Blue Screen of Death error with stop code `0x00000167`. It indicates that a kernel thread terminated while still holding a lock that should have been released. This resource leak signals a serious bug in a kernel-mode driver that failed to properly clean up its synchronization objects before the thread exited.

This is a relatively rare BSOD that points to a driver bug — specifically, a driver that acquires a kernel lock (such as a mutex, fast mutex, or pushlock) but fails to release it before the thread is terminated. It is almost always caused by a third-party driver, not Windows itself.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: KERNEL_LOCK_ENTRY_LEAKED_ON_THREAD_TERMINATION

The Windows kernel uses various lock mechanisms to synchronize access to shared resources. When a thread acquires a lock, it must release it before terminating. If a thread is killed (either by a timeout, an exception, or a deliberate termination) while holding a lock, the kernel cannot safely free the resource, leading to this bug check.

Common scenarios for this BSOD:

- **With third-party antivirus** — AV drivers use kernel locks that may not be properly released
- **After installing new software** — Software with kernel-mode components has a resource leak
- **During heavy system load** — Race conditions in drivers cause lock leaks under stress
- **With virtualization software** — Hypervisor drivers can leak kernel locks

## Common Causes

1. **Buggy third-party driver** — A driver acquires a kernel lock but fails to release it on thread termination.
2. **Third-party antivirus software** — AV kernel-mode drivers are frequent offenders.
3. **Virtualization software** — Hypervisor or VM drivers with resource management bugs.
4. **Corrupted driver installation** — Partially installed driver with incomplete synchronization code.

## Solutions

### Solution 1: Identify and Remove the Faulty Driver

The BSOD often identifies the problematic driver. Check the "What failed" field if available.

**List recently installed drivers:**

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object {$_.DriverDate -gt (Get-Date).AddDays(-30)} | Select-Object DeviceName, DriverVersion, DriverDate | Sort-Object DriverDate -Descending | Format-Table -AutoSize
```

**If the faulty driver is a third-party antivirus:**

1. Boot into **Safe Mode**.
2. Uninstall the antivirus software completely.
3. Restart and verify the BSOD no longer occurs.
4. Install a different antivirus or use Windows Defender.

**Common problematic drivers:**

- Third-party antivirus (kernel-mode filter drivers)
- VPN clients with kernel-mode components
- Disk encryption software
- Virtual machine hypervisors (VMware, VirtualBox, Hyper-V third-party)

### Solution 2: Use Driver Verifier to Identify the Culprit

Driver Verifier monitors drivers for illegal operations and can catch lock leaks.

**Enable Driver Verifier:**

```cmd
verifier /standard /all
```

Restart your computer. Driver Verifier monitors all drivers and triggers a BSOD with diagnostic information when a driver misbehaves.

**After the next crash, analyze the minidump:**

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

Use WinDbg to open the most recent `.dmp` file and run `!analyze -v` to identify the driver.

**Disable Driver Verifier when done:**

```cmd
verifier /reset
```

**Warning:** Driver Verifier may cause additional BSODs while monitoring. This is expected — each crash provides diagnostic information.

### Solution 3: Update All Device Drivers

Outdated drivers may have lock management bugs that have been fixed in newer versions.

**Check for devices with errors:**

```powershell
Get-WmiObject Win32_PnPEntity | Where-Object {$_.ConfigManagerErrorCode -ne 0} | Select-Object Name, DeviceID, ConfigManagerErrorCode | Format-Table -AutoSize
```

**Update all drivers via Device Manager:**

1. Right-click **Start** and select **Device Manager**.
2. Expand each category.
3. Right-click any device with a warning icon.
4. Select **Update driver** > **Search automatically for drivers**.

**Focus on updating:**
- Network adapters
- Storage controllers
- USB controllers
- Security software drivers

### Solution 4: Repair System Files

Corrupted Windows files can cause kernel synchronization issues.

```cmd
sfc /scannow
```

If SFC finds errors it cannot fix:

```cmd
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth
```

Run SFC again after DISM completes and restart.

### Solution 5: Perform a Clean Boot

A clean boot starts Windows with only Microsoft services, helping identify third-party software causing the issue.

**Configure a clean boot:**

1. Press `Win + R`, type `msconfig`, and press Enter.
2. Go to the **Services** tab.
3. Check **Hide all Microsoft services**.
4. Click **Disable all**.
5. Go to the **Startup** tab and click **Open Task Manager**.
6. Disable all startup items.
7. Restart your computer.

If the BSOD doesn't occur in clean boot, re-enable services one at a time to find the culprit.

**Return to normal boot:**

```cmd
msconfig
```

Select **Normal startup** on the **General** tab and restart.

## Related Errors

- **[BSOD KMODE_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-kmode-exception2" >}})** — Another driver-related kernel exception
- **[BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/windows/bsod-irql-not-less-or-equal" >}})** — Driver memory access violations
- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-system-thread-exception" >}})** — System thread failure from faulty drivers
- **[BSOD SYSTEM_SERVICE_EXCEPTION]({{< relref "/windows/bsod-system-service-exception" >}})** — System service crash from driver conflicts
