---
title: "[Solution] PowerShell Event Log Write Failed Error Fix"
description: "Fix PowerShell event log write errors when Write-EventLog fails. Learn why event log operations fail and how to handle logging correctly."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A PowerShell event log error occurs when `Write-EventLog` or `Get-WinEvent` fails to interact with the Windows Event Log. This can happen when writing to a log source that does not exist, reading logs without permissions, or the event log service is not available.

## Why It Happens

- The event log source has not been registered before writing
- Insufficient permissions to read or write event logs
- The event log is full or corrupted
- The event log service is not running
- Attempting to write to a log that does not exist
- The log name is invalid or misspelled
- Running in a container or restricted environment without event log access

## How to Fix It

### Register the event source before writing

```powershell
# WRONG: Writing to unregistered source
Write-EventLog -LogName Application -Source "MyApp" -EventId 1 -Message "Test"

# CORRECT: Register the source first (requires admin)
if (-not [System.Diagnostics.EventLog]::SourceExists("MyApp")) {
    New-EventLog -LogName Application -Source "MyApp"
}
Write-EventLog -LogName Application -Source "MyApp" -EventId 1 -Message "Test"
```

### Use try/catch for event log operations

```powershell
# WRONG: No error handling
Write-EventLog -LogName Application -Source "MyApp" -EventId 1 -Message "Test"

# CORRECT: Handle event log errors
try {
    Write-EventLog -LogName Application -Source "MyApp" -EventId 1 -Message "Test" -ErrorAction Stop
} catch [System.Diagnostics.EventLogException] {
    Write-Warning "Event log write failed: $($_.Exception.Message)"
    # Fallback to file logging
    "[$(Get-Date)] Event log write failed" | Out-File "C:\Logs\fallback.log" -Append
}
```

### Check event log permissions

```powershell
# CORRECT: Verify event log access
$logNames = @("Application", "System", "Security")
foreach ($log in $logNames) {
    try {
        Get-EventLog -LogName $log -Newest 1 -ErrorAction Stop | Out-Null
        Write-Host "Can read: $log"
    } catch {
        Write-Host "Cannot read: $log - $($_.Exception.Message)"
    }
}
```

### Clear full event logs

```powershell
# CORRECT: Clear event log when full (requires admin)
Clear-EventLog -LogName Application
# Or archive first
wevtutil epl Application "C:\Logs\Application.evtx"
Clear-EventLog -LogName Application
```

### Use structured event logging

```powershell
# CORRECT: Use Write-EventLog with proper parameters
function Write-AppLog {
    param(
        [string]$Message,
        [System.Diagnostics.EventLogEntryType]$EntryType = "Information",
        [int]$EventId = 1000
    )
    
    $source = "MyPowerShellApp"
    if (-not [System.Diagnostics.EventLog]::SourceExists($source)) {
        New-EventLog -LogName Application -Source $source -ErrorAction SilentlyContinue
    }
    
    Write-EventLog -LogName Application -Source $source `
        -EventId $EventId -EntryType $EntryType -Message $Message
}

Write-AppLog "Script started" -EventId 1001
```

## Common Mistakes

- Not registering the event source before the first write attempt
- Forgetting that event log operations require administrator privileges
- Using generic event IDs that overlap with system event IDs
- Not clearing event logs regularly, causing them to fill up
- Assuming event log entries are immediately available for reading

## Related Pages

- [PowerShell Unauthorized Access](ps-unauthorized-access-v2) - access denied
- [PowerShell Service Error](ps-service-error-v2) - service issues
- [PowerShell Transcription Error](ps-transcription-error) - logging failed
- [PowerShell WMI Error](ps-wmi-error) - WMI query failed
