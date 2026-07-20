---
title: "[Solution] Error 145 — DIR_NOT_EMPTY Fix"
description: "Fix Windows Error Code (DIR_NOT_EMPTY) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 145
---

# [Solution] Error 145 — DIR_NOT_EMPTY Fix

Win32 error 145 (`ERROR_DIR_NOT_EMPTY`) occurs when the directory is not empty. This prevents you from deleting, renaming, or moving a directory that still contains files or subdirectories.

## Description

The DIR_NOT_EMPTY error is returned when an operation targets a directory that still contains files, subdirectories, or hidden/system items. This is common during cleanup operations, application uninstallation, and automated scripts that expect directories to be empty before removal. The error code is `ERROR_DIR_NOT_EMPTY` (value 145). The full message reads:

> "The directory is not empty."

## Common Causes

1. Hidden files or system files are present in the directory.
2. A subdirectory contains files that prevent deletion.
3. An application has files open within the directory.
4. Read-only attributes prevent deletion of contents.
5. The Recycle Bin is located within the directory.
6. Long file paths within the directory prevent proper enumeration.

## Solutions

### Solution 1: Check Directory Contents

List all files including hidden and system files:

```powershell
# List all files including hidden ones
Get-ChildItem "C:\Path\To\Directory" -Force -Recurse | Select-Object FullName, Attributes
```

```cmd
:: List all files including hidden and system
dir "C:\Path\To\Directory" /a /s /b
```

### Solution 2: Delete Files First, Then Remove Directory

Remove all contents before deleting the directory:

```powershell
# Remove all contents recursively
Remove-Item "C:\Path\To\Directory\*" -Recurse -Force
# Now remove the empty directory
Remove-Item "C:\Path\To\Directory" -Force
```

### Solution 3: Use rd /s to Recursively Delete

Use the `rd` command with `/s` flag to remove the directory and all contents:

```cmd
rd /s /q "C:\Path\To\Directory"
```

### Solution 4: Remove Read-Only Attributes

Strip read-only attributes before deletion:

```cmd
attrib -r "C:\Path\To\Directory\*.*" /s
rd /s /q "C:\Path\To\Directory"
```

### Solution 5: Use robocopy Empty Directory Trick

Use robocopy to mirror an empty directory over the target:

```cmd
mkdir C:\EmptyDir
robocopy C:\EmptyDir "C:\Path\To\Directory" /MIR
rmdir /s /q "C:\Path\To\Directory"
rmdir /s /q C:\EmptyDir
```

## Related Errors

- [Error 32 — SHARING_VIOLATION]({{< relref "/os/windows/win32-sharing-violation" >}}) — File is being used by another process
- [Error 5 — ACCESS_DENIED]({{< relref "/os/windows/win32-access-denied-win32" >}}) — Access is denied
- [Error 3 — PATH_NOT_FOUND]({{< relref "/os/windows/win32-path-not-found" >}}) — The system cannot find the path
