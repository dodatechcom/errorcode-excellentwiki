---
title: "[Solution] Windows Update Error 0x80073D1A — Package Download Failed Fix"
description: "Fix Windows Update error 0x80073D1A (package could not be downloaded) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] Error 0x80073D1A — Package Could Not Be Downloaded Fix

Windows Update error 0x80073D1A indicates a package could not be downloaded. The system fails to retrieve the package from Microsoft's servers due to network issues or Store configuration problems.

## Description

The full error message reads:

> "Error 0x80073D1A: The package download operation failed."

This error occurs during the download phase of app or update installation. The Store or Windows Update service cannot complete the download due to network connectivity problems, proxy issues, or corrupted download cache.

## Common Causes

1. **Network connectivity issues** — Unstable internet connection during download.
2. **Corrupted download cache** — Damaged partial downloads preventing retry.
3. **Proxy or firewall blocking** — Network configuration blocking Store downloads.
4. **DNS resolution failure** — Cannot resolve Microsoft download server hostnames.

## Solutions

### Solution 1: Check Network Connectivity

```cmd
ping download.windowsupdate.com
nslookup www.microsoft.com
```

### Solution 2: Reset Windows Store

```cmd
wsreset.exe
```

### Solution 3: Clear Download Cache

```cmd
del /q/f/s C:\Windows\SoftwareDistribution\Download\*
net stop wuauserv
net start wuauserv
```

### Solution 4: Try Manual Download

Download the app or update package directly from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install it offline.

### Solution 5: Reset Network Settings

```cmd
netsh winsock reset
netsh int ip reset
ipconfig /flushdns
```

Restart your computer after running these commands.

## Related Errors

- [Error 0x80073D22]({{< relref "/os/windows/windows-update-0x80073d22" >}}) — Package resource limit
- [Error 0x8024402c]({{< relref "/os/windows/windows-update-0x8024402c" >}}) — Connection error
- [Error 0x80073D13]({{< relref "/os/windows/windows-update-0x80073d13" >}}) — Package dependency failed
