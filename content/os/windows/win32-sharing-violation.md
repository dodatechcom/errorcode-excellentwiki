---
title: "[Solution] Error 32 — SHARING_VIOLATION Fix"
description: "Fix Windows Error Code (SHARING_VIOLATION) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 32
---

# [Solution] Error 32 — SHARING_VIOLATION Fix

Win32 error 32 (`ERROR_SHARING_VIOLATION`) occurs when the process cannot access the file because it is being used by another process. This is one of the most common file-locking errors on Windows, frequently encountered during file copy, move, or delete operations.

## Description

The SHARING_VIOLATION error is returned by the Windows API when a process attempts to open, read, write, or delete a file that has already been opened by another process in a mode that prevents sharing. Windows file locking prevents concurrent modifications to protect data integrity, but it often causes unexpected failures in scripts, installers, and automated tasks. The error code is `ERROR_SHARING_VIOLATION` (value 32). The full message reads:

> "The process cannot access the file because it is being used by another process."

## Common Causes

1. Another application has the target file open for reading or writing.
2. An antivirus scanner is scanning the file at the time of access.
3. Windows Explorer has a preview or thumbnail lock on the file.
4. A previous instance of the same program left the file handle open.
5. A backup or indexing service (Windows Search) is accessing the file.
6. The file is locked by a file system filter driver.

## Solutions

### Solution 1: Close Conflicting Programs

Identify which process has the file open and close it.

```powershell
# Find processes using a specific file
Get-Process | ForEach-Object {
    $proc = $_
    try {
        $proc.Modules | Where-Object { $_.FileName -eq "C:\Path\To\file.txt" }
    } catch {}
}
```

Alternatively, use the Sysinternals Handle tool:

```cmd
handle "C:\Path\To\file.txt"
```

### Solution 2: Use Resource Monitor

Open Resource Monitor to find and release file locks:

```powershell
# Launch Resource Monitor
resmon.exe
```

1. Open the **CPU** tab.
2. Under **Associated Handles**, search for the locked file name.
3. Right-click the locking process and select **End Process**.

### Solution 3: Restart the Computer

If the file lock cannot be released manually, restarting the computer will close all open file handles:

```powershell
# Restart the computer
Restart-Computer -Force
```

### Solution 4: Retry with a Short Delay

Sometimes the file is released momentarily. Add a retry loop:

```powershell
$maxRetries = 5
for ($i = 0; $i -lt $maxRetries; $i++) {
    try {
        Move-Item "C:\Path\To\file.txt" "C:\Dest\file.txt" -Force
        Write-Host "File moved successfully."
        break
    } catch {
        Write-Host "Attempt $($i + 1) failed. Retrying in 2 seconds..."
        Start-Sleep -Seconds 2
    }
}
```

### Solution 5: Use robocopy to Bypass Locks

`robocopy` can copy files that other tools fail on due to sharing violations:

```cmd
robocopy "C:\Source" "C:\Dest" "file.txt" /R:3 /W:5
```

## Related Errors

- [Error 33 — LOCK_VIOLATION]({{< relref "/os/windows/win32-lock-violation" >}}) — Another process has locked a portion of the file
- [Error 5 — ACCESS_DENIED]({{< relref "/os/windows/win32-access-denied-win32" >}}) — Access is denied
- [Error 33 — NETWORK_BUSY]({{< relref "/os/windows/win32-network-busy" >}}) — The network is busy
