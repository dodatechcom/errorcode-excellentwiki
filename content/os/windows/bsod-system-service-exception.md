---
title: "[Solution] BSOD SYSTEM_SERVICE_EXCEPTION Windows 11/10 — Fixed"
description: "Fix Blue Screen SYSTEM_SERVICE_EXCEPTION error on Windows 10 and 11. Update GPU drivers, check for incompatible software, and run system file checks to resolve."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD SYSTEM_SERVICE_EXCEPTION Windows 11/10 — Fixed

SYSTEM_SERVICE_EXCEPTION is a critical Blue Screen of Death error with stop code `0x0000003B`. It occurs when a system service routine encounters an unexpected exception while executing in kernel mode. This typically means a driver or system service performed an illegal operation.

This BSOD affects both Windows 10 and 11 and is commonly triggered by GPU drivers, network drivers, and third-party security software.

## Common Causes

- **GPU driver issues** — Graphics drivers that corrupt system service call handling are the most frequent cause.
- **Third-party antivirus** — Kernel-mode antivirus hooks that interfere with system service routines.
- **Corrupted system files** — Damaged Windows system files that system services depend on.
- **Faulty RAM** — Memory corruption causes unpredictable system service behavior.

## How to Fix

### Update or Roll Back GPU Drivers

GPU drivers are the leading cause of this error.

**Roll back the driver:**

1. Open **Device Manager** (`Win + X` > Device Manager).
2. Expand **Display adapters**, right-click your GPU, and select **Properties**.
3. Go to the **Driver** tab and click **Roll Back Driver**.

**Or install the latest stable driver:**

- **NVIDIA**: Download from [nvidia.com/drivers](https://www.nvidia.com/drivers)
- **AMD**: Download from [amd.com/support](https://www.amd.com/support)
- **Intel**: Use Intel Driver & Support Assistant

Perform a clean installation when updating GPU drivers.

### Uninstall Conflicting Antivirus

Third-party antivirus software with kernel-mode components frequently triggers this error:

1. Open **Settings > Apps > Installed apps**.
2. Uninstall your third-party antivirus.
3. Restart your computer.
4. Windows Defender will activate automatically for protection.
5. Reinstall the latest version from the vendor if needed, or switch to Windows Defender.

### Run System File Checker

```cmd
sfc /scannow
```

If SFC reports issues it cannot fix:

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Boot into Safe Mode and Check for Device Errors

1. Hold `Shift` and click **Restart**.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**.
3. Press `4` or `F4` for Safe Mode.

```powershell
Get-WmiObject Win32_PnPEntity | Where-Object { $_.ConfigManagerErrorCode -ne 0 } | Select-Object Name, DeviceID, ConfigManagerErrorCode | Format-Table -AutoSize
```

### Test RAM

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Use MemTest86 for comprehensive testing.

### Analyze the Minidump

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

Open the dump file in WinDbg and run `!analyze -v` to identify the specific service or driver that failed.

## Examples

This error commonly occurs in these scenarios:

- **After updating GPU drivers** — A new graphics driver contains a bug in its system service calls.
- **During gaming** — GPU driver stress under load causes system service exceptions.
- **After installing antivirus** — A third-party security product hooks into system services incorrectly.
- **Following a Windows Update** — A cumulative update modifies system service behavior.

## Related Errors

- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/os/windows/bsod-system-thread-exception" >}}) — System thread generates an unhandled exception
- [BSOD KMODE_EXCEPTION_NOT_HANDLED]({{< relref "/os/windows/bsod-kmode-exception" >}}) — Kernel-mode program generates an exception
- [BSOD CRITICAL_PROCESS_DIED]({{< relref "/os/windows/bsod-critical-process-died" >}}) — Critical process termination
- [Error 0xc000021a]({{< relref "/os/windows/0xc000021a" >}}) — BSOD from winlogon/csrss process failure
