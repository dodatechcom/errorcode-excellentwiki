---
title: "[Solution] PowerShell EXECUTION_POLICY — Scripts Cannot Be Loaded"
description: "Fix PowerShell Execution Policy error with these step-by-step solutions. Includes PowerShell commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 1001
---

# [Solution] PowerShell EXECUTION_POLICY — Scripts Cannot Be Loaded

The PowerShell Execution Policy error prevents scripts from running because the system's security policy restricts script execution. This is a common issue when running `.ps1` files on Windows systems with default security settings.

## Description

When you attempt to run a PowerShell script, you may encounter an error stating that scripts cannot be loaded because running scripts is disabled on this system. The full error message reads:

> "File C:\script.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170."

The execution policy determines which scripts are allowed to run and under what conditions. The default policy on Windows client systems is `Restricted`, which blocks all scripts.

## Common Causes

1. The default execution policy is set to `Restricted`.
2. Group Policy overrides the local execution policy setting.
3. The script is digitally unsigned and the policy requires signed scripts.
4. The execution policy was changed by a system administrator or security tool.
5. Running PowerShell scripts from a network path with default security settings.
6. PowerShell profile scripts are blocked by the execution policy.

## Solutions

### Solution 1: Set Execution Policy to RemoteSigned

Allow local scripts to run while requiring downloaded scripts to be signed:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

For all users (requires Administrator):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
```

### Solution 2: Bypass Execution Policy for a Single Script

Run a specific script without changing the global policy:

```powershell
powershell -ExecutionPolicy Bypass -File "C:\path\to\script.ps1"
```

Or from within PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\script.ps1
```

### Solution 3: Set Execution Policy to Unrestricted

Allow all scripts to run (less secure):

```powershell
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```

### Solution 4: Check Current Execution Policy

Verify the current policy before making changes:

```powershell
Get-ExecutionPolicy
Get-ExecutionPolicy -List
```

### Solution 5: Remove Group Policy Override

Check if Group Policy is enforcing the policy:

```powershell
Get-ExecutionPolicy -List | Format-Table -AutoSize
```

If `MachinePolicy` or `UserPolicy` shows as the effective policy, contact your domain administrator to modify the Group Policy setting.

### Solution 6: Set Policy via Registry

If the GUI or cmdlet is blocked, set the policy directly in the registry:

```powershell
New-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell" -Name "EnableScripts" -Value 1 -PropertyType DWORD -Force
New-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell" -Name "ExecutionPolicy" -Value "RemoteSigned" -Force
```

## Related Errors

- [PowerShell Module Not Found]({{< relref "/os/windows/powershell-module-not-found" >}}) — Module cannot be loaded
- [PowerShell Remoting Error]({{< relref "/os/windows/powershell-remoting-error" >}}) — WSMan configuration error
- [PowerShell Script Block Logging Error]({{< relref "/os/windows/powershell-script-block-logging-error" >}}) — Script block logging failure
