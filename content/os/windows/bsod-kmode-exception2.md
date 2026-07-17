---
title: "[Solution] BSOD KMODE_EXCEPTION_NOT_HANDLED (Faulty Driver) Windows 11/10 — Fixed"
description: "Fix Blue Screen KMODE_EXCEPTION_NOT_HANDLED on Windows 10 and 11. Resolve stop code 0x1E by identifying and removing faulty kernel-mode drivers."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "kmode", "exception", "driver", "kernel"]
weight: 5
---

# [Solution] BSOD KMODE_EXCEPTION_NOT_HANDLED (Faulty Driver) Windows 11/10 — Fixed

KMODE_EXCEPTION_NOT_HANDLED is a critical Blue Screen of Death error with stop code `0x0000001E`. It indicates that a kernel-mode program generated an exception that the error handler did not catch, typically caused by a faulty or incompatible device driver. The Windows kernel cannot safely continue and must halt the system.

This BSOD is one of the most common driver-related crashes. The offending driver is usually identified in the blue screen's "What failed" field, making it easier to pinpoint and fix than many other BSODs.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: KMODE_EXCEPTION_NOT_HANDLED
> What failed: [driver name, e.g., ntoskrnl.exe, e22w10x64.sys, rt640x64.sys]

Kernel-mode drivers run with full access to hardware and memory. When a driver has a programming error — such as accessing freed memory, dereferencing a null pointer, or executing an invalid instruction — the CPU generates an exception. If the driver's error handler cannot resolve it, Windows crashes with this BSOD.

Common scenarios for this BSOD:

- **After installing new hardware** — The device driver is incompatible with Windows
- **Following a Windows update** — Updated kernel components conflict with existing drivers
- **After installing driver manually** — Manually installed driver is corrupted or wrong version
- **With third-party antivirus** — Kernel-mode AV drivers cause exceptions

## Common Causes

1. **Faulty or incompatible device driver** — The driver identified in "What failed" has a code error.
2. **Corrupted driver installation** — Partially installed or corrupted driver files.
3. **Third-party antivirus software** — Kernel-mode AV drivers frequently cause this BSOD.
4. **Memory corruption** — Bad RAM causes drivers to read invalid data.

## Solutions

### Solution 1: Identify and Fix the Faulty Driver

The "What failed" field names the exact driver causing the crash. Focus on that specific driver.

**Use PowerShell to find which device uses the problematic driver:**

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object {$_.DriverName -like "*[partial driver name]*"} | Select-Object DeviceName, DriverVersion, InfName | Format-Table -AutoSize
```

Replace `*[partial driver name]*` with a partial match for the driver shown in the BSOD.

**If the faulty driver is a third-party antivirus driver (e.g., avgmgr*.sys, kl*.sys, mbamswissarmy.sys):**

1. Boot into **Safe Mode**.
2. Uninstall the antivirus software completely.
3. Restart and install a different antivirus or use Windows Defender.

**If the faulty driver is a hardware driver:**

1. Boot into **Safe Mode** if needed.
2. Open **Device Manager** and find the device.
3. Right-click and select **Uninstall device**.
4. Check **Delete the driver software for this device**.
5. Restart and install the correct driver from the manufacturer's website.

### Solution 2: Boot into Safe Mode to Remove the Driver

If the BSOD prevents normal startup, Safe Mode loads only essential drivers.

**Boot into Safe Mode:**

1. Force shutdown 3 times during boot to trigger Recovery Environment.
2. Select **Advanced options** > **Troubleshoot** > **Advanced options** > **Startup Settings**.
3. Click **Restart** and press `4` or `F4` for Safe Mode.

**In Safe Mode, uninstall the problematic driver:**

1. Right-click **Start** and select **Device Manager**.
2. Find the device with the faulty driver.
3. Right-click and select **Uninstall device**.
4. Restart in normal mode and reinstall the correct driver.

### Solution 3: Analyze the Minidump File

WinDbg identifies the exact code location causing the exception.

**Find the latest minidump:**

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

**Analyze with WinDbg:**

1. Install **WinDbg** from the Microsoft Store.
2. Open WinDbg and select **File > Open dump file**.
3. Open the most recent `.dmp` file.
4. Type `!analyze -v` and press Enter.
5. Look for **MODULE_NAME** and **IMAGE_NAME** to identify the driver.
6. The **EXCEPTION_CODE** tells you the type of error (e.g., `0xC0000005` for access violation).

### Solution 4: Run System File Checker

Corrupted system files can cause kernel exceptions.

```cmd
sfc /scannow
```

If SFC finds errors it cannot fix:

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
```

Run SFC again after DISM completes and restart.

### Solution 5: Test RAM for Errors

Memory corruption can cause drivers to read invalid data and generate exceptions.

**Run Windows Memory Diagnostic:**

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Check results in Event Viewer under **Windows Logs > System** with source `MemoryDiagnostics-Results`.

**Extended test with MemTest86:**

1. Download MemTest86 from [memtest86.com](https://www.memtest86.com/).
2. Create a bootable USB and boot from it.
3. Run at least **4 full passes**.
4. Any error confirms faulty RAM.

## Related Errors

- **[BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/windows/bsod-irql-not-less-or-equal" >}})** — Another driver-related memory access violation
- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-system-thread-exception" >}})** — System thread failure from faulty drivers
- **[BSOD SYSTEM_SERVICE_EXCEPTION]({{< relref "/windows/bsod-system-service-exception" >}})** — System service crash from driver conflicts
- **[BSOD PAGE_FAULT_IN_NONPAGED_AREA]({{< relref "/windows/bsod-page-fault" >}})** — Memory page errors often linked to the same driver issues
