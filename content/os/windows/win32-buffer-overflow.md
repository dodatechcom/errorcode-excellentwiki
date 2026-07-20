---
title: "[Solution] Error 111 — BUFFER_OVERFLOW Fix"
description: "Fix Windows Error Code (BUFFER_OVERFLOW) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 111
---

# [Solution] Error 111 — BUFFER_OVERFLOW Fix

Win32 error 111 (`ERROR_BUFFER_OVERFLOW`) occurs when the file name is too long. Windows enforces path length limits that can cause this error during file operations with deeply nested directories or long file names.

## Description

The BUFFER_OVERFLOW error (also known as `ERROR_FILENAME_EXCED_RANGE`) is returned when a file name or path exceeds the maximum allowed length. By default, Windows limits paths to 260 characters (`MAX_PATH`). Long file names and deeply nested folder structures can easily exceed this limit, particularly in development environments and network shares. The error code is `ERROR_BUFFER_OVERFLOW` (value 111). The full message reads:

> "The file name is too long."

## Common Causes

1. The full file path exceeds 260 characters (`MAX_PATH` limit).
2. Deeply nested directory structures consume the path length budget.
3. The file name itself is very long (close to the 255-character limit).
4. Network paths (`\\server\share`) add extra characters to the path.
5. Backup copies and temp files create additional path depth.
6. Long paths are not enabled in the Windows registry.

## Solutions

### Solution 1: Shorten the File Name

Rename files or folders to reduce path length:

```powershell
# Rename a long file name
Rename-Item "C:\Very\Long\Path\To\A\Very\Long\Filename.txt" "short.txt"
```

### Solution 2: Use UNC Paths with \\\\?\ Prefix

The `\\?\` prefix bypasses the 260-character limit for local paths:

```cmd
dir "\\?\C:\Very\Long\Path\That\Exceeds\260\Characters\file.txt"
```

```powershell
# PowerShell with long path support
Get-ChildItem -Path "\\?\C:\Very\Long\Path" -Recurse
```

### Solution 3: Enable Long Paths in Windows Registry

Enable the `LongPathsEnabled` setting for Windows 10 (version 1607+) and Windows 11:

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem]
"LongPathsEnabled"=dword:00000001
```

Apply the change:

```cmd
reg import enable_long_paths.reg
```

### Solution 4: Use the Group Policy Setting

Enable Win32 long paths via Group Policy:

```powershell
# Enable via Group Policy (Windows 10 1607+)
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1
```

### Solution 5: Use robocopy with Long Path Support

`robocopy` supports long paths natively:

```cmd
robocopy "C:\Source\Long\Path" "C:\Dest" /E /R:1 /W:1
```

## Related Errors

- [Error 3 — PATH_NOT_FOUND]({{< relref "/os/windows/win32-path-not-found" >}}) — The system cannot find the path
- [Error 2 — FILE_NOT_FOUND]({{< relref "/os/windows/win32-file-not-found" >}}) — The system cannot find the file
- [Error 122 — INSUFFICIENT_BUFFER]({{< relref "/os/windows/win32-insufficient-buffer-error" >}}) — Data area passed to a system call is too small
