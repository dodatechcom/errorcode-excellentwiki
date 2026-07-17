---
title: "[Solution] Windows Update Error 0x800f0922 CBS_E_CONNECTOR_DISABLED Fix"
description: "Fix Windows Update error 0x800f0922 (CBS_E_CONNECTOR_DISABLED) on Windows 10 and 11. Enable the Windows Update service, reset components, and check network settings."
platforms: ["windows"]
severities: ["error"]
error_types: ["update-error"]
weight: 5
---

# [Solution] Windows Update Error 0x800f0922 CBS_E_CONNECTOR_DISABLED Fix

Error 0x800f0922 is a Windows Update error with the internal code `CBS_E_CONNECTOR_DISABLED`. It occurs when the Windows Update servicing stack is disabled or the system cannot connect to the Component-Based Servicing (CBS) component. The update agent fails to download or install updates because its connector has been deactivated.

This error affects both Windows 10 and 11 and is commonly caused by disabled Windows Update services, corrupted update components, or network restrictions blocking Microsoft's update endpoints.

## Description

The full error message typically reads:

> "There were problems downloading some updates, but we'll try again later. Error code: (0x800f0922)"

Or in the Windows Update log:

> "CBS_E_CONNECTOR_DISABLED: The CBS connector has been disabled."

This error indicates that the Component-Based Servicing connector — the component responsible for managing Windows update operations — has been turned off. This can happen due to Group Policy restrictions, third-party system optimization tools, or corrupted Windows Update services.

## Common Causes

- **Disabled Windows Update services** — The wuauserv or bits services have been stopped or disabled by Group Policy or optimization software.
- **Third-party system tuners** — Tools like O&O ShutUp10, ChrisPC Win10Tweaker, or similar software that disable Windows Update.
- **Corrupted update components** — The Windows Update agent files are damaged or missing.
- **Network restrictions** — Corporate firewalls or proxy servers blocking access to CBS endpoints.

## How to Fix

### Re-enable Windows Update Services

Ensure all required Windows Update services are running:

```cmd
sc config wuauserv start=auto
sc config bits start=auto
sc config cryptsvc start=auto
sc config trustedinstaller start=auto
```

Start the services:

```cmd
net start wuauserv
net start bits
net start cryptsvc
net start trustedinstaller
```

Verify services are running:

```powershell
Get-Service wuauserv, bits, cryptsvc, trustedinstaller | Select-Object Name, Status, StartType | Format-Table -AutoSize
```

### Reset Windows Update Components

If re-enabling services doesn't resolve the issue, perform a full component reset:

```cmd
net stop wuauserv
net stop cryptSvc
net stop bits
net stop msiserver
net stop appidsvc
```

Rename the cache folders:

```cmd
ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
ren C:\Windows\System32\catroot2 catroot2.old
```

Restart the services:

```cmd
net start appidsvc
net start cryptsvc
net start bits
net start wuauserv
net start msiserver
```

### Check Group Policy Settings

Third-party tools may have set Group Policy entries that disable Windows Update. Check the current policy:

```cmd
gpresult /h C:\gpreport.html
```

Open the report and look for policies related to Windows Update. Common culprits:

- **Configure Automatic Updates** — Set to Disabled
- **Remove access to use all Windows Update features**

If you have access to Group Policy Editor:

```cmd
gpedit.msc
```

Navigate to **Computer Configuration > Administrative Templates > Windows Components > Windows Update** and ensure the policies are set to **Not Configured** or **Enabled**.

Run `gpupdate /force` after making changes:

```cmd
gpupdate /force
```

### Run the Windows Update Troubleshooter

```cmd
msdt.exe /id WindowsUpdateDiagnostic
```

Or via Settings:

1. Press `Win + I` to open **Settings**.
2. Navigate to **System > Troubleshoot > Other troubleshooters**.
3. Locate **Windows Update** and click **Run**.

### Run SFC and DISM

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Manually Reset the Windows Update Agent

Download and run the Windows Update Troubleshooter from Microsoft's support site, or manually re-register the update DLLs:

```cmd
regsvr32.exe /s atl.dll
regsvr32.exe /s urlmon.dll
regsvr32.exe /s mshtml.dll
regsvr32.exe /s shdocvw.dll
regsvr32.exe /s browseui.dll
regsvr32.exe /s jscript.dll
regsvr32.exe /s vbscript.dll
regsvr32.exe /s scrrun.dll
regsvr32.exe /s msxml.dll
regsvr32.exe /s msxml3.dll
regsvr32.exe /s msxml6.dll
regsvr32.exe /s actxprxy.dll
regsvr32.exe /s softpub.dll
regsvr32.exe /s wintrust.dll
regsvr32.exe /s dssenh.dll
regsvr32.exe /s rsaenh.dll
regsvr32.exe /s gpkcsp.dll
regsvr32.exe /s sccbase.dll
regsvr32.exe /s slbcsp.dll
regsvr32.exe /s cryptdlg.dll
regsvr32.exe /s oleaut32.dll
regsvr32.exe /s ole32.dll
regsvr32.exe /s shell32.dll
regsvr32.exe /s wuaueng.dll
regsvr32.exe /s wuaueng1.dll
regsvr32.exe /s wucltui.dll
regsvr32.exe /s wups.dll
regsvr32.exe /s wups2.dll
regsvr32.exe /s wuweb.dll
regsvr32.exe /s qmgr.dll
regsvr32.exe /s qmgrprxy.dll
regsvr32.exe /s wucltux.dll
regsvr32.exe /s muweb.dll
regsvr32.exe /s wuwebv.dll
```

Restart your computer after running these commands and try Windows Update again.

## Examples

This error commonly occurs in these scenarios:

- **After running system optimization tools** — Software that disables Windows Update services to save resources.
- **On corporate-managed systems** — Group Policy blocks the CBS connector for update control.
- **After malware removal** — Malware that disabled services is removed, but the services remain disabled.
- **Following a system restore** — Restored system state has disabled update components.

## Related Errors

- [Error 0x80070002]({{< relref "/os/windows/windows-update-0x80070002" >}}) — File Not Found during Windows Update
- [Error 0x8024402c]({{< relref "/os/windows/windows-update-0x8024402c" >}}) — Windows Update cannot connect to update servers
- [Error 0x80070005]({{< relref "/os/windows/windows-update-0x80070005" >}}) — Access Denied during Windows Update
- [Error 0x80073712]({{< relref "/os/windows/windows-update-0x80073712" >}}) — Component store corrupted
