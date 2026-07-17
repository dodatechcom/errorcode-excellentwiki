---
title: "ERROR_FILE_NOT_FOUND (2) - How to Fix"
description: "Fix Windows ERROR_FILE_NOT_FOUND (2). Resolve file not found errors, locate missing files, and fix file access issues on Windows 10 and 11."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["win32", "error-2", "file-not-found", "api-error"]
weight: 5
---

# ERROR_FILE_NOT_FOUND (Win32 Error 2)

This Win32 API error occurs when a requested file cannot be located by the system. The error code is `ERROR_FILE_NOT_FOUND` (value 2). The full message reads:

> "The system cannot find the file specified."

This is one of the most common Win32 errors and appears in applications, services, installers, and scripts that reference files that don't exist at the expected path.

## Common Causes

- **File was deleted or moved** — The file no longer exists at the specified path.
- **Typo in file path** — The path contains incorrect characters or separators.
- **File on removable media** — USB drive or external disk is not connected.
- **Symbolic link broken** — Link target no longer exists.
- **Application looking in wrong directory** — Working directory doesn't match expected location.

## How to Fix

### Verify File Exists

```powershell
Test-Path "C:\Path\To\file.exe"
```

### Search for the File

```powershell
Get-ChildItem -Path C:\ -Filter "filename.exe" -Recurse -ErrorAction SilentlyContinue | Select-Object FullName
```

### Check the Working Directory

```powershell
Get-Location
```

### Check File Permissions

```powershell
Get-Acl "C:\Path\To\file.exe" | Format-List
```

### Use Short Path Name

```cmd
for %I in ("C:\Long Path\To\file.exe") do @echo %~sI
```

### Check Event Viewer for Details

```powershell
Get-WinEvent -LogName Application -MaxEvents 20 | Where-Object { $_.Message -like "*file not found*" } | Format-List TimeCreated, Message
```

### Restore Deleted File

```powershell
# Check Recycle Bin
$shell = New-Object -ComObject Shell.Application
$recycleBin = $shell.NameSpace(0xA)
$recycleBin.Items() | Select-Object Name, Path
```

## Related Errors

- [ERROR_PATH_NOT_FOUND (3)]({{< relref "/os/windows/win32-path-not-found" >}}) — Path itself is invalid
- [ERROR_BAD_PATHNAME (161)]({{< relref "/os/windows/win32-bad-pathname" >}}) — Malformed path string
- [DLL Not Found]({{< relref "/os/windows/dll-not-found" >}}) — Missing DLL files
