---
title: "[Solution] Control-C Interrupt Handler Error"
description: "Fix Control-C (Ctrl+C) interrupt handler errors on Windows. Resolve console control handler issues and signal processing failures."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Control-C Interrupt Handler Error

A Control-C interrupt handler error occurs when a console application fails to handle the `CTRL_C_EVENT` signal properly, or when the default handler terminates the process unexpectedly. The crash may show:

> "Unhandled exception: control-C"

Or the application terminates without any error message when `Ctrl+C` is pressed.

## What This Error Means

When the user presses `Ctrl+C` in a Windows console, the system sends a `CTRL_C_EVENT` to all processes attached to that console. By default, this terminates the process. Applications can register a custom console control handler with `SetConsoleCtrlHandler` to catch the signal and perform cleanup. If the handler itself crashes or the application does not install a handler, the process is terminated abruptly.

## Common Causes

- Application does not register a `SetConsoleCtrlHandler` callback
- The control handler crashes (e.g., accesses freed memory)
- Console application running in a non-interactive session (service, scheduled task)
- Pipeline or batch script processing interrupted mid-operation
- `Ctrl+C` in PowerShell triggers `PipelineStoppedException`

## How to Fix

### Register a Console Control Handler (for Developers)

```c
#include <windows.h>
#include <stdio.h>

BOOL WINAPI ConsoleHandler(DWORD dwCtrlType) {
    switch (dwCtrlType) {
        case CTRL_C_EVENT:
            printf("CTRL+C received. Cleaning up...\n");
            // Perform cleanup here
            return TRUE;
        case CTRL_BREAK_EVENT:
            printf("CTRL+BREAK received.\n");
            return TRUE;
        case CTRL_CLOSE_EVENT:
            printf("Console closing.\n");
            return TRUE;
        default:
            return FALSE;
    }
}

int main() {
    SetConsoleCtrlHandler(ConsoleHandler, TRUE);
    // ... application logic
    return 0;
}
```

### Use /B Flag in CMD to Ignore Ctrl+C

```cmd
:: Run a batch script ignoring Ctrl+C
cmd /C "myapp.exe"
:: Or within a batch file:
:: Press Ctrl+C twice to force termination
```

### Handle Interrupt in PowerShell Scripts

```powershell
try {
    # Long-running operation
    Get-Process | ForEach-Object { Start-Sleep -Seconds 1 }
} catch [System.Management.Automation.PipelineStoppedException] {
    Write-Host "Operation was interrupted by the user."
    # Cleanup code
}
```

### Ignore Ctrl+C in Python/Node.js

```python
# Python - ignore Ctrl+C
import signal
signal.signal(signal.SIGINT, signal.SIG_IGN)
```

```javascript
// Node.js - catch Ctrl+C
process.on('SIGINT', () => {
    console.log('Received SIGINT. Cleaning up...');
    process.exit(0);
});
```

### Check for Service Context

Services cannot receive `Ctrl+C`. If your application is running as a service and you need to stop it:

```powershell
# Stop a service gracefully
net stop ServiceName

# Or via PowerShell
Stop-Service -Name "ServiceName"
```

## Related Errors

- [Unhandled Exception]({{< relref "/os/windows/runtime-error-unhandled-exception" >}}) — Unhandled exceptions at crash address
- [General Protection Fault]({{< relref "/os/windows/runtime-error-gpf" >}}) — General protection fault terminations
- [Application Error Event 1000]({{< relref "/os/windows/event-1000" >}}) — Event log entries for application crashes
