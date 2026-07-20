---
title: "[Solution] PowerShell SCRIPT_BLOCK_LOGGING — Script Block Logging Error"
description: "Fix PowerShell Script Block Logging error with these step-by-step solutions. Includes PowerShell commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 1003
---

# [Solution] PowerShell SCRIPT_BLOCK_LOGGING — Script Block Logging Error

The PowerShell Script Block Logging error occurs when the system fails to log or record PowerShell script block execution. This is critical for security monitoring and auditing environments that rely on script block logs for threat detection.

## Description

Script Block Logging records the content of all script blocks that are processed by the PowerShell engine. When this feature encounters errors, it can produce Event Log warnings or fail silently, leaving gaps in your audit trail. A common event related to script block logging errors appears in the Windows Event Log:

> "PowerShell script block logging has encountered an error while logging a script block. The script block may not have been logged."

This error is often associated with Event ID 4103 or 4104 in the Microsoft-Windows-PowerShell/Operational log.

## Common Causes

1. Script Block Logging is not enabled in the PowerShell logging policy.
2. The PowerShell Operational Event Log is full or corrupted.
3. Group Policy settings conflict with local logging configuration.
4. The script block is too large and exceeds the logging limit.
5. Insufficient disk space prevents writing to the Event Log.
6. The Microsoft-Windows-PowerShell event log provider is damaged.
7. Antivirus or security software interferes with the logging mechanism.

## Solutions

### Solution 1: Enable Script Block Logging via Group Policy

Enable logging through Group Policy Editor:

```powershell
# Enable via registry if Group Policy is not available
$regPath = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"
New-Item -Path $regPath -Force
New-ItemProperty -Path $regPath -Name "EnableScriptBlockLogging" -Value 1 -PropertyType DWORD -Force
```

### Solution 2: Clear the PowerShell Operational Event Log

A full or corrupted event log can prevent logging:

```powershell
wevtutil cl "Microsoft-Windows-PowerShell/Operational"
```

Or through PowerShell:

```powershell
Clear-Log -LogName "Microsoft-Windows-PowerShell/Operational"
```

### Solution 3: Increase Event Log Size

Expand the maximum log size for the PowerShell Operational log:

```powershell
wevtutil sl "Microsoft-Windows-PowerShell/Operational" /ms:1073741824
```

This sets the log size to 1 GB.

### Solution 4: Enable Module Logging Alongside Script Block Logging

Enable comprehensive logging for better diagnostics:

```powershell
$regPath = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ModuleLogging"
New-Item -Path $regPath -Force
New-ItemProperty -Path $regPath -Name "EnableModuleLogging" -Value 1 -PropertyType DWORD -Force

$modulesPath = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ModuleLogging\ModuleNames"
New-Item -Path $modulesPath -Force
New-ItemProperty -Path $modulesPath -Name "*" -Value "*" -Force
```

### Solution 5: Verify Logging Status

Check if script block logging is currently enabled:

```powershell
$logName = "Microsoft-Windows-PowerShell/Operational"
Get-WinEvent -LogName $logName -MaxEvents 10 | Where-Object { $_.Id -in @(4103, 4104) }
```

### Solution 6: Reinstall the PowerShell Event Log Provider

If the event log channel is corrupted:

```powershell
wevtutil set-log "Microsoft-Windows-PowerShell/Operational" /enabled:true /maxsize:1073741824
```

## Related Errors

- [PowerShell Execution Policy Error]({{< relref "/os/windows/powershell-execution-policy-error" >}}) — Scripts cannot be loaded
- [PowerShell Remoting Error]({{< relref "/os/windows/powershell-remoting-error" >}}) — WSMan configuration error
- [PowerShell DSC Error]({{< relref "/os/windows/powershell-desired-state-configuration-error" >}}) — Configuration failed
