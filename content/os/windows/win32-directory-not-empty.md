---
title: "ERROR_DIR_NOT_EMPTY (145) - How to Fix"
description: "Fix Windows ERROR_DIR_NOT_EMPTY (145). Resolve directory not empty errors, force remove directories, and fix folder deletion issues on Windows."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["win32", "error-145", "dir-not-empty", "directory"]
weight: 5
---

# ERROR_DIR_NOT_EMPTY (Win32 Error 145)

This Win32 API error occurs when trying to delete or rename a directory that still contains files or subdirectories. The error code is `ERROR_DIR_NOT_EMPTY` (value 145). The full message reads:

> "The directory is not empty."

This commonly occurs during cleanup operations, application uninstallation, and folder management.

## Common Causes

- **Hidden files in directory** — Directory contains hidden or system files.
- **Files still open** — Application has files locked in the directory.
- **Recycle Bin contents** — Directory is the Recycle Bin with items in it.
- **Protected/system files** — Windows system files prevent deletion.
- **Subdirectory permissions** — Can't list contents of subdirectories.

## How to Fix

### List All Files Including Hidden

```powershell
Get-ChildItem "C:\Path\To\Directory" -Force -Recurse | Select-Object FullName, Attributes
```

### Force Remove Directory Contents

```powershell
Remove-Item "C:\Path\To\Directory" -Recurse -Force
```

### Use Command Prompt for Stubborn Deletion

```cmd
rmdir /s /q "C:\Path\To\Directory"
```

### Check for Locked Files

```powershell
Get-Process | ForEach-Object {
    $proc = $_
    try {
        $proc.Modules | Where-Object { $_.FileName -like "C:\Path\To\Directory\*" }
    } catch {}
} | Where-Object { $_ -ne $null }
```

### Use Handle Tool to Find Locks

```cmd
handle "C:\Path\To\Directory"
```

### Remove Read-Only Attributes

```cmd
attrib -r "C:\Path\To\Directory\*.*" /s
rmdir /s /q "C:\Path\To\Directory"
```

### Delete with Robocopy Empty Directory Trick

```cmd
mkdir C:\EmptyDir
robocopy C:\EmptyDir "C:\Path\To\Directory" /MIR
rmdir /s /q "C:\Path\To\Directory"
rmdir /s /q C:\EmptyDir
```

### Check for Long Path Files

```powershell
Get-ChildItem "C:\Path\To\Directory" -Recurse | Where-Object { $_.FullName.Length -gt 260 } | Select-Object FullName
```

## Related Errors

- [ERROR_FILE_NOT_FOUND (2)]({{< relref "/os/windows/win32-file-not-found" >}}) — Files in directory not found
- [ERROR_ACCESS_DENIED (5)]({{< relref "/os/windows/win32-access-denied-win32" >}}) — Permission denied accessing files
- [ERROR_PATH_NOT_FOUND (3)]({{< relref "/os/windows/win32-path-not-found" >}}) — Path doesn't exist
