---
title: "[Solution] BSOD SYSTEM_SERVICE_EXCEPTION (win32kfull.sys) Windows 11/10 — Fixed"
description: "Fix Blue Screen SYSTEM_SERVICE_EXCEPTION with win32kfull.sys on Windows 10 and 11. Resolve stop code 0x3B with driver updates and system file repairs."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD SYSTEM_SERVICE_EXCEPTION (win32kfull.sys) Windows 11/10 — Fixed

SYSTEM_SERVICE_EXCEPTION with win32kfull.sys is a critical Blue Screen of Death error with stop code `0x0000003B`. It indicates that the win32kfull.sys kernel-mode driver — which handles Windows graphics and window management — generated an exception that was not properly handled. This is a graphics subsystem crash.

win32kfull.sys is responsible for the Windows desktop window manager, GDI operations, and UI rendering. When this driver faults, it typically points to GPU driver issues, graphics hardware problems, or corrupted system files in the Windows graphics stack.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: SYSTEM_SERVICE_EXCEPTION
> What failed: win32kfull.sys

The win32kfull.sys driver is a core Windows component that manages all window and graphics operations. When a GPU driver sends invalid data to win32kfull.sys, or when the driver itself has a bug in how it interacts with the graphics subsystem, win32kfull.sys crashes and triggers this BSOD.

Common scenarios for this BSOD:

- **During gaming or heavy graphics use** — GPU driver causes win32kfull.sys to fault
- **After GPU driver update** — New driver incompatible with win32kfull.sys
- **With multiple monitors** — Multi-display setups stress the graphics subsystem
- **After Windows update** — Updated win32kfull.sys conflicts with existing GPU driver

## Common Causes

1. **Faulty GPU driver** — The display driver sends invalid commands to win32kfull.sys.
2. **Corrupted win32kfull.sys** — The system file itself is damaged.
3. **Incompatible GPU driver version** — Driver version doesn't match the current Windows build.
4. **Third-party overlay or hooking software** — Discord, OBS, or game overlays that inject into the graphics pipeline.

## Solutions

### Solution 1: Update or Reinstall GPU Drivers

The GPU driver's interaction with win32kfull.sys is the primary cause. Update or clean-reinstall the driver.

**Check installed GPU driver version:**

```powershell
Get-WmiObject Win32_VideoController | Select-Object Name, DriverVersion, DriverDate | Format-Table -AutoSize
```

**Perform a clean GPU driver reinstall:**

1. Download the latest driver from your GPU manufacturer (NVIDIA, AMD, or Intel).
2. Download [DDU (Display Driver Uninstaller)](https://www.guru3d.com/files-details/display-driver-uninstaller-download.html).
3. Boot into **Safe Mode**.
4. Run DDU and select **Clean and restart**.
5. After restart, install the fresh driver you downloaded.
6. Restart again.

### Solution 2: Disable Overlays and Hooking Software

Third-party software that overlays on games or hooks into the graphics pipeline can conflict with win32kfull.sys.

**Common culprits to disable temporarily:**

- **Discord** — Disable in-game overlay in Discord settings
- **Steam Overlay** — Right-click game > Properties > Uncheck "Enable the Steam Overlay"
- **NVIDIA GeForce Experience** — Disable in-game overlay in settings
- **AMD Radeon Software** — Disable in-game overlay
- **MSI Afterburner / RivaTuner** — Disable OSD overlay
- **OBS Studio** — Close completely while testing

**Check for injected DLLs in the graphics process:**

```powershell
Get-Process | Where-Object {$_.MainWindowTitle -ne ""} | ForEach-Object { $_.Modules } | Where-Object {$_.ModuleName -like "*overlay*" -or $_.ModuleName -like "*hook*"} | Select-Object ModuleName, FileName
```

### Solution 3: Repair System Files

If win32kfull.sys itself is corrupted, repair it with SFC and DISM.

```cmd
sfc /scannow
```

If SFC finds errors it cannot fix:

```cmd
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth
```

Run SFC again after DISM completes:

```cmd
sfc /scannow
```

**Verify win32kfull.sys integrity:**

```powershell
Get-FileHash "C:\Windows\System32\win32kfull.sys" -Algorithm SHA256
```

Compare the hash against a known-good system or Microsoft's file signatures.

### Solution 4: Update Windows

Microsoft frequently patches win32kfull.sys to fix compatibility issues with GPU drivers.

**Check for Windows updates:**

```powershell
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate
Install-WindowsUpdate -AcceptAll -AutoReboot
```

**Or use the built-in updater:**

```cmd
wuauclt /detectnow /updatenow
```

### Solution 5: Check for GPU Hardware Issues

If the BSOD persists across clean driver installs, the GPU hardware may be failing.

**Run a GPU stress test:**

1. Download FurMark or Unigine Heaven.
2. Run the test for 15-30 minutes.
3. Watch for artifacts, visual glitches, or crashes.

**Check GPU health in Event Viewer:**

```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; StartTime=(Get-Date).AddDays(-7)} | Where-Object {$_.Id -eq 4101 -or $_.Message -like "*win32kfull*"} | Select-Object TimeCreated, Id, Message | Format-Table -AutoSize
```

If stress tests fail consistently, the GPU may need replacement.

## Related Errors

- **[BSOD VIDEO_TDR_FAILURE]({{< relref "/windows/bsod-video-tdr-failure" >}})** — GPU hang timeout from the same graphics subsystem
- **[BSOD VIDEO_SCHEDULER_INTERNAL_ERROR]({{< relref "/windows/bsod-video-scheduler" >}})** — Video scheduler failure in the graphics stack
- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-system-thread-exception" >}})** — System thread crash from the same driver issues
- **[BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/windows/bsod-irql-not-less-or-equal" >}})** — Driver memory access violations
