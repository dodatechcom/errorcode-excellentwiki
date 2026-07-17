---
title: "[Solution] PowerShell Set-Clipboard Error"
description: "Fix PowerShell clipboard errors when Set-Clipboard or Get-Clipboard fails, or clipboard operations throw exceptions."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["clipboard", "Set-Clipboard", "Get-Clipboard", "copy", "paste"]
weight: 5
---

# PowerShell Set-Clipboard Error Fix

Clipboard errors occur when `Set-Clipboard` or `Get-Clipboard` fail, usually in non-interactive sessions or when the clipboard is locked by another process.

## What This Error Means

PowerShell clipboard cmdlets use the Windows clipboard API. They fail in non-interactive sessions (scheduled tasks, services) or when the clipboard is in use.

## Common Causes

- Running in non-interactive session (no desktop)
- Another process holding clipboard lock
- Data too large for clipboard
- Clipboard API not available (Server Core)
- Data format not supported by clipboard

## How to Fix

### 1. Check if session supports clipboard

```powershell
# Test clipboard availability
try {
    Get-Clipboard
    Write-Host "Clipboard available"
} catch {
    Write-Host "Clipboard not available"
}
```

### 2. Use alternative for non-interactive sessions

```powershell
# In scheduled tasks or services, use file instead
$data | Out-File -FilePath "C:\temp\output.txt"
# Then read on a desktop session
```

### 3. Set clipboard with specific format

```powershell
# Set as text
"Hello" | Set-Clipboard -Format Text

# Set as HTML
"<b>Hello</b>" | Set-Clipboard -Format Html
```

### 4. Clear clipboard before setting

```powershell
# Clear first to release any locks
Set-Clipboard -Value $null
# Then set new content
"New content" | Set-Clipboard
```

## Related Errors

- [Argument Error](powershell-argument-error) — argument validation
- [InvalidOperation](invalid-operation) — operation errors
- [Type Error](powershell-type-error) — type conversion issues
