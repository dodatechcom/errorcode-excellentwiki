---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED Windows 11/10 — Fixed"
description: "Fix Blue Screen SYSTEM_THREAD_EXCEPTION_NOT_HANDLED error on Windows 10 and 11. Resolve stop code 0x1000007E with driver updates, SFC scans, and memory diagnostics."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "system-thread", "driver", "kernel"]
weight: 5
---

# [Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED Windows 11/10 — Fixed

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED is a critical Blue Screen of Death error with stop code `0x1000007E`. It indicates that a system thread running in kernel mode generated an exception that the kernel's error handler did not catch, forcing Windows to crash to prevent system corruption.

This BSOD typically appears after a driver update, Windows update, or when a newly installed driver conflicts with an existing system component. The offending driver is usually identified in the blue screen's "What failed" field.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: SYSTEM_THREAD_EXCEPTION_NOT_HANDLED
> What failed: [driver name, e.g., nvlddmkm.sys, igdkmd64.sys, dxgkrnl.sys]

A system thread is a core execution thread managed by the Windows kernel. When such a thread generates an unhandled exception, it signals a severe problem — either a bug in a driver, memory corruption, or an incompatible software component. Windows cannot safely continue execution and must halt the system.

Common scenarios for this BSOD:

- **After installing GPU drivers** — NVIDIA, AMD, or Intel graphics drivers are frequent offenders
- **Following a Windows feature update** — Updated kernel components conflict with existing drivers
- **After adding new hardware** — A device driver generates exceptions under load
- **During sleep/wake transitions** — Power management drivers fail to handle state changes correctly

## Common Causes

1. **Faulty or incompatible device drivers** — Especially GPU, network, or storage drivers that execute in kernel mode.
2. **Corrupted Windows system files** — Damaged kernel files from disk errors or interrupted updates.
3. **Faulty RAM or hardware** — Memory corruption causes system threads to execute invalid instructions.
4. **Malware or rootkit infection** — Kernel-mode malware can hijack system threads.

## Solutions

### Solution 1: Update or Roll Back GPU Drivers

GPU drivers are the most common culprit for this BSOD. If it started after a driver update, roll back to the previous version.

**Check the "What failed" field on the blue screen** to identify the exact driver, then:

**Roll back a driver in Device Manager:**

1. Right-click the **Start** button and select **Device Manager**.
2. Expand **Display adapters**.
3. Right-click your GPU and select **Properties**.
4. Go to the **Driver** tab and click **Roll Back Driver**.
5. Follow the prompts and restart your computer.

**Check installed GPU driver version:**

```powershell
Get-WmiObject Win32_VideoController | Select-Object Name, DriverVersion, DriverDate | Format-Table -AutoSize
```

**Download the latest stable driver directly from the manufacturer:**
- **NVIDIA**: [nvidia.com/drivers](https://www.nvidia.com/Download/index.aspx)
- **AMD**: [amd.com/support](https://www.amd.com/en/support)
- **Intel**: [intel.com/support](https://www.intel.com/content/www/us/en/support.html)

Perform a clean installation during setup by checking the **Perform a clean install** option.

### Solution 2: Run System File Checker and DISM

Corrupted kernel files can cause system threads to generate exceptions. Repair the Windows image:

```cmd
sfc /scannow
```

If SFC reports errors it cannot fix:

```cmd
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth
```

Run SFC again after DISM completes:

```cmd
sfc /scannow
```

Restart your computer after all scans complete successfully.

### Solution 3: Check for Faulty RAM

Memory corruption is a common cause of unpredictable system thread exceptions.

**Run Windows Memory Diagnostic:**

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. After logging back in, check results in Event Viewer under **Windows Logs > System** with source `MemoryDiagnostics-Results`.

**Extended test with MemTest86:**

1. Download MemTest86 from [memtest86.com](https://www.memtest86.com/).
2. Create a bootable USB using the MemTest86 image writer.
3. Boot your computer from the USB drive.
4. Let the test run for at least **4 full passes**.
5. Any single error confirms faulty RAM.

### Solution 4: Analyze the Minidump File

Identify exactly which driver is causing the exception by analyzing the crash dump.

**Find the latest minidump:**

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

**Install WinDbg and analyze the dump:**

1. Install **WinDbg** from the Microsoft Store.
2. Open WinDbg and select **File > Open dump file**.
3. Navigate to `C:\Windows\Minidump\` and open the most recent `.dmp` file.
4. Type `!analyze -v` in the command window and press Enter.
5. Look for the **MODULE_NAME** and **IMAGE_NAME** lines to identify the problematic driver.

### Solution 5: Check for Malware

Kernel-mode malware can hijack system threads and trigger this BSOD.

**Run a full system scan:**

```powershell
Start-MpScan -ScanType FullScan
```

**Run an offline scan for rootkits:**

```powershell
Start-MpScan -ScanType OfflineScan
```

This restarts your computer and scans before Windows loads, catching rootkits that hide from regular scans.

## Related Errors

- **[BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/windows/bsod-irql-not-less-or-equal" >}})** — Driver-related memory access violations
- **[BSOD KMODE_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-kmode-exception" >}})** — Another kernel-mode exception error with similar driver-related causes
- **[BSOD PAGE_FAULT_IN_NONPAGED_AREA]({{< relref "/windows/bsod-page-fault" >}})** — Memory management error often caused by faulty RAM or drivers
- **[BSOD SYSTEM_SERVICE_EXCEPTION]({{< relref "/windows/bsod-system-service-exception" >}})** — System service failure typically caused by win32kfull.sys or similar components
