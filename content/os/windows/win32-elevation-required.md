---
title: "[Solution] Error 740 — ELEVATION_REQUIRED Fix"
description: "Fix Windows Error Code (ELEVATION_REQUIRED) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 740
---

# [Solution] Error 740 — ELEVATION_REQUIRED Fix

Win32 error 740 (`ERROR_ELEVATION_REQUIRED`) occurs when the requested operation requires elevation. This error is triggered by User Account Control (UAC) when an application needs administrator privileges to run.

## Description

The ELEVATION_REQUIRED error is returned when a program or script attempts to perform an operation that requires administrator-level privileges but was launched without elevation. This is one of the most common Windows errors since the introduction of UAC in Windows Vista. The error code is `ERROR_ELEVATION_REQUIRED` (value 740). The full message reads:

> "The requested operation requires elevation."

## Common Causes

1. The application requires administrator privileges to run.
2. The program was launched without using "Run as administrator."
3. The application manifest specifies `requireAdministrator`.
4. The operation modifies protected system areas (registry, Program Files).
5. A service requires elevated permissions to start.
6. UAC settings are set to the highest level.

## Solutions

### Solution 1: Run as Administrator

Right-click the application and select **Run as administrator**, or launch from an elevated prompt:

```powershell
# Launch with elevation
Start-Process "C:\Path\To\app.exe" -Verb RunAs
```

```cmd
:: Use runas to launch with different credentials
runas /user:Administrator "C:\Path\To\app.exe"
```

### Solution 2: Check UAC Settings

Review and adjust UAC settings if appropriate:

```powershell
# Check current UAC level
Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name EnableLUA
```

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System]
"EnableLUA"=dword:00000001
"ConsentPromptBehaviorAdmin"=dword:00000005
```

### Solution 3: Use runas Command

Launch the program with different credentials:

```cmd
:: Run as a specific user
runas /user:DOMAIN\AdminAccount "C:\Path\To\app.exe"

:: Run as current user in elevated mode
powershell -Command "Start-Process cmd -Verb RunAs"
```

### Solution 4: Create an Elevated Shortcut

Create a shortcut that automatically runs as administrator:

```powershell
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("C:\Desktop\ElevatedApp.lnk")
$Shortcut.TargetPath = "C:\Path\To\app.exe"
$Shortcut.Save()

# To elevate, the shortcut must be launched via a scheduled task or manually right-clicked
```

### Solution 5: Configure Application Manifest

If you are the developer, set the application to request elevation in its manifest:

```xml
<requestedExecutionLevel level="requireAdministrator" uiAccess="false" />
```

## Related Errors

- [Error 5 — ACCESS_DENIED]({{< relref "/os/windows/win32-access-denied-win32" >}}) — Access is denied
- [Error 86 — INVALID_PASSWORD]({{< relref "/os/windows/win32-invalid-password" >}}) — Invalid network password
- [Error 65 — NETWORK_ACCESS_DENIED]({{< relref "/os/windows/win32-network-access-denied" >}}) — Network access is denied
