---
title: "[Solution] Error 33 — LOCK_VIOLATION Fix"
description: "Fix Windows Error Code (LOCK_VIOLATION) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 33
---

# [Solution] Error 33 — LOCK_VIOLATION Fix

Win32 error 33 (`ERROR_LOCK_VIOLATION`) occurs when the process cannot access the file because another process has locked a portion of the file. Unlike a sharing violation, a lock violation is specific to byte-range locks placed on a file region.

## Description

The LOCK_VIOLATION error is returned when a process attempts to access a region of a file that has been locked by another process using `LockFile` or `LockFileEx`. This is common in database engines and multi-process file access scenarios where applications use byte-range locking to coordinate access to shared data files. The error code is `ERROR_LOCK_VIOLATION` (value 33). The full message reads:

> "The process cannot access the file because another process has locked a portion of the file."

## Common Causes

1. A database engine (SQL Server, Access, SQLite) holds a lock on the file.
2. Another application has locked a byte range within the file.
3. A network file share has a client-side lock on the file.
4. The file is open in exclusive mode by another process.
5. Anti-malware software is locking the file during a scan.
6. The application did not properly release a previous lock.

## Solutions

### Solution 1: Close Conflicting Applications

Identify and close the application holding the lock:

```cmd
handle -a "C:\Path\To\file.lock"
```

Kill the locking process if necessary:

```powershell
Stop-Process -Name "ProcessName" -Force
```

### Solution 2: Use Unlocker to Release Locks

Download and use Unlocker or a similar tool to release file locks:

1. Right-click the locked file in Explorer.
2. Select **Unlocker** from the context menu.
3. Choose **Unlock All** and click **OK**.

### Solution 3: Restart the Computer

Restarting clears all byte-range locks held by any process:

```powershell
Restart-Computer -Force
```

### Solution 4: Check for Database Lock Files

Look for associated lock files and remove them if the database is not running:

```powershell
# Find .lock files in a directory
Get-ChildItem "C:\Path\To\Database" -Filter "*.lock" -Recurse
Remove-Item "C:\Path\To\Database\file.lock" -Force
```

### Solution 5: Disable Opportunistic Locking

If opportunistic locking causes the issue, disable it via the registry:

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters]
"EnableOplocks"=dword:00000000
```

Apply the change:

```cmd
reg import disable_oplocks.reg
net stop lanmanserver && net start lanmanserver
```

## Related Errors

- [Error 32 — SHARING_VIOLATION]({{< relref "/os/windows/win32-sharing-violation" >}}) — File is being used by another process
- [Error 5 — ACCESS_DENIED]({{< relref "/os/windows/win32-access-denied-win32" >}}) — Access is denied
- [Error 54 — NETWORK_BUSY]({{< relref "/os/windows/win32-network-busy" >}}) — The network is busy
