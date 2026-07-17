---
title: "COM Class Not Registered Error - How to Fix"
description: "Fix 'COM class not registered' errors on Windows 10 and 11. Register COM components, fix class IDs, and resolve component activation failures."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# COM Class Not Registered Error

This error occurs when an application tries to create a COM object but the required class is not registered in the Windows registry. The error typically reads:

> "Class not registered (Exception from HRESULT: 0x80040154)"

This commonly affects applications that depend on specific COM DLLs or components, especially after application updates, migrations, or corrupted installations.

## Common Causes

- **COM DLL not registered** — The DLL containing the COM class was never registered.
- **32-bit/64-bit mismatch** — 32-bit COM components registered in 64-bit environment or vice versa.
- **Corrupted registration** — Registry entries for the COM class are damaged.
- **DLL missing** — The registered DLL file is missing from disk.
- **Permission issue** — Cannot access the COM registration in the registry.

## How to Fix

### Register the COM DLL

```cmd
regsvr32 "C:\Path\To\component.dll"
```

For 32-bit DLLs on 64-bit Windows:

```cmd
regsvr32 "C:\Windows\SysWOW64\component.dll"
```

### Register with Full Path Using PowerShell

```powershell
& regsvr32.exe "C:\Program Files\Common Files\Microsoft Shared\component.dll" /s
```

### Check if COM Class is Registered

Search the registry for the CLSID:

```cmd
reg query "HKCR\CLSID\{YOUR-CLSID-HERE}" /s
```

Or search by name:

```cmd
reg query "HKCR" /s /f "ClassName" /d
```

### Re-register All COM DLLs

```powershell
Get-ChildItem "C:\Windows\System32\*.dll" | ForEach-Object { & regsvr32.exe $_.FullName /s 2>$null }
```

### Check 32-bit vs 64-bit Registration

```cmd
:: 64-bit components
reg query "HKCR\CLSID\{YOUR-CLSID-HERE}" /s

:: 32-bit components on 64-bit Windows
reg query "HKCR\WOW6432Node\CLSID\{YOUR-CLSID-HERE}" /s
```

### Use the Correct regsvr32

```cmd
:: For 64-bit DLLs
%SystemRoot%\System32\regsvr32.exe "path\to\dll"

:: For 32-bit DLLs
%SystemRoot%\SysWOW64\regsvr32.exe "path\to\dll"
```

## Related Errors

- [COM Registration Error]({{< relref "/os/windows/com-registration-error" >}}) — Registration process failures
- [COM Class Factory Error]({{< relref "/os/windows/com-factory-error" >}}) — Class factory creation failures
- [DLL Not Found]({{< relref "/os/windows/dll-not-found" >}}) — Missing DLL files
