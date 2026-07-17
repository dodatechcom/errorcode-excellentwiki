---
title: "COM Class Factory Error - How to Fix"
description: "Fix 'COM class factory error' on Windows 10 and 11. Resolve ClassFactory failures, cocreateinstance errors, and COM component instantiation issues."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# COM Class Factory Error

This error occurs when the COM class factory cannot create an instance of the requested COM class. The error typically reads:

> "ClassFactory cannot supply the class requested (Exception from HRESULT: 0x80040154)"

or

> "No class factory can be created for CLSID [CLSID]."

The class factory is responsible for creating COM object instances. When it fails, the entire COM activation chain breaks.

## Common Causes

- **Class factory not registered** — The DLL implementing the class factory is not registered.
- **DLL version mismatch** — Registered factory points to wrong DLL version.
- **32/64-bit conflict** — Class factory registered for wrong architecture.
- **Insufficient permissions** — Cannot access the class factory DLL.
- **Dependency chain failure** — One of the factory's dependencies is missing.

## How to Fix

### Re-register the COM Component

```cmd
regsvr32 "C:\Path\To\component.dll"
```

### Check Class Factory Registration

```cmd
reg query "HKCR\CLSID\{YOUR-CLSID}\InprocServer32" /ve
```

Verify the path points to the correct DLL.

### Verify DLL Exists

```powershell
$dllPath = (Get-ItemProperty -Path "HKCR:\CLSID\{YOUR-CLSID}\InprocServer32" -Name "(Default)")."(Default)"
Test-Path $dllPath
```

### Fix InprocServer32 Path

```cmd
reg add "HKCR\CLSID\{YOUR-CLSID}\InprocServer32" /ve /t REG_SZ /d "C:\Correct\Path\component.dll" /f
```

### Check 32-bit Component on 64-bit Windows

```cmd
reg query "HKCR\WOW6432Node\CLSID\{YOUR-CLSID}\InprocServer32" /ve
```

### Use Correct regsvr32 for Architecture

```cmd
:: Register 64-bit DLL
%SystemRoot%\System32\regsvr32.exe "component.dll"

:: Register 32-bit DLL
%SystemRoot%\SysWOW64\regsvr32.exe "component.dll"
```

### Check COM Debug Information

```powershell
Get-WinEvent -LogName Application -MaxEvents 20 | Where-Object { $_.Message -like "*class factory*" } | Format-List TimeCreated, Message
```

## Related Errors

- [COM Class Not Registered]({{< relref "/os/windows/com-class-not-registered" >}}) — Class missing from registry
- [COM Registration Error]({{< relref "/os/windows/com-registration-error" >}}) — Registration process failure
- [COM Activation Error]({{< relref "/os/windows/com-activation-error" >}}) — Overall activation failure
