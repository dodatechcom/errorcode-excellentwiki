---
title: "[Solution] COM STA Threading Model Error Fix"
description: "Fix COM Single-Threaded Apartment threading errors on Windows. Resolve COM STA marshaling failures and apartment threading conflicts."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] COM STA Threading Model Error Fix

COM STA threading errors occur when a COM object created in an STA thread is accessed from a different thread without proper marshaling. This violates COM threading rules and causes the object to become inaccessible.

## Common Causes
- COM object created in STA being called from MTA thread
- Missing marshaling for cross-apartment COM calls
- Application creating COM objects on the wrong thread type
- STA thread terminated while COM objects are still alive
- CoInitialize called with incompatible threading model

## How to Fix

### Solution 1: Initialize COM Correctly

```c
CoInitialize(NULL);  // STA
// or
CoInitializeEx(NULL, COINIT_MULTITHREADED);  // MTA
```

### Solution 2: Marshal COM Interfaces

Use CoMarshalInterThreadInterfaceInStream and CoGetInterfaceAndReleaseStream to safely pass COM interfaces between threads.

### Solution 3: Use Message Pump for STA

STA threads require a message pump. Ensure the thread hosting STA objects has a running message loop.

### Solution 4: Check Application Settings

Some applications have threading model settings. Check the application configuration for COM threading options.

### Solution 5: Switch to MTA

If possible, configure the application to use multi-threaded apartment model to avoid marshaling overhead.

## Examples
```powershell
Get-WinEvent -FilterHashtable @{LogName='Application'; ProviderName='Application Error'} -MaxEvents 10 | Format-Table TimeCreated, Message -Wrap
```
