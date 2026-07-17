---
title: "[Solution] PowerShell Get-History Error"
description: "Fix PowerShell Get-History errors when command history is empty, inaccessible, or history persistence fails."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PowerShell Get-History Error Fix

History errors occur when `Get-History` returns empty results, fails to persist between sessions, or `Invoke-History` cannot re-execute a command.

## What This Error Means

PowerShell maintains command history per session. History can be extended to persist across sessions using PSReadLine module. Errors indicate module or configuration issues.

## Common Causes

- PSReadLine module not installed or loaded
- History file path not writable
- History size limit exceeded
- Session is non-interactive (no history)
- History provider not registered

## How to Fix

### 1. Check command history

```powershell
# View current session history
Get-History

# If empty, ensure you're in an interactive session
```

### 2. Install PSReadLine for persistent history

```powershell
# Install PSReadLine
Install-Module -Name PSReadLine -Force

# Enable persistent history in profile
Add-Content $PROFILE "Import-Module PSReadLine"
```

### 3. Configure history settings

```powershell
# Set history size
Set-PSReadLineOption -HistoryHistorySize 10000

# Set history save path
Set-PSReadLineOption -HistorySavePath "C:\Users\User\ps_history.txt"
```

### 4. Invoke historical command

```powershell
# Re-execute command by ID
Invoke-History 5

# Search history
Get-History | Where-Object { $_.CommandLine -like "*Get-Process*" }
```

## Related Errors

- [Transcription Error](powershell-transcription-error) — session logging
- [Profile Error](powershell-profile-error) — profile configuration
- [CommandNotFound](powershell-command-not-found) — command issues
