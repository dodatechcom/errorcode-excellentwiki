---
title: "[Solution] HRESULT E_NOINTERFACE (0x80004002) — No Interface"
description: "Fix Windows HRESULT E_NOINTERFACE (0x80004002) no interface error. Causes and solutions for COM interface query failures."
platforms: ["windows"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["hresult", "e-nointerface", "0x80004002", "no-interface", "com", "queryinterface"]
weight: 5
---

# HRESULT E_NOINTERFACE (0x80004002) — No Interface

**Error Code:** `0x80004002`

E_NOINTERFACE indicates that a COM object does not support the requested interface when queried via `QueryInterface`.

## What This Error Means

This HRESULT is returned by `IUnknown::QueryInterface` when the object cannot provide the interface pointer the caller requested. The object may not implement the interface at all, or the interface may not be available in the current state.

## Common Causes

- Querying for an interface the COM object does not implement
- Using an incorrect IID (Interface ID) when calling QueryInterface
- Component version mismatch between client and server
- COM object not fully initialized or in a degraded state

## How to Fix

### Verify the Correct Interface IID

```cpp
// Ensure the IID matches the expected interface
hr = pObj->QueryInterface(IID_IOleClientSite, (void**)&pClientSite);
if (hr == E_NOINTERFACE) {
    // Object does not support this interface
    // Try an alternative interface
    hr = pObj->QueryInterface(IID_IOleObject, (void**)&pOleObject);
}
```

### Check COM Object Registration

```cmd
reg query "HKCR\CLSID\{YourCLSID}" /s
```

### Reinstall or Re-register the Component

```cmd
regsvr32 "C:\Path\To\YourComponent.dll"
```

### Use Interface Aggregation if Needed

For objects that support interface aggregation, ensure proper construction with `IUnknown` delegation.

## Related Errors

- [E_NOTIMPL (0x80004001)]({{< relref "/os/windows/hresult-e-notimpl" >}}) — Not implemented, related but for unimplemented methods
- [E_POINTER (0x80004003)]({{< relref "/os/windows/hresult-e-pointer" >}}) — Invalid pointer, null output pointer from QueryInterface
- [REGDB_E_CLASSNOTREG (0x80040154)]({{< relref "/os/windows/hresult-regdb-e-class" >}}) — Class not registered, cannot create object to query
