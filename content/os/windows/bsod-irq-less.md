---
title: "[Solution] BSOD IRQL_GT_ZERO_AT_SYSTEM_SERVICE Windows 11/10 — Fixed"
description: "Fix Blue Screen IRQL_GT_ZERO_AT_SYSTEM_SERVICE on Windows 10 and 11. Resolve stop code 0x0000004A with driver updates and system service diagnostics."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "irql", "system-service", "driver", "kernel"]
weight: 5
---

# [Solution] BSOD IRQL_GT_ZERO_AT_SYSTEM_SERVICE Windows 11/10 — Fixed

IRQL_GT_ZERO_AT_SYSTEM_SERVICE is a critical Blue Screen of Death error with stop code `0x0000004A`. It indicates that a thread running at an elevated IRQL (Interrupt Request Level) greater than zero attempted to enter a system service that requires execution at IRQL zero. This violates the Windows kernel's memory access rules and triggers a bug check.

This BSOD is almost always caused by a third-party driver that calls a system service function at an improper IRQL level. It points to a programming error in a kernel-mode driver that is not following the correct synchronization protocol.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: IRQL_GT_ZERO_AT_SYSTEM_SERVICE

System services are functions provided by the Windows kernel that drivers can call to perform privileged operations. Many of these services require the caller to be at IRQL zero (passive level) because they may need to access paged memory. When a driver calls such a service at an elevated IRQL (above zero), the kernel cannot safely execute the service and triggers this bug check.

Common scenarios for this BSOD:

- **With third-party antivirus** — AV kernel drivers execute at high IRQL
- **After installing new hardware** — Device driver has IRQL-related bugs
- **With VPN software** — Network filter drivers use improper IRQL levels
- **During heavy I/O operations** — Driver IRQL management breaks under load

## Common Causes

1. **Third-party driver IRQL violation** — A driver calls a system service at an improper IRQL level.
2. **Third-party antivirus software** — Kernel-mode AV drivers are frequent offenders.
3. **Network filter drivers** — VPN or firewall drivers with incorrect synchronization.
4. **Storage driver bugs** — Disk controllers that don't properly manage IRQL transitions.

## Solutions

### Solution 1: Identify and Remove the Faulty Driver

The BSOD's "What failed" field identifies the problematic driver.

**Use Driver Verifier to catch the culprit:**

```cmd
verifier /standard /all
```

Restart your computer. Driver Verifier monitors all drivers and triggers a detailed BSOD when a driver misbehaves.

**After the crash, analyze the minidump:**

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

Open the most recent `.dmp` file in WinDbg and run `!analyze -v`.

**Disable Driver Verifier when done:**

```cmd
verifier /reset
```

### Solution 2: Uninstall Third-Party Antivirus

Kernel-mode antivirus drivers are the most common cause of this BSOD.

**Boot into Safe Mode and uninstall:**

1. Force shutdown 3 times during boot to trigger Recovery Environment.
2. Select **Advanced options** > **Troubleshoot** > **Advanced options** > **Startup Settings**.
3. Press `4` for Safe Mode.
4. Uninstall your third-party antivirus software.
5. Restart in normal mode.

**Use Windows Defender instead:**

```powershell
# Verify Windows Defender is active
Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled, AntivirusEnabled
```

### Solution 3: Update All Device Drivers

Outdated drivers may have IRQL management bugs.

**Check for devices with errors:**

```powershell
Get-WmiObject Win32_PnPEntity | Where-Object {$_.ConfigManagerErrorCode -ne 0} | Select-Object Name, DeviceID, ConfigManagerErrorCode | Format-Table -AutoSize
```

**Update critical drivers via Device Manager:**

1. Right-click **Start** and select **Device Manager**.
2. Focus on these categories:
   - **Network adapters** — Network filter drivers
   - **Disk drives** — Storage drivers
   - **System devices** — Chipset drivers
3. Right-click each device and select **Update driver**.

**Download the latest drivers from manufacturer websites** rather than relying solely on Windows Update.

### Solution 4: Perform a Clean Boot

A clean boot helps identify if the issue is caused by third-party software.

**Configure a clean boot:**

1. Press `Win + R`, type `msconfig`, and press Enter.
2. Go to the **Services** tab.
3. Check **Hide all Microsoft services**.
4. Click **Disable all**.
5. Go to the **Startup** tab and click **Open Task Manager**.
6. Disable all startup items.
7. Restart your computer.

If the BSOD doesn't occur, re-enable services one at a time to find the culprit.

### Solution 5: Repair System Files

Corrupted Windows kernel files can cause IRQL violations.

```cmd
sfc /scannow
```

If SFC finds errors:

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
```

Run SFC again after DISM completes and restart.

## Related Errors

- **[BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/windows/bsod-irql-not-less-or-equal" >}})** — Broader IRQL violation from driver memory access
- **[BSOD IRQL_NOT_LESS_OR_EQUAL (Driver)]({{< relref "/windows/bsod-irql-driver" >}})** — Driver-specific IRQL violation
- **[BSOD KMODE_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-kmode-exception2" >}})** — Another kernel exception from faulty drivers
- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-system-thread-exception" >}})** — System thread crash from driver issues
