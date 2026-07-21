---
title: "[Solution] HRESULT CLASS_NOT_REGISTERED COM Error Fix"
description: "Fix HRESULT CLASS_NOT_REGISTERED (0x80040154) COM error on Windows. Resolve COM class registration failures and component instantiation errors."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] HRESULT CLASS_NOT_REGISTERED COM Error Fix

The HRESULT CLASS_NOT_REGISTERED (0x80040154) error means the COM class you are trying to instantiate is not registered in the system registry.

## Common Causes
- COM DLL was not registered during installation
- 32-bit vs 64-bit registration mismatch
- Class registered under HKLM but user lacks access
- Application referencing an old CLSID
- Corrupted COM registration in the registry

## How to Fix

### Solution 1: Register the COM DLL

```cmd
regsvr32 "C:\Path\To\Component.dll"
```

### Solution 2: Register 32-bit DLL on 64-bit Windows

```cmd
C:\Windows\SysWOW64\regsvr32.exe "C:\Path\To\Component.dll"
```

### Solution 3: Check Registry Entry

```cmd
reg query "HKCR\CLSID\{YOUR-CLSID}\InprocServer32"
```

### Solution 4: Reinstall the Application

Uninstall and reinstall the application that provides the COM component.

### Solution 5: Use Registry Editor

Open regedit and search for the CLSID to verify its InprocServer32 value is correct.

## Examples
```powershell
Get-ChildItem "HKLM:\SOFTWARE\Classes\CLSID" | Where-Object { $_.PSChildName -eq '{YOUR-CLSID}' }
```
