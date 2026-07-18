---
title: "[Solution] PowerShell Clipboard Access Denied Error Fix"
description: "Fix PowerShell clipboard access errors when Set-Clipboard or Get-Clipboard fails. Learn why clipboard operations fail and workarounds."
languages: ["powershell"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A PowerShell clipboard error occurs when `Set-Clipboard`, `Get-Clipboard`, or `Get-CimInstance Win32_Desktop` fails due to clipboard access restrictions. This commonly happens in remote sessions, non-interactive environments, or when UIPI (User Interface Privilege Isolation) blocks clipboard access between processes running at different privilege levels.

## Why It Happens

- Clipboard operations are not supported in remote PowerShell sessions
- The session is running as a Windows service without a desktop
- UIPI blocks clipboard access between elevated and non-elevated processes
- No active user desktop session is available
- The clipboard is locked by another application
- Running in a Docker container or headless environment
- PowerShell ISE or console window is not the foreground window

## How to Fix It

### Check if clipboard is available

```powershell
# WRONG: Assuming clipboard works in all contexts
Set-Clipboard "test"  # may fail in remote session

# CORRECT: Check if clipboard is accessible
function Test-ClipboardAvailable {
    try {
        [System.Windows.Forms.Clipboard]::SetText("test")
        [System.Windows.Forms.Clipboard]::Clear()
        return $true
    } catch {
        return $false
    }
}

Add-Type -AssemblyName System.Windows.Forms
if (Test-ClipboardAvailable) {
    Set-Clipboard "test"
} else {
    Write-Warning "Clipboard not available in this session"
}
```

### Use alternative output methods in remote sessions

```powershell
# WRONG: Clipboard does not work in remoting
Invoke-Command -ComputerName Server01 -ScriptBlock {
    Get-Process | Set-Clipboard  # fails
}

# CORRECT: Use alternative output methods
Invoke-Command -ComputerName Server01 -ScriptBlock {
    Get-Process | ConvertTo-Csv -NoTypeInformation
} | Set-Clipboard
```

### Handle non-interactive sessions

```powershell
# CORRECT: Check for interactive session before clipboard operations
function SafeSetClipboard {
    param([string]$Text)
    
    if ($host.UI.RawUI -eq $null) {
        Write-Output $Text  # fallback to stdout
    } else {
        Set-Clipboard $Text
    }
}
```

### Use file-based clipboard alternatives

```powershell
# CORRECT: Use temp files as clipboard alternative
$tempFile = [System.IO.Path]::GetTempFileName()
Get-Process | Out-File $tempFile
# Other sessions can read from temp file
$clipContent = Get-Content $tempFile -Raw
Remove-Item $tempFile
```

### Use Windows Forms directly for advanced operations

```powershell
# CORRECT: Direct .NET clipboard access for more control
Add-Type -AssemblyName System.Windows.Forms

# Copy text to clipboard
[System.Windows.Forms.Clipboard]::SetText("Hello from PowerShell")

# Get text from clipboard
$text = [System.Windows.Forms.Clipboard]::GetText()

# Check clipboard contents
if ([System.Windows.Forms.Clipboard]::ContainsText()) {
    $text = [System.Windows.Forms.Clipboard]::GetText()
}
```

## Common Mistakes

- Not adding the `System.Windows.Forms` assembly before using clipboard cmdlets
- Assuming clipboard works in scheduled tasks or background jobs
- Not handling the case where clipboard is locked by another application
- Forgetting that clipboard operations require an active desktop session in some contexts
- Using clipboard for inter-process communication instead of proper IPC mechanisms

## Related Pages

- [PowerShell Unauthorized Access](ps-unauthorized-access-v2) - access denied
- [PowerShell Remote Session Error](ps-remote-session-error) - remoting issues
- [PowerShell Event Log Error](ps-event-log-error) - event log write failed
- [PowerShell Service Error](ps-service-error-v2) - service issues
