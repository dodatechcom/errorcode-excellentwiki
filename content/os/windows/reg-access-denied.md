---
title: "Registry Access Denied Error - How to Fix"
description: "Fix 'Registry access denied' errors on Windows 10 and 11. Resolve permission issues, restore registry access, and regain control of registry keys."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Registry Access Denied Error

This error occurs when you try to access, modify, or delete a registry key or value but Windows blocks the operation due to insufficient permissions. The full message may read:

> "Cannot open [key name]: Error while opening key."

or

> "Registry access denied."

This commonly appears in `regedit`, PowerShell `Set-ItemProperty`, or third-party tools attempting to modify the Windows Registry.

## Common Causes

- **Insufficient user permissions** — Your account lacks read/write access to the registry key.
- **Registry key owned by SYSTEM or TrustedInstaller** — Critical keys are protected by Windows.
- **UAC elevation missing** — Registry changes require administrator privileges.
- **Malware or third-party software** has locked or restricted registry keys.
- **Group Policy restrictions** — Domain policies may prevent registry access.

## How to Fix

### Run Registry Editor as Administrator

Right-click `regedit.exe` and select **Run as administrator**, or launch it from an elevated terminal:

```powershell
Start-Process regedit -Verb RunAs
```

### Take Ownership of the Registry Key

Use `reg` command to take ownership from an elevated Command Prompt:

```cmd
reg add "HKLM\SOFTWARE\YourKey" /v "ValueName" /t REG_SZ /d "data" /f
```

Or use PowerShell to change owner and permissions:

```powershell
$key = "HKLM:\SOFTWARE\YourKey"
$acl = Get-Acl $key
$rule = New-Object System.Security.AccessControl.RegistryAccessRule("Administrators", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
$acl.AddAccessRule($rule)
Set-Acl $key $acl
```

### Use SYSTEM Privileges with PsExec

For keys owned by SYSTEM account:

```cmd
psexec -s regedit
```

Download [PsExec](https://learn.microsoft.com/en-us/sysinternals/downloads/psexec) from Sysinternals first.

### Check Current Permissions

View the current access control list for a registry key:

```powershell
Get-Acl "HKLM:\SOFTWARE\YourKey" | Format-List
```

### Reset Registry Permissions

Restore default permissions using the Security Configuration Wizard:

```powershell
secedit /configure /cfg %windir%\inf\defltbase.inf /db defltbase.sdb /verbose
```

**Warning:** This resets security settings to defaults. Use only as a last resort.

## Related Errors

- [Registry Key Not Found]({{< relref "/os/windows/reg-key-not-found" >}}) — Key doesn't exist in the registry
- [Registry Write Protected]({{< relref "/os/windows/reg-write-protected" >}}) — Registry is in read-only mode
- [Access Denied 0x80070005]({{< relref "/os/windows/0x80070005" >}}) — General Windows access denied error
