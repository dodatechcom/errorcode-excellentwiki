---
title: "[Solution] PowerShell Unauthorized Access to Script Fix"
description: "Fix PowerShell unauthorized access errors when scripts fail with access denied. Learn why permission issues occur and how to resolve them."
languages: ["powershell"]
severities: ["error"]
error-types: ["security-error"]
weight: 5
---

## What This Error Means

The PowerShell UnauthorizedAccessException occurs when the current user does not have permission to execute a script, access a file, or modify a system resource. This error is common when running scripts from protected directories, accessing system files, or modifying security-sensitive settings.

## Why It Happens

- The script file is in a directory requiring elevated permissions
- File system ACLs deny the current user execute or read permissions
- The script attempts to modify registry keys owned by SYSTEM
- Running scripts from a network share without proper authentication
- UAC (User Account Control) blocks elevated operations
- Antivirus or security software blocks script execution
- The script folder is marked as read-only

## How to Fix It

### Check and adjust file permissions

```powershell
# WRONG: Running script from restricted folder
C:\Windows\System32\my-script.ps1  # access denied

# CORRECT: Check permissions first
$acl = Get-Acl "C:\Scripts\my-script.ps1"
$acl.Access | Format-Table IdentityReference, FileSystemRights

# Or copy to a user-writable location
Copy-Item "C:\SystemFolder\script.ps1" "$env:TEMP\script.ps1"
& "$env:TEMP\script.ps1"
```

### Run with elevated privileges when needed

```powershell
# WRONG: Running system modification without elevation
Set-ItemProperty -Path "HKLM:\SOFTWARE\MyApp" -Name "Setting" -Value 1

# CORRECT: Check for admin and request elevation
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Start-Process powershell -Verb RunAs -ArgumentList "-File `"$PSCommandPath`""
    exit
}
# Now running as admin
Set-ItemProperty -Path "HKLM:\SOFTWARE\MyApp" -Name "Setting" -Value 1
```

### Fix ACLs for script directories

```powershell
# CORRECT: Grant execute permission to users
$path = "C:\Scripts"
$acl = Get-Acl $path
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule(
    "Users", "ReadAndExecute", "ContainerInherit,ObjectInherit", "None", "Allow"
)
$acl.SetAccessRule($rule)
Set-Acl -Path $path -AclObject $acl
```

### Handle network path access

```powershell
# WRONG: Script on network share without credentials
\\server\share\script.ps1  # access denied

# CORRECT: Map network drive with credentials
$cred = Get-Credential
New-PSDrive -Name "Scripts" -PSProvider FileSystem `
    -Root "\\server\share" -Credential $cred

& "Scripts:\script.ps1"
```

### Use Constrained Language Mode awareness

```powershell
# CORRECT: Check if Constrained Language Mode is active
if ($ExecutionContext.SessionState.LanguageMode -eq "ConstrainedLanguage") {
    Write-Warning "Running in Constrained Language Mode. Some features disabled."
}

# Some operations require FullLanguage mode
# This is controlled by AppLocker or WDAC policies
```

## Common Mistakes

- Assuming that being a local admin always grants full access to all paths
- Not checking if AppLocker or WDAC policies restrict script execution
- Forgetting that network drives may not be available in elevated sessions
- Using `Set-ExecutionPolicy` without understanding that it does not grant file system permissions
- Running scripts from `%TEMP%` where antivirus may block execution

## Related Pages

- [PowerShell Execution Policy](ps-execution-policy-v2) - script execution blocked
- [PowerShell Module Not Found](ps-module-not-found-v2) - module loading failed
- [PowerShell Certificate Store Error](ps-certstore-error) - certificate access denied
- [PowerShell Service Error](ps-service-error-v2) - service start/stop failed
