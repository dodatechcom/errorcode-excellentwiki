---
title: "ERROR_PATH_NOT_FOUND (3) - How to Fix"
description: "Fix Windows ERROR_PATH_NOT_FOUND (3). Resolve invalid path errors, fix directory references, and troubleshoot path issues on Windows 10 and 11."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["win32", "error-3", "path-not-found", "api-error"]
weight: 5
---

# ERROR_PATH_NOT_FOUND (Win32 Error 3)

This Win32 API error occurs when a specified path cannot be found. The error code is `ERROR_PATH_NOT_FOUND` (value 3). The full message reads:

> "The system cannot find the path specified."

Unlike Error 2 (file not found), this error means the directory structure itself doesn't exist. The parent path is invalid or missing.

## Common Causes

- **Directory doesn't exist** — The folder path was never created or was deleted.
- **Network path unavailable** — Mapped network drive or UNC path is disconnected.
- **Invalid characters in path** — Path contains illegal characters.
- **Path too long** — Exceeds the 260-character Windows path limit.
- **Removable media disconnected** — Drive letter no longer valid.

## How to Fix

### Verify Directory Exists

```powershell
Test-Path "C:\Path\To\Directory"
```

### Create Missing Directory

```powershell
New-Item -ItemType Directory -Path "C:\Path\To\Directory" -Force
```

### Check Network Path

```powershell
Test-NetConnection -ComputerName "ServerName" -Port 445
```

### Verify Mapped Drives

```cmd
net use
```

### Check Path Length

```powershell
$path = "C:\Very\Long\Path\To\..."
$path.Length
```

### Use UNC Path Instead of Mapped Drive

```powershell
# Instead of X:\folder
\\ServerName\share\folder
```

### Check for Invalid Characters

```powershell
$invalid = [System.IO.Path]::GetInvalidPathChars()
"path\with*invalid" -match "[$([regex]::Escape($invalid))]"
```

### Enable Long Path Support

```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWord -Force
```

## Related Errors

- [ERROR_FILE_NOT_FOUND (2)]({{< relref "/os/windows/win32-file-not-found" >}}) — File within valid path not found
- [ERROR_BAD_PATHNAME (161)]({{< relref "/os/windows/win32-bad-pathname" >}}) — Invalid path format
- [ERROR_DIR_NOT_EMPTY (145)]({{< relref "/os/windows/win32-directory-not-empty" >}}) — Directory exists but not empty
