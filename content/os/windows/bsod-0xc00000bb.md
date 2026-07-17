---
title: "[Solution] BSOD 0xc00000bb STATUS_NOT_SUPPORTED Windows 11/10 — Fixed"
description: "Fix Blue Screen error 0xc00000bb (STATUS_NOT_SUPPORTED) on Windows 10 and 11. Update drivers, check hardware compatibility, and repair system files to resolve this stop code."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD 0xc00000bb STATUS_NOT_SUPPORTED Windows 11/10 — Fixed

Error 0xc00000bb is a critical BSOD STOP error with the status code `STATUS_NOT_SUPPORTED`. It occurs when Windows or a driver attempts to use a feature, operation, or interface that is not supported by the hardware, firmware, or driver. The kernel halts because the operation cannot be completed with the available capabilities.

This error affects both Windows 10 and 11 and is commonly caused by driver incompatibility, outdated firmware, or hardware that lacks support for a requested operation.

## Common Causes

- **Incompatible driver** — A driver attempts to use a hardware feature that the device doesn't support.
- **Outdated BIOS/UEFI** — Motherboard firmware lacks support for a feature that the driver expects.
- **Legacy hardware** — Older hardware that doesn't support modern Windows features or APIs.
- **Corrupted driver installation** — A partially installed or corrupted driver sends unsupported requests.

## How to Fix

### Update All Drivers

Outdated or incompatible drivers are the primary cause:

```powershell
Get-WmiObject Win32_PnPSignedDriver | Sort-Object DriverDate -Descending | Select-Object -First 20 DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

Download the latest drivers from the hardware manufacturer's website. Focus on:
- **GPU drivers** — NVIDIA, AMD, Intel
- **Storage drivers** — AHCI, NVMe, RAID
- **Network drivers** — Ethernet and Wi-Fi adapters
- **Chipset drivers** — Motherboard chipset package

### Update BIOS/UEFI

```cmd
wmic baseboard get product,Manufacturer,version
```

Visit your motherboard manufacturer's website and download the latest BIOS version. Follow the flashing instructions exactly and ensure uninterrupted power.

### Check for Device Errors

```powershell
Get-WmiObject Win32_PnPEntity | Where-Object { $_.ConfigManagerErrorCode -ne 0 } | Select-Object Name, DeviceID, ConfigManagerErrorCode | Format-Table -AutoSize
```

Devices with errors may need driver updates, reinstallation, or physical removal.

### Reinstall the Problematic Driver

1. Open **Device Manager** (`Win + X` > Device Manager).
2. Find the device with the error.
3. Right-click and select **Uninstall device**.
4. Check **Attempt to remove the driver for this device**.
5. Restart your computer. Windows will reinstall the driver automatically.

**Or use PowerShell:**

```powershell
pnputil /enum-devices /driver oem*.inf
pnputil /delete-driver oemXX.inf /uninstall
```

### Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Check Hardware Compatibility

If the error occurs with a specific hardware device:

1. Verify the device is on the manufacturer's compatibility list for your version of Windows.
2. Check if the device requires specific drivers or firmware updates.
3. Try the device in a different USB port or PCIe slot.
4. Test the device on another computer to verify it's functioning correctly.

### Disable the Feature or Workaround

If a specific feature is unsupported:

1. Open **Device Manager**.
2. Right-click the device and select **Properties**.
3. Check the **Device Properties** for any feature toggles.
4. Disable advanced features that may not be supported by the hardware.

## Examples

This error commonly occurs in these scenarios:

- **After installing a new GPU** — The GPU driver uses a DirectX feature not supported by the card's firmware.
- **With legacy printers or scanners** — Older devices with drivers that use deprecated Windows APIs.
- **When connecting USB 3.0 devices to USB 2.0 ports** — The device expects USB 3.0 features that the port doesn't support.
- **After a Windows Update** — An update enables a new feature that older drivers cannot handle.

## Related Errors

- [BSOD 0xc000009a STATUS_INSUFFICIENT_RESOURCES]({{< relref "/os/windows/bsod-0xc000009a" >}}) — Resource exhaustion from incompatible drivers
- [BSOD KMODE_EXCEPTION_NOT_HANDLED]({{< relref "/os/windows/bsod-kmode-exception" >}}) — Kernel exception from driver incompatibility
- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/os/windows/bsod-system-thread-exception" >}}) — System thread crash from unsupported operations
- [BSOD 0xc0000420 STATUS_AUTHENTICATION_FIREWALL_FAILED]({{< relref "/os/windows/bsod-0xc0000420" >}}) — Authentication failure from filter driver conflicts
