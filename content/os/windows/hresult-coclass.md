---
title: "[Solution] HRESULT CO_E_OBJISCONNECTED (0x800401FD) — COM Object Disconnected"
description: "Fix Windows HRESULT CO_E_OBJISCONNECTED (0x800401FD) COM object disconnected error. Causes and solutions for distributed COM connection failures."
platforms: ["windows"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["hresult", "co-e-objisconnected", "0x800401fd", "com", "dcom", "disconnected"]
weight: 5
---

# HRESULT CO_E_OBJISCONNECTED (0x800401FD) — COM Object Disconnected

**Error Code:** `0x800401FD`

CO_E_OBJISCONNECTED indicates that the COM object has been disconnected from its server or the remote machine hosting the object is no longer accessible.

## What This Error Means

This HRESULT is a COM class-specific error that occurs when a distributed COM (DCOM) object loses its connection to the server process. The object reference is still held by the client but the underlying server is unreachable or has terminated the connection.

## Common Causes

- The remote DCOM server process has crashed or been terminated
- Network connection to the DCOM server was lost
- The DCOM server idle timeout expired and the connection was released
- Firewall or security policy terminated the DCOM session

## How to Fix

### Re-establish the DCOM Connection

```cmd
dcomcnfg
```

Navigate to **Component Services** > **Computers** > **My Computer** > **DCOM Config**, find your application, and verify its configuration.

### Increase DCOM Timeout Settings

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Ole" /v "NetworkAccess" /t REG_DWORD /d 1 /f
reg add "HKLM\SOFTWARE\Microsoft\Ole" /v "EnableDCOM" /t REG_SZ /d "Y" /f
```

### Implement Connection Recovery

```cpp
// Reconnect on CO_E_OBJISCONNECTED
hr = pObject->SomeMethod();
if (hr == CO_E_OBJISCONNECTED) {
    // Release stale reference
    pObject->Release();
    // Re-create the object
    hr = CoCreateInstance(CLSID_MyObject, NULL, CLSCTX_ALL, IID_IMyObject, (void**)&pObject);
}
```

### Configure DCOM Security Permissions

```cmd
dcomcnfg > My Computer > Properties > COM Security > Edit Limits
```

## Related Errors

- [E_FAIL (0x80004005)]({{< relref "/os/windows/hresult-e-fail" >}}) — General failure, may occur when connection recovery fails
- [E_NOINTERFACE (0x80004002)]({{< relref "/os/windows/hresult-e-no-interface" >}}) — No interface, object may be in degraded state
- [REGDB_E_CLASSNOTREG (0x80040154)]({{< relref "/os/windows/hresult-regdb-e-class" >}}) — Class not registered, re-registration needed
