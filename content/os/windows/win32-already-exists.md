---
title: "ERROR_ALREADY_EXISTS (183) - How to Fix"
description: "Fix Windows ERROR_ALREADY_EXISTS (183). Resolve duplicate file, directory, and object creation errors on Windows 10 and 11."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# ERROR_ALREADY_EXISTS (Win32 Error 183)

This Win32 API error occurs when trying to create a file, directory, or object that already exists. The error code is `ERROR_ALREADY_EXISTS` (value 183). The full message reads:

> "Cannot create a file when that file already exists."

This commonly appears during file operations, directory creation, named pipe connections, and mutex creation.

## Common Causes

- **File already exists** — Attempting to create a file that's already there.
- **Directory already exists** — Creating a folder with existing name.
- **Named object conflict** — Mutex, semaphore, or named pipe already created.
- **Case-insensitive collision** — Windows is case-insensitive; `File.txt` and `file.txt` conflict.

## How to Fix

### Check if File/Directory Exists First

```powershell
$path = "C:\Path\To\NewItem"
if (Test-Path $path) {
    Write-Host "Item already exists"
} else {
    New-Item -ItemType Directory -Path $path
}
```

### Use -Force to Overwrite

```powershell
New-Item -ItemType Directory -Path "C:\Path\To\Dir" -Force
Copy-Item -Path "source.txt" -Destination "dest.txt" -Force
```

### Rename Existing File Before Creating New One

```powershell
$existing = "C:\Path\To\file.txt"
if (Test-Path $existing) {
    $backup = "$existing.$(Get-Date -Format 'yyyyMMddHHmmss').bak"
    Rename-Item $existing $backup
}
New-Item -ItemType File -Path $existing
```

### Check for Case-Insensitive Collision

```powershell
Get-ChildItem "C:\Path" | Where-Object { $_.Name -ieq "filename.txt" }
```

### Use Unique Names with Timestamp

```powershell
$uniqueName = "file_$(Get-Date -Format 'yyyyMMdd_HHmmss').txt"
New-Item -ItemType File -Path "C:\Path\$uniqueName"
```

### Handle Named Object Conflicts

```powershell
# Check if named mutex already exists
$mutex = New-Object System.Threading.Mutex($false, "Global\MyMutex")
if (-not $mutex.WaitOne(0)) {
    Write-Host "Mutex already held by another process"
}
```

## Related Errors

- [ERROR_FILE_NOT_FOUND (2)]({{< relref "/os/windows/win32-file-not-found" >}}) — File doesn't exist
- [ERROR_DIR_NOT_EMPTY (145)]({{< relref "/os/windows/win32-directory-not-empty" >}}) — Directory exists but not empty
- [ERROR_ACCESS_DENIED (5)]({{< relref "/os/windows/win32-access-denied-win32" >}}) — Permission denied
