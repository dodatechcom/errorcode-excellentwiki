---
title: "COM Not Initialized Error - How to Fix"
description: "Fix 'COM not initialized' errors on Windows 10 and 11. Initialize COM libraries, resolve CoInitialize failures, and fix apartment threading issues."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["com", "not-initialized", "coinitialize", "com-library"]
weight: 5
---

# COM Not Initialized Error

This error occurs when code attempts to use COM services without first initializing the COM library. The error typically reads:

> "CoInitialize has not been called."

or

> "COM has not been initialized."

COM must be initialized before any COM API calls. This error commonly appears in applications, scripts, and services that interact with COM components.

## Common Causes

- **Missing CoInitialize call** — Application didn't call `CoInitializeEx` before using COM.
- **Thread model mismatch** — COM initialized on wrong thread or with wrong apartment model.
- **Multiple initializations** — COM was initialized and then uninitialized prematurely.
- **Script language limitations** — Some scripting environments don't auto-initialize COM.
- **Service hosting** — COM requires explicit initialization in service contexts.

## How to Fix

### Initialize COM in PowerShell

```powershell
$null = [System.Runtime.InteropServices.Marshal]::CoInitialize([System.Runtime.InteropServices.ComTypes.THREADFLAGS]::STA)
```

Or using COM interop:

```powershell
$comShell = New-Object -ComObject Shell.Application
```

### Initialize COM in C# Application

```csharp
[STAThread]
static void Main()
{
    System.Threading.Thread.CurrentThread.SetApartmentState(System.Threading.ApartmentState.STA);
    // COM code here
}
```

### Initialize COM in VBScript

```vbscript
Set objShell = CreateObject("Shell.Application")
```

### Fix Threading Model

Ensure the correct threading model is used:

```powershell
# STA (Single-Threaded Apartment) - required for most COM objects
$null = [System.Runtime.InteropServices.Marshal]::CoInitializeEx(0, [System.Runtime.InteropServices.ComTypes.THREADFLAGS]::STA)
```

### Check COM Initialization Status

```powershell
try {
    $obj = New-Object -ComObject WScript.Shell
    Write-Host "COM initialized successfully"
} catch {
    Write-Host "COM initialization failed: $_"
}
```

### Initialize COM for Background Jobs

```powershell
Start-Job -ScriptBlock {
    $null = [System.Runtime.InteropServices.Marshal]::CoInitialize(0)
    # COM operations here
    [System.Runtime.InteropServices.Marshal]::CoUninitialize()
}
```

## Related Errors

- [COM STA Threading Error]({{< relref "/os/windows/com-sta-error" >}}) — Single-Threaded Apartment issues
- [COM Not Initialized]({{< relref "/os/windows/com-not-initialized" >}}) — General COM initialization failure
- [COM Class Not Registered]({{< relref "/os/windows/com-class-not-registered" >}}) — COM class registration missing
