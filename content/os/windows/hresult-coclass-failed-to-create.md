---
title: "[Solution] HRESULT CO_E_CLASS_CREATE_FAILED Fix"
description: "Fix HRESULT CO_E_CLASS_CREATE_FAILED error on Windows when COM cannot instantiate a requested class object from its CLSID or ProgID."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] HRESULT CO_E_CLASS_CREATE_FAILED Fix

The CO_E_CLASS_CREATE_FAILED HRESULT error (0x80040154) means the COM runtime was unable to create an instance of the requested class. The class factory could not be located or the constructor failed.

## Common Causes
- The COM DLL or EXE server is not registered in the system
- 32-bit and 64-bit COM registration path conflict
- Insufficient permissions to instantiate the class
- Corrupted class factory registration in the registry
- DLL dependency missing from the search path

## How to Fix

### Solution 1: Register the COM Component

```cmd
regsvr32 "C:\Path\To\Component.dll"
```

### Solution 2: Use Correct Architecture Command Prompt

For 32-bit COM components on 64-bit Windows:

```cmd
C:\Windows\SysWOW64\regsvr32.exe "C:\Path\To\Component.dll"
```

### Solution 3: Verify CLSID Registration

```cmd
reg query "HKCR\CLSID\{YOUR-CLSID}\InprocServer32"
```

Confirm the DLL path in the registry matches the actual file location.

### Solution 4: Check Component Permissions

Ensure the user account has Launch and Activation permissions for the COM component through dcomcnfg.

### Solution 5: Reinstall the Application

Uninstall and reinstall the application that provides the COM component to re-register all necessary classes.

## Examples
```powershell
Get-ItemProperty "HKLM:\SOFTWARE\Classes\CLSID\{YOUR-CLSID}" -ErrorAction SilentlyContinue
```
