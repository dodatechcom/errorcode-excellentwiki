---
title: "Registry Hive Error - How to Fix"
description: "Fix 'Registry hive error' on Windows 10 and 11. Repair corrupt registry hive files (SYSTEM, SOFTWARE, DEFAULT) and restore system functionality."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Registry Hive Error

This error occurs when a specific registry hive file is corrupted or unreadable. Windows stores the registry as several hive files:

- `SYSTEM` — Hardware and system configuration
- `SOFTWARE` — Installed software settings
- `DEFAULT` — Default user profile
- `NTUSER.DAT` — Per-user settings
- `SAM` — Security Account Manager
- `SECURITY` — Security policies

A corrupted hive can prevent Windows from booting or cause specific services to fail.

## Common Causes

- **Sudden power loss** — Hive file was being written when power was cut.
- **Disk failure** — Physical disk error damaged hive files.
- **Failed update or installation** — Incomplete write operation corrupted the hive.
- **Malware** — Malicious software targeted specific hives.
- **Memory failure** — RAM errors corrupted data during write operations.

## How to Fix

### Identify the Corrupted Hive

Check Event Viewer for hive-related errors:

```powershell
Get-WinEvent -LogName System -MaxEvents 100 | Where-Object { $_.Message -like "*registry*" -or $_.Message -like "*hive*" } | Select-Object TimeCreated, Message | Format-List
```

### Replace Corrupted Hive from RegBack

```cmd
xcopy /y "C:\Windows\System32\config\RegBack\SYSTEM" "C:\Windows\System32\config\SYSTEM"
xcopy /y "C:\Windows\System32\config\RegBack\SOFTWARE" "C:\Windows\System32\config\SOFTWARE"
```

### Repair from Windows Recovery Environment

1. Boot from Windows installation media or recovery drive.
2. Open **Command Prompt**.
3. Load the corrupted hive for repair:

```cmd
reg load HKLM\BROKEN D:\Windows\System32\config\SOFTWARE
reg query HKLM\BROKEN
reg unload HKLM\BROKEN
```

### Check Disk Integrity

```cmd
chkdsk C: /f /r /x
```

### Run Memory Diagnostic

```powershell
mdsched.exe
```

Select **Restart now and check for problems**.

### Use Last Known Good Configuration

1. Restart and press **F8** repeatedly.
2. Select **Last Known Good Configuration (Advanced)**.

## Related Errors

- [Registry Corrupted]({{< relref "/os/windows/reg-corrupted" >}}) — General registry corruption
- [Registry Restore Error]({{< relref "/os/windows/reg-restore-error" >}}) — Failure restoring from backup
- [Registry Transaction Error]({{< relref "/os/windows/reg-transaction-error" >}}) — Transactional write failures
