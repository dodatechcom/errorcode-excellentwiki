---
title: "COM Access Denied Error - How to Fix"
description: "Fix 'COM access denied' errors on Windows 10 and 11. Configure DCOM permissions, launch/activation rights, and resolve COM security restrictions."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["com", "access-denied", "dcom-permissions", "launch-permissions"]
weight: 5
---

# COM Access Denied Error

This error occurs when a client application is denied permission to access or activate a COM object. The error typically reads:

> "Access is denied. (Exception from HRESULT: 0x80070005)"

or

> "COM access denied."

This commonly affects DCOM applications, services, and web applications trying to instantiate COM objects under specific user accounts.

## Common Causes

- **Insufficient launch permissions** — User account lacks COM launch rights.
- **DCOM security restrictions** — Default DCOM permissions deny access.
- **Running under wrong identity** — COM server configured to run under specific account.
- **UAC token filtering** — Elevated COM calls are filtered by User Account Control.
- **Network DCOM restrictions** — Remote COM access requires specific configuration.

## How to Fix

### Configure Launch and Activation Permissions

```cmd
dcomcnfg
```

Navigate to **Component Services > Computers > My Computer > DCOM Config**, right-click the component, select **Properties**, and go to the **Security** tab.

### Set COM Permissions via PowerShell

```powershell
$comAdmin = New-Object -ComObject COMAdmin.COMAdminCatalog
$apps = $comAdmin.GetCollection("Applications")
$apps.Populate()
```

### Grant DCOM Launch Permission via Registry

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Ole" /v "LegacyAuthenticationLevel" /t REG_DWORD /d 1 /f
reg add "HKLM\SOFTWARE\Microsoft\Ole" /v "LegacyImpersonationLevel" /t REG_DWORD /d 2 /f
```

### Configure COM Security for Specific User

```powershell
# Add user to COM launch and access permissions
$identity = "DOMAIN\Username"
$regPath = "HKLM:\SOFTWARE\Microsoft\Ole"
```

### Use Component Services GUI

1. Press **Win+R**, type `dcomcnfg`.
2. Expand **Component Services > Computers > My Computer**.
3. Right-click **My Computer > Properties**.
4. Go to **COM Security** tab.
5. Edit **Launch and Activation Permissions** under **Edit Limits**.

### Check UAC and Elevated COM

Run the application as the target user:

```powershell
Start-Process "app.exe" -Credential (Get-Credential)
```

## Related Errors

- [COM Access Denied]({{< relref "/os/windows/com-access-denied" >}}) — General COM permission denial
- [Access Denied (ERROR_ACCESS_DENIED)]({{< relref "/os/windows/win32-access-denied-win32" >}}) — Win32 access denied
- [COM STA Threading Error]({{< relref "/os/windows/com-sta-error" >}}) — Threading model issues
