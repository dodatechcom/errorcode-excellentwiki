---
title: "[Solution] HRESULT REGDB_E_CLASSNOTREG (0x80040154) — Class Not Registered"
description: "Fix Windows HRESULT REGDB_E_CLASSNOTREG (0x80040154) class not registered error. Causes and solutions for COM class registration failures."
platforms: ["windows"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# HRESULT REGDB_E_CLASSNOTREG (0x80040154) — Class Not Registered

**Error Code:** `0x80040154`

REGDB_E_CLASSNOTREG indicates that the requested COM class is not registered in the system registry. The CLSID or ProgID used to instantiate the object does not exist or has been removed.

## What This Error Means

This HRESULT is returned when `CoCreateInstance` or a similar COM activation call cannot find the class in the Windows registry. The CLSID mapping is missing, corrupted, or points to an invalid InprocServer32/LocalServer32 entry.

## Common Causes

- COM class was never registered or was uninstalled
- Registry entry for the CLSID is corrupted or incomplete
- 32-bit vs 64-bit registry redirection mismatch
- DCOM configuration is missing the class registration

## How to Fix

### Re-register the Component

```cmd
regsvr32 "C:\Path\To\Component.dll"
```

### Verify CLSID Registration

```cmd
reg query "HKCR\CLSID\{Your-CLSID-Here}" /s
```

### Fix 32/64-bit Registration Mismatch

For 32-bit components on 64-bit Windows:

```cmd
C:\Windows\SysWOW64\regsvr32.exe "C:\Path\To\32bitComponent.dll"
```

### Check Wow6432Node for 32-bit Entries

```cmd
reg query "HKCR\Wow6432Node\CLSID\{Your-CLSID-Here}" /s
```

### Use DISM to Repair COM Registration

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

## Related Errors

- [E_NOINTERFACE (0x80004002)]({{< relref "/os/windows/hresult-e-no-interface" >}}) — No interface, class exists but does not support requested interface
- [CO_E_OBJISCONNECTED (0x800401FD)]({{< relref "/os/windows/hresult-coclass" >}}) — COM object disconnected, server process lost
- [E_NOTIMPL (0x80004001)]({{< relref "/os/windows/hresult-e-notimpl" >}}) — Not implemented, class may be partially registered
