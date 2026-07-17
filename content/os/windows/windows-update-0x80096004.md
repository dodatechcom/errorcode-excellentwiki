---
title: "[Solution] Windows Update Error 0x80096004 Certificate Error Fix"
description: "Fix Windows Update error 0x80096004 (certificate trust failure) on Windows 10 and 11. Resolve update signature verification errors with certificate updates and store repairs."
platforms: ["windows"]
severities: ["error"]
error_types: ["system-error"]
tags: ["windows-update", "0x80096004", "certificate", "signature", "trust"]
weight: 5
---

# [Solution] Windows Update Error 0x80096004 Certificate Error Fix

Error 0x80096004 means Windows Update failed to verify the digital certificate of the update package. This is a certificate trust error that prevents the update from being installed because its signature cannot be validated.

This error can occur when the Windows certificate store is outdated, when an intermediate certificate is missing, or when system time is incorrect.

## What This Error Means

The full error message typically reads:

> "Some updates were not installed. Errors found: Code 0x80096004. Windows Update ran into a problem."

Error 0x80096004 maps to a certificate trust verification failure. Windows Update cannot confirm that the update package was signed by a trusted authority. Common triggers include:

- **Outdated certificate store** — Root or intermediate certificates are expired or missing
- **Incorrect system time** — Certificate validation depends on correct time
- **Corrupted certificate store** — Damaged certificate database from updates or malware
- **Proxy or firewall interception** — Network devices intercepting HTTPS connections

## Common Causes

1. **Outdated certificate store** — Missing or expired root/intermediate certificates.
2. **Incorrect system time** — Certificate validation fails with wrong system clock.
3. **Corrupted certificate store** — Damaged certificate database.
4. **Proxy or firewall interception** — Network devices breaking certificate chains.

## How to Fix

### Verify System Time

Certificate validation depends on accurate system time:

```powershell
Get-Date
w32tm /query /status
```

If the time is incorrect:

```cmd
w32tm /resync
```

Or set it manually:

```cmd
net stop w32time
w32tm /unregister
w32tm /register
net start w32time
w32tm /resync /force
```

### Update Root Certificates

```cmd
certutil -generateSSTFromWU roots.sst
certutil -addstore Root roots.sst
```

Delete the SST file after:

```cmd
del roots.sst
```

### Repair the Certificate Store

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

### Reset Windows Update Components

```cmd
net stop wuauserv
net stop cryptSvc
net stop bits
net stop msiserver
rd /s /q "C:\Windows\SoftwareDistribution"
rd /s /q "C:\Windows\System32\catroot2"
net start wuauserv
net start cryptSvc
net start bits
net start msiserver
```

### Check for Proxy/Firewall Issues

Temporarily disable any proxy:

```cmd
netsh winhttp reset proxy
```

If behind a corporate proxy, ensure it does not intercept HTTPS update connections.

### Download and Install Manually

1. Note the KB number from Windows Update.
2. Visit [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. Download and install the update manually.

## Related Errors

- [Error 0x800b0109]({{< relref "/os/windows/windows-update-0x800b0109" >}}) — Certificate chain error
- [Error 0x80070005]({{< relref "/os/windows/windows-update-0x80070005" >}}) — Access Denied during update
- [Error 0x800f0922]({{< relref "/os/windows/windows-update-0x800f0922" >}}) — Connection timeout
