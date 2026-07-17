---
title: "COM STA Threading Error - How to Fix"
description: "Fix 'COM STA threading error' on Windows 10 and 11. Resolve Single-Threaded Apartment conflicts, threading model mismatches, and COM concurrency issues."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["com", "sta", "threading", "apartment", "multi-threaded"]
weight: 5
---

# COM STA Threading Error

This error occurs when a COM object that requires a Single-Threaded Apartment (STA) is accessed from a different apartment type or from a multi-threaded context. The error may read:

> "Component threading model does not match client threading model."

or

> "COM STA threading error."

Many COM objects (including Shell objects and Office automation) require STA threading. This error commonly appears in background jobs, PowerShell workflows, and multithreaded applications.

## Common Causes

- **MTA thread accessing STA COM object** — Background threads default to MTA.
- **PowerShell background jobs** — Jobs run in MTA by default.
- **Thread pool usage** — Thread pool threads are MTA.
- **Wrong apartment state** — Application not configured for STA.
- **Cross-apartment COM call** — COM object passed between different apartments.

## How to Fix

### Set STA Thread in PowerShell

```powershell
powershell -STA -Command "your_script.ps1"
```

Or within a script:

```powershell
$currentThread = [System.Threading.Thread]::CurrentThread
$currentThread.SetApartmentState([System.Threading.ApartmentState]::STA)
```

### Create STA Thread Manually

```powershell
$thread = New-Object System.Threading.Thread({
    $null = [System.Runtime.InteropServices.Marshal]::CoInitialize()
    # COM operations here
    [System.Runtime.InteropServices.Marshal]::CoUninitialize()
})
$thread.SetApartmentState([System.Threading.ApartmentState]::STA)
$thread.Start()
$thread.Join()
```

### Configure PowerShell Profile for STA

Check current threading model:

```powershell
$host.Runspace.ThreadOptions
```

Set to STA:

```powershell
$host.Runspace.ThreadOptions = "ReuseThread"
```

### Use STA in Scheduled Tasks

```powershell
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-STA -File C:\Scripts\com_script.ps1"
Register-ScheduledTask -Action $action -TaskName "COM Script" -Trigger (Get-ScheduledTaskTrigger -Daily)
```

### Fix in C# Application

```csharp
[STAThread]
static void Main()
{
    Thread.CurrentThread.SetApartmentState(ApartmentState.STA);
    Application.Run(new MainForm());
}
```

### Use Dispatcher for UI COM Calls

For WPF or WinForms applications:

```csharp
Dispatcher.Invoke(() => {
    // STA COM call here
});
```

## Related Errors

- [COM Not Initialized]({{< relref "/os/windows/com-not-initialized" >}}) — COM library not initialized
- [COM Class Not Registered]({{< relref "/os/windows/com-class-not-registered" >}}) — COM class not found
- [COM Activation Error]({{< relref "/os/windows/com-activation-error" >}}) — COM object creation failure
