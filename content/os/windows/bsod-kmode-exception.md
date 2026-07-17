---
title: "[Solution] BSOD KMODE_EXCEPTION_NOT_HANDLED Windows 11/10 — Fixed"
description: "Fix Blue Screen KMODE_EXCEPTION_NOT_HANDLED error on Windows 10 and 11. Update drivers, disable overclocking, and run memory diagnostics to resolve this stop code."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD KMODE_EXCEPTION_NOT_HANDLED Windows 11/10 — Fixed

KMODE_EXCEPTION_NOT_HANDLED is a critical Blue Screen of Death error with stop code `0x0000001E`. It occurs when a kernel-mode program generates an exception that the kernel error handler does not catch. This typically means a driver has attempted to execute an illegal or undefined CPU instruction.

This BSOD affects both Windows 10 and 11 and is most commonly caused by faulty drivers, incompatible hardware, or overclocking instability.

## Common Causes

- **Faulty or incompatible drivers** — The most common cause. A kernel-mode driver executes an invalid instruction or accesses restricted memory.
- **Overclocking instability** — CPU or RAM overclocking beyond stable limits causes the processor to execute incorrect instructions.
- **Faulty RAM** — Memory corruption leads to unpredictable kernel behavior.
- **Incompatible hardware** — Recently added hardware without proper driver support.

## How to Fix

### Boot into Safe Mode

1. Restart your PC and press `F8` or hold `Shift` while clicking Restart.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**.
3. Press `4` or `F4` for Safe Mode.

### Update or Uninstall Problematic Drivers

Check for device errors in Safe Mode:

```powershell
Get-WmiObject Win32_PnPEntity | Where-Object { $_.ConfigManagerErrorCode -ne 0 } | Select-Object Name, DeviceID, ConfigManagerErrorCode | Format-Table -AutoSize
```

Uninstall recently updated drivers:

```powershell
pnputil /enum-devices /driver oem*.inf
pnputil /delete-driver oemXX.inf /uninstall
```

Focus on GPU, network, and storage drivers first.

### Disable Overclocking

1. Restart and enter BIOS/UEFI (press `Del`, `F2`, or `F12` during boot).
2. Select **Load Optimized Defaults** or **Load Fail-Safe Defaults**.
3. Save and exit.

If using software overclocking tools (MSI Afterburner, Intel XTU, Ryzen Master), click **Reset to defaults**.

### Run Memory Diagnostics

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. For thorough testing, use MemTest86 from a bootable USB with at least 4 passes.

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Analyze the Minidump

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

Open the dump file in WinDbg and run `!analyze -v` to identify the faulting driver.

## Examples

This error commonly occurs in these scenarios:

- **After installing a new driver** — An unsigned or beta driver contains illegal instructions.
- **With overclocked systems** — Pushing CPU or RAM beyond stable limits causes instruction errors.
- **During heavy multitasking** — Driver conflicts surface under sustained system load.
- **After hardware changes** — New RAM, GPU, or peripherals with incompatible drivers.

## Related Errors

- [BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-irql-not-less-or-equal" >}}) — Another driver-related BSOD caused by invalid memory access at high IRQL
- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-driver-irql-not-less-or-equal" >}}) — Driver accessing memory at an invalid IRQL level
- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/os/windows/bsod-system-thread-exception" >}}) — System thread crash from unhandled exceptions
- [Error 0xc0000005]({{< relref "/os/windows/0xc0000005" >}}) — Access Violation, related memory access errors
