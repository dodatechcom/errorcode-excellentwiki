---
title: "[Solution] Windows Update Error 0x80244022 Fix"
description: "Fix Windows Update error 0x80244022 WU_E_PT_HTTP_STATUS_SERVICE_UNAVAIL when the update service is temporarily unavailable on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Windows Update Error 0x80244022 Fix

Windows Update error 0x80244022 (WU_E_PT_HTTP_STATUS_SERVICE_UNAVAIL) means the Windows Update service received an HTTP 503 Service Unavailable response from the update servers.

## Common Causes
- Microsoft Update servers experiencing high traffic
- Proxy or firewall blocking HTTPS connections to update servers
- Third-party security software interfering with update traffic
- VPN connection causing routing issues to update servers
- Windows Update service throttling from previous errors

## How to Fix

### Solution 1: Wait and Retry

This is often a temporary server-side issue. Wait 15 to 30 minutes and try again.

### Solution 2: Check Proxy Settings

```cmd
netsh winhttp show proxy
```

### Solution 3: Reset Windows Update Components

```cmd
net stop wuauserv
net stop cryptSvc
net stop bits
net stop msiserver
ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
net start wuauserv
net start cryptSvc
net start bits
net start msiserver
```

### Solution 4: Run the Windows Update Troubleshooter

Go to Settings > System > Troubleshoot and run the Windows Update troubleshooter.

### Solution 5: Disable VPN Temporarily

Disconnect any VPN connections and retry the update.

## Examples
```powershell
Test-NetConnection -ComputerName fe2cr.ws.microsoft.com -Port 443
```
