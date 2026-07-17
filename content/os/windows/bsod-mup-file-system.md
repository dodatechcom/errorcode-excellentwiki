---
title: "[Solution] BSOD MUP_FILE_SYSTEM Windows 11/10 — Fixed"
description: "Fix Blue Screen MUP_FILE_SYSTEM error on Windows 10 and 11. Update network and file system drivers, check disk health, and repair system files to resolve this stop code."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD MUP_FILE_SYSTEM Windows 11/10 — Fixed

MUP_FILE_SYSTEM is a critical Blue Screen of Death error with stop code `0x00000044` (or sometimes referenced by the `mups.sys` driver). It occurs when the Multiple UNC Provider (MUP) — the Windows component responsible for redirecting file system requests to network shares — encounters a fatal error. The MUP driver routes file operations to the appropriate network mini-redirector, and when this redirection fails, the system crashes.

This BSOD affects both Windows 10 and 11 and is typically related to network file sharing, mapped drives, or network file system drivers.

## Common Causes

- **Corrupted network file system driver** — The MUP driver or a network mini-redirector is damaged or incompatible.
- **Network storage issues** — A NAS, network share, or DFS path that becomes unreachable during active file operations.
- **Outdated SMB or network drivers** — The Server Message Block (SMB) client or network adapter driver has bugs in its file redirection logic.
- **Corrupted system files** — Windows system files that the MUP component depends on are damaged.

## How to Fix

### Disconnect Network Drives

If mapped network drives are active when the crash occurs:

1. Open **File Explorer**.
2. Right-click each mapped network drive and select **Disconnect**.
3. If the BSOD stops occurring, the issue is with the network share or its configuration.

**Or disconnect all mapped drives from Command Prompt:**

```cmd
net use * /delete /y
```

### Update Network Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "NET" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

Download the latest network adapter drivers from the hardware manufacturer's website. Focus on:
- **Ethernet NIC drivers** — Intel, Realtek, Broadcom
- **Wi-Fi adapter drivers** — Intel, Qualcomm, Realtek

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

The MUP driver is a core Windows component — system file corruption can directly cause this BSOD.

### Check Disk Health

```cmd
chkdsk C: /f /r
```

Press `Y` to schedule for next restart. Disk corruption can damage the MUP driver or related system files.

### Update Windows

Windows updates include fixes for the SMB client and network file system components:

```powershell
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate -AcceptAll -Install -AutoReboot
```

### Check Network Share Health

If the BSOD occurs when accessing a specific network share:

1. Verify the network share is accessible: `net view \\server-name`
2. Check the SMB version in use:

```powershell
Get-SmbConnection | Select-Object ServerName, ShareName, UserName, NumOpens | Format-Table -AutoSize
```

3. Ensure the NAS or file server firmware is up to date.
4. If using DFS, verify DFS namespace health:

```powershell
Get-DfsnRoot | Select-Object Path, Type, State | Format-Table -AutoSize
```

### Boot into Safe Mode and Test

1. Hold `Shift` and click **Restart**.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**.
3. Press `4` or `F4` for Safe Mode.

If the BSOD doesn't occur in Safe Mode, a third-party network filter driver is likely the cause.

## Examples

This error commonly occurs in these scenarios:

- **When accessing a network share** — A mapped drive or UNC path triggers a fatal MUP redirection error.
- **After connecting to a new NAS** — The network mini-redirector for the NAS is incompatible with the Windows MUP driver.
- **During large file transfers over SMB** — Sustained network I/O exposes bugs in the network file system driver.
- **With VPN connections active** — VPN network filter drivers interfere with MUP file redirection.

## Related Errors

- [BSOD NTFS_FILE_SYSTEM]({{< relref "/os/windows/bsod-ntfs-file-system" >}}) — Local NTFS file system corruption
- [BSOD FAT_FILE_SYSTEM]({{< relref "/os/windows/bsod-fat-file-system" >}}) — FAT volume file system error
- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-driver-irql-not-less-or-equal" >}}) — Network driver accessing memory at invalid IRQL
- [BSOD DPC Watchdog Violation]({{< relref "/os/windows/bsod-dpc-watchdog-violation" >}}) — Driver timeout from I/O issues
