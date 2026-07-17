---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED (mrxsmb.sys) Windows 11/10 — Fixed"
description: "Fix Blue Screen SYSTEM_THREAD_EXCEPTION_NOT_HANDLED caused by mrxsmb.sys on Windows 10 and 11. Resolve SMB network driver issues and fix file sharing crashes."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "system-thread", "mrxsmb", "smb", "network", "file-sharing"]
weight: 5
---

# [Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED (mrxsmb.sys) Windows 11/10 — Fixed

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED caused by mrxsmb.sys is a critical Blue Screen of Death error with stop code `0x1000007E`. It indicates that the SMB (Server Message Block) redirector driver — mrxsmb.sys — generated an unhandled exception in a system thread. This driver is responsible for accessing files and resources on network shares.

This BSOD typically occurs on computers that frequently connect to network file shares, NAS devices, or network-attached storage. It points to issues with the SMB network file system driver, often caused by network configuration problems, corrupted SMB components, or incompatible network drivers.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: SYSTEM_THREAD_EXCEPTION_NOT_HANDLED
> What failed: mrxsmb.sys

mrxsmb.sys (also known as SMB Redirector) is a kernel-mode driver that handles client-side SMB file sharing operations. When Windows accesses a network share, this driver translates local file operations into SMB protocol commands. A fault in this driver can be caused by network driver issues, corrupted SMB configuration, or conflicts with third-party network software.

Common scenarios for this BSOD:

- **While accessing network shares** — Connecting to NAS or file servers triggers the crash
- **With mapped network drives** — Persistent network connections cause intermittent crashes
- **After network driver updates** — Updated NIC driver conflicts with SMB components
- **With VPN connections** — VPN network adapters interfere with SMB traffic
- **On domain-joined computers** — Group Policy or domain authentication issues

## Common Causes

1. **Corrupted SMB driver** — The mrxsmb.sys file or related SMB components are damaged.
2. **Network driver conflict** — The NIC driver is incompatible with the SMB redirector.
3. **Third-party network software** — VPN clients, firewalls, or network optimization tools conflict with SMB.
4. **Corrupted network configuration** — Winsock catalog or TCP/IP stack is damaged.

## Solutions

### Solution 1: Reset the Network Stack

A corrupted network configuration is a common cause. Reset the entire network stack.

**Reset Winsock and TCP/IP:**

```cmd
netsh winsock reset
netsh int ip reset
```

**Reset the network adapter:**

```cmd
netsh interface reset
```

**Flush DNS cache:**

```cmd
ipconfig /flushdns
```

**Reset Windows Firewall to defaults:**

```cmd
netsh advfirewall reset
```

Restart your computer after all commands complete.

### Solution 2: Repair System Files

The SMB driver is a Windows system file that can be repaired with SFC and DISM.

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

**Verify mrxsmb.sys integrity:**

```powershell
Get-FileHash "C:\Windows\System32\drivers\mrxsmb.sys" -Algorithm SHA256
```

### Solution 3: Update Network Adapter Drivers

The NIC driver must be compatible with the SMB redirector.

**Check current network driver version:**

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object {$_.DeviceClass -eq "Net"} | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

**Update via Device Manager:**

1. Right-click **Start** and select **Device Manager**.
2. Expand **Network adapters**.
3. Right-click your network adapter and select **Update driver**.
4. Choose **Search automatically for drivers**.

**Download the latest driver from your NIC manufacturer:**
- **Intel**: Intel Network Adapter driver
- **Realtek**: Realtek PCIe FE/GbE Family Controller driver
- **Killer**: Killer Networking driver

### Solution 4: Disable Third-Party Network Software

VPN clients, firewalls, and network optimization tools can conflict with SMB operations.

**Common software to temporarily disable:**

- VPN clients (Cisco AnyConnect, NordVPN, ExpressVPN)
- Third-party firewalls (ZoneAlarm, Comodo)
- Network optimization tools (TCP Optimizer, cFosSpeed)
- Antivirus network protection modules

**Check for problematic network filter drivers:**

```powershell
Get-NetAdapterBinding | Where-Object {$_.Enabled -eq $true} | Select-Object Name, ComponentID, DisplayName | Format-Table -AutoSize
```

If you identify a problematic third-party component, disable it and test.

### Solution 5: Disable SMB MultiChannel and SMB Signing

Some SMB features can cause driver issues on certain hardware configurations.

**Disable SMB Signing (not recommended for domain environments):**

```powershell
Set-SmbClientConfiguration -RequireSecuritySignature $false -Force
```

**Check SMB configuration:**

```powershell
Get-SmbClientConfiguration | Select-Object EnableMultiChannel, RequireSecuritySignature, EnableBandwidthThrottling | Format-Table -AutoSize
```

**Disable SMB MultiChannel if enabled:**

```powershell
Set-SmbClientConfiguration -EnableMultiChannel $false -Force
```

**Re-enable after testing:**

```powershell
Set-SmbClientConfiguration -RequireSecuritySignature $true -Force
Set-SmbClientConfiguration -EnableMultiChannel $true -Force
```

### Solution 6: Analyze the Minidump

Identify the exact code location in mrxsmb.sys causing the crash.

**Find the latest minidump:**

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

**Analyze with WinDbg:**

1. Install **WinDbg** from the Microsoft Store.
2. Open WinDbg and select **File > Open dump file**.
3. Open the most recent `.dmp` file.
4. Type `!analyze -v` and press Enter.
5. Look for the **FOLLOWUP_IP** and **STACK_TEXT** to identify the exact fault location.

## Related Errors

- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-system-thread-exception" >}})** — The general system thread exception error
- **[BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/windows/bsod-irql-not-less-or-equal" >}})** — Network driver memory access violations
- **[BSOD KMODE_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-kmode-exception2" >}})** — Kernel exception from faulty network drivers
- **[BSOD DPC_WATCHDOG_VIOLATION]({{< relref "/windows/bsod-dpc-watchdog2" >}})** — Storage and network driver timeout issues
