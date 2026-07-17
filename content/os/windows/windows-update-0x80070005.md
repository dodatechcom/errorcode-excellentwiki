---
title: "[Solution] Windows Update Error 0x80070005 Access Denied Fix"
description: "Fix Windows Update error 0x80070005 (Access Denied) on Windows 10 and 11. Reset permissions, take ownership of files, and disable antivirus to resolve update failures."
platforms: ["windows"]
severities: ["error"]
error_types: ["update-error"]
weight: 5
---

# [Solution] Windows Update Error 0x80070005 Access Denied Fix

Error 0x80070005 is the Windows "Access Denied" error that blocks you from installing updates. It appears when Windows Update tries to write or modify system files but is denied the necessary permissions by the operating system.

This error affects both Windows 10 and 11 and is one of the most common barriers to completing Windows Updates. It can also affect file operations and application launches that require elevated privileges.

## Description

The full error message typically reads:

> "There were problems downloading some updates, but we'll try again later. Error code: (0x80070005)"

Or:

> "Error(s) found: Code 0x80070005. Windows Update ran into a problem."

Error 0x80070005 maps to the standard Windows `ACCESS_DENIED` result. The operating system's security subsystem explicitly blocked the requested operation. This can be triggered by user account permissions, Group Policy restrictions, or security software.

## Common Causes

- **Insufficient user account permissions** — Your account lacks the required privileges for the update operation.
- **Antivirus software interference** — Security programs locking system files during the update process.
- **Corrupted Windows Update database** — The SoftwareDistribution folder has permission or integrity issues.
- **File ownership issues** — System files owned by TrustedInstaller instead of the Administrators group.

## How to Fix

### Reset Windows Update Permissions

Take ownership of the update folders and grant full control:

```cmd
takeown /f "C:\Windows\SoftwareDistribution" /r /d y
icacls "C:\Windows\SoftwareDistribution" /grant administrators:F /t
takeown /f "C:\Windows\System32\catroot2" /r /d y
icacls "C:\Windows\System32\catroot2" /grant administrators:F /t
```

### Reset Windows Update Components

```cmd
net stop wuauserv
net stop cryptSvc
net stop bits
net stop msiserver
```

Clear the cache:

```cmd
rd /s /q "C:\Windows\SoftwareDistribution"
rd /s /q "C:\Windows\System32\catroot2"
```

Restart the services:

```cmd
net start wuauserv
net start cryptSvc
net start bits
net start msiserver
```

### Run as Administrator

Right-click **Command Prompt** in the Start menu and select **Run as administrator**. Then run:

```cmd
wuauclt /detectnow /updatenow
```

Or reset Windows Update components from the elevated prompt using the commands above.

### Temporarily Disable Antivirus

Third-party antivirus can lock files during the update process:

1. Open your antivirus application from the system tray.
2. Navigate to **Settings > Protection** or **Real-time scanning**.
3. **Disable** real-time protection for 15–30 minutes.
4. Run Windows Update.
5. **Re-enable** antivirus protection immediately after.

For Windows Defender:

```powershell
Set-MpPreference -DisableRealtimeMonitoring $true
```

Re-enable after:

```powershell
Set-MpPreference -DisableRealtimeMonitoring $false
```

### Check Group Policy Settings

```cmd
gpresult /h C:\gpreport.html
```

Look for denied policies under **Applied GPOs**. Common policies that cause 0x80070005:

- **User Account Control: Run all administrators in Admin Approval Mode**
- **Windows Update: Configure Automatic Updates**

If you have admin access, modify the policy through `gpedit.msc`:

```cmd
gpedit.msc
```

Navigate to **Computer Configuration > Administrative Templates > Windows Components > Windows Update** and adjust settings. Run `gpupdate /force` after changes.

### Fix Registry Permissions

If the error occurs during registry modifications:

1. Press `Win + R`, type `regedit`, and press **Ctrl + Shift + Enter**.
2. Navigate to the key you need to modify.
3. Right-click the key, select **Permissions**.
4. Click **Advanced** and then **Change** the owner to your account.
5. Grant your account **Full Control**.

### Run SFC and DISM

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

## Examples

This error commonly occurs in these scenarios:

- **During cumulative updates** — Monthly security updates fail to install due to permission issues.
- **After changing user accounts** — Switching to a new account without proper admin rights.
- **With aggressive antivirus** — Security software locking System32 files during update operations.
- **On enterprise systems** — Group Policy restrictions blocking update installation.

## Related Errors

- [Error 0x800f0922]({{< relref "/os/windows/windows-update-0x800f0922" >}}) — CBS connector disabled, update service issues
- [Error 0x80070002]({{< relref "/os/windows/windows-update-0x80070002" >}}) — File Not Found during Windows Update
- [Error 0x8024402c]({{< relref "/os/windows/windows-update-0x8024402c" >}}) — Windows Update connection error
- [Error 0x80073712]({{< relref "/os/windows/windows-update-0x80073712" >}}) — Component store corrupted
