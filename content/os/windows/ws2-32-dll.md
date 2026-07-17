---
title: "[Solution] ws2_32.dll Error — Fix Windows Sockets DLL Error"
description: "Fix ws2_32.dll errors on Windows 10/11. Resolve Winsock DLL load failures and network socket errors in Windows applications."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["ws2_32", "winsock", "dll", "network", "socket", "tcp-ip"]
weight: 5
---

# ws2_32.dll Error — Windows Sockets DLL Error

A `ws2_32.dll` error occurs when a program cannot load or crashes in the Windows Sockets 2 DLL, which provides the TCP/IP networking API. The error may read:

> "The program can't start because ws2_32.dll is missing."

Or:

> "Exception code: 0xC0000005 — Access violation in ws2_32.dll"

## What This Error Means

`ws2_32.dll` is the Windows Sockets DLL that implements the BSD sockets API for TCP/IP networking in Windows. It is used by virtually every application that makes network connections — browsers, games, chat applications, and system services. A load failure is extremely rare since this is a core system DLL. Access violations usually indicate a corrupted Winsock catalog or a third-party network filter driver.

## Common Causes

- Corrupted Winsock catalog (LSP chain corruption)
- Third-party network filter driver or VPN client corrupting the stack
- Malware installed a malicious Layered Service Provider
- Winsock reset was interrupted
- System file corruption (rare)

## How to Fix

### Reset Winsock Catalog

```cmd
netsh winsock reset catalog
```

Restart the computer after running this command. It restores the Winsock catalog to the default state.

### Reset TCP/IP Stack

```cmd
netsh int ip reset reset.log
```

### Check Winsock Catalog

```cmd
netsh winsock show catalog
```

Verify that only expected providers are listed. Unknown or suspicious entries indicate malware or corrupted LSP chain.

### Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

### Check for Network Filter Drivers

```powershell
# List Winsock providers
Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Services\Winsock2\Parameters\Protocol_Catalog9\Catalog_Entries\*\PackedCatalogItem" -ErrorAction SilentlyContinue | Select-Object -ExpandProperty PathName
```

### Reinstall Network Adapter Drivers

```powershell
# Disable and re-enable the network adapter
Disable-NetAdapter -Name "Ethernet" -Confirm:$false
Enable-NetAdapter -Name "Ethernet" -Confirm:$false
```

## Related Errors

- [Network Connection Refused]({{< relref "/os/linux/connection-refused7" >}}) — TCP connection refused errors
- [DNS Resolution Failed]({{< relref "/os/linux/linux-k8s-dns-resolution" >}}) — DNS lookup failures
- [Socket Permission Denied]({{< relref "/os/linux/linux-docker-socket-permission" >}}) — Socket access errors
