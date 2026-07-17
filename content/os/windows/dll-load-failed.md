---
title: "[Solution] DLL Load Failed — Windows Cannot Load the DLL"
description: "Fix 'DLL Load Failed' errors on Windows. Resolve LoadLibrary failures caused by missing dependencies, incorrect paths, or permission issues."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["dll", "load-failed", "loadlibrary", "dependency", "path"]
weight: 5
---

# DLL Load Failed — Windows Cannot Load the DLL

The "DLL Load Failed" error occurs when `LoadLibrary` or `LoadLibraryEx` fails to load a DLL into a process. The error message typically reads:

> "The specified module could not be found."

Or:

> "LoadLibrary failed with error 126: The specified module could not be found."

Or:

> "LoadLibrary failed with error 87: The parameter is incorrect."

## What This Error Means

`LoadLibrary` is the Windows API function that loads DLLs into a process. It can fail for many reasons — the DLL file is missing, one of its dependencies is missing, the DLL path is incorrect, or the process does not have permission to read the file. The specific error code determines which condition triggered the failure.

## Common Causes

- DLL file not found at the expected path
- Dependency DLL of the requested DLL is missing (dependency chain broken)
- DLL path not in the system PATH or application directory
- Insufficient file permissions on the DLL
- DLL requires administrator privileges but running as standard user
- Antivirus blocking DLL load
- DLL is 32-bit but loaded by a 64-bit process

## How to Fix

### Identify the Missing Dependency

```powershell
# Use Dependencies tool (open source)
Dependencies.exe "C:\Path\To\program.exe"

# Or use dumpbin from Visual Studio
dumpbin /dependents "C:\Path\To\file.dll"
```

### Add the DLL Directory to PATH

```powershell
# Add application directory to PATH
$appPath = "C:\Program Files\MyApp"
[Environment]::SetEnvironmentVariable("PATH", "$env:PATH;$appPath", "Machine")
```

### Copy DLL to Application Directory

Copy the required DLL into the same directory as the application's `.exe` file. Windows searches the application directory first.

### Fix File Permissions

```powershell
# Check permissions on the DLL
Get-Acl "C:\Path\To\file.dll" | Format-List

# Grant read access
icacls "C:\Path\To\file.dll" /grant Everyone:F
```

### Reinstall the Visual C++ Redistributable

```powershell
Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x64.exe" -OutFile "$env:TEMP\vc_redist.x64.exe"
Start-Process "$env:TEMP\vc_redist.x64.exe" -ArgumentList "/install /quiet /norestart" -Wait
```

## Related Errors

- [Missing DLL Error]({{< relref "/os/windows/dll-not-found" >}}) — The DLL file itself is missing
- [DLL Dependency Error]({{< relref "/os/windows/dll-dependency-error" >}}) — A required dependency DLL is missing
- [DLL Version Mismatch]({{< relref "/os/windows/dll-version-mismatch" >}}) — Wrong architecture or version of DLL
