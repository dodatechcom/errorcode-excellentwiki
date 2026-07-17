---
title: "[Solution] BSOD DPC_WATCHDOG_VIOLATION (storahci.sys) Windows 11/10 — Fixed"
description: "Fix Blue Screen DPC_WATCHDOG_VIOLATION caused by storahci.sys on Windows 10 and 11. Update SATA AHCI drivers and fix storage controller issues."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD DPC_WATCHDOG_VIOLATION (storahci.sys) Windows 11/10 — Fixed

DPC_WATCHDOG_VIOLATION caused by storahci.sys is a critical Blue Screen of Death error with stop code `0x00000133`. It indicates that the Standard SATA AHCI Controller driver (storahci.sys) timed out during a deferred procedure call (DPC). The storage controller took too long to complete an I/O operation, triggering the watchdog timer.

This specific variant of DPC Watchdog Violation is caused by the default Windows SATA AHCI driver — not a third-party driver. It typically means the storage controller is not communicating properly with the hard drive or SSD, often due to outdated BIOS, AHCI power management issues, or a failing drive.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: DPC_WATCHDOG_VIOLATION
> What failed: storahci.sys

storahci.sys is the Microsoft Standard SATA AHCI Controller driver. It manages communication between Windows and SATA devices using the AHCI protocol. When a SATA device takes too long to respond to a command — due to power management, firmware bugs, or hardware failure — the DPC watchdog timer expires and Windows crashes.

Common scenarios for this BSOD:

- **On systems with SATA SSDs** — The SSD's response time exceeds the DPC timeout
- **After BIOS update** — New BIOS settings conflict with AHCI behavior
- **With AHCI power management enabled** — Link State Power Management causes timeouts
- **During heavy disk I/O** — Large file transfers overwhelm the storage controller

## Common Causes

1. **AHCI Link State Power Management** — The SATA link enters a low-power state and cannot wake up in time.
2. **Outdated BIOS/UEFI** — The motherboard firmware has AHCI compatibility bugs.
3. **Failing SATA drive** — The drive's response time degrades as it fails.
4. **Standard AHCI driver limitations** — The generic Microsoft driver lacks features specific to your hardware.

## Solutions

### Solution 1: Disable AHCI Link State Power Management

The most common fix is disabling SATA power management that causes timeouts.

**Using PowerShell:**

```powershell
powercfg /setacvalueindex SCHEME_CURRENT SUB_DISK AHCIHIPM 0
powercfg /setactive SCHEME_CURRENT
```

**Using Device Manager:**

1. Open **Device Manager**.
2. Expand **IDE ATA/ATAPI controllers**.
3. Right-click **Standard SATA AHCI Controller** and select **Properties**.
4. Go to the **Policies** or **Power Management** tab.
5. Uncheck **Allow the computer to turn off this device to save power**.
6. Click **OK**.

**Set power plan to High Performance:**

```cmd
powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c
```

**Disable Hibernate to prevent deep sleep states:**

```cmd
powercfg -h off
```

### Solution 2: Update to Manufacturer-Specific AHCI Driver

The generic storahci.sys driver lacks optimizations for specific hardware. Install the manufacturer's driver.

**Check current storage driver:**

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object {$_.DeviceClass -eq "SCSIAdapter"} | Select-Object DeviceName, DriverVersion, DriverDate, InfName | Format-Table -AutoSize
```

**For Intel systems — install Intel Rapid Storage Technology (IRST):**

1. Go to [Intel's download center](https://www.intel.com/content/www/us/en/download-center/home.html).
2. Search for **Intel Rapid Storage Technology**.
3. Download and install the latest version.
4. Restart your computer.

**For AMD systems — install AMD SATA/StoreMI driver:**

1. Visit your motherboard manufacturer's website.
2. Find the AMD SATA driver for your specific motherboard model.
3. Download and install.

**If you need to change the driver in Device Manager:**

1. Open **Device Manager** > **IDE ATA/ATAPI controllers**.
2. Right-click **Standard SATA AHCI Controller**.
3. Select **Update driver** > **Browse my computer for drivers**.
4. Select **Let me pick from a list of available drivers**.
5. If manufacturer-specific drivers are available, select them.

### Solution 3: Update BIOS/UEFI

An outdated BIOS is a frequent cause of storahci.sys timeouts.

**Identify your motherboard:**

```cmd
wmic baseboard get product,Manufacturer,version
```

1. Visit your motherboard manufacturer's website (ASUS, MSI, Gigabyte, ASRock, Dell, HP).
2. Find the support page for your exact model.
3. Download the latest BIOS update.
4. Follow the manufacturer's instructions carefully.

**Warning:** Never interrupt a BIOS update. Ensure your computer is plugged into a reliable power source.

### Solution 4: Check Drive Health

A failing drive can cause the storage controller to timeout waiting for responses.

**Check SMART status:**

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Temperature, Wear, ReadErrorsTotal, WriteErrorsTotal | Format-Table -AutoSize
```

**Run CHKDSK:**

```cmd
chkdsk C: /f /r
```

Press `Y` to schedule for next restart, then reboot.

**Check drive health:**

```powershell
Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus, Size | Format-Table -AutoSize
```

Any errors or degraded health indicate the drive needs replacement.

### Solution 5: Adjust SATA Link Speed

Forcing a lower SATA link speed can stabilize unreliable connections.

**In BIOS/UEFI:**

1. Enter BIOS/UEFI (press `Del`, `F2`, or `F12` during boot).
2. Navigate to **Storage Configuration** or **SATA Configuration**.
3. Look for **SATA Link Speed** or **SATA Mode**.
4. If set to Auto, try forcing **SATA 3 Gb/s (SATA II)** instead of **SATA 6 Gb/s (SATA III)**.
5. Save and exit.

This reduces the maximum speed but can stabilize a failing connection.

## Related Errors

- **[BSOD DPC_WATCHDOG_VIOLATION (General)]({{< relref "/windows/bsod-dpc-watchdog-violation" >}})** — The broader DPC watchdog error covering all storage drivers
- **[BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/windows/bsod-kernel-data-inpage" >}})** — Disk read failures from the same storage issues
- **[BSOD INACCESSIBLE_BOOT_DEVICE]({{< relref "/windows/bsod-inaccessible-boot" >}})** — Boot drive failure from storage controller problems
- **[BSOD NTFS_FILE_SYSTEM]({{< relref "/windows/bsod-ntfs-file" >}})** — NTFS corruption from storage I/O errors
