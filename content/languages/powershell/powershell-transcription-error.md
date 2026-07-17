---
title: "[Solution] PowerShell Start-Transcript Error"
description: "Fix Start-Transcript errors in PowerShell when session transcription fails to start, write, or stop properly."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["transcript", "logging", "session", "Start-Transcript", "audit"]
weight: 5
---

# PowerShell Start-Transcript Error Fix

Transcript errors occur when `Start-Transcript` fails to begin recording, `Stop-Transcript` fails, or the transcript file cannot be written.

## What This Error Means

Transcription logs all PowerShell session input and output to a text file. Errors occur due to file permissions, path issues, or transcription already in progress.

## Common Causes

- Output path doesn't exist or is not writable
- Transcription already active in the session
- File locked by another process
- Path contains invalid characters
- Group Policy disables transcription

## How to Fix

### 1. Ensure output path exists

```powershell
# Create the directory if needed
$transcriptPath = "C:\Logs"
if (-not (Test-Path $transcriptPath)) {
    New-Item -ItemType Directory -Path $transcriptPath -Force
}

Start-Transcript -Path "$transcriptPath\session.log"
```

### 2. Check for active transcription

```powershell
# Stop any existing transcript
try { Stop-Transcript } catch {}

# Start fresh
Start-Transcript -Path "C:\Logs\session.log"
```

### 3. Use Append mode

```powershell
# Append to existing transcript
Start-Transcript -Path "C:\Logs\session.log" -Append
```

### 4. Verify transcription works

```powershell
Start-Transcript -Path "C:\test.log"
# Do some work
Stop-Transcript
Get-Content "C:\test.log"
```

## Related Errors

- [History Error](powershell-history-error) — command history issues
- [Profile Error](powershell-profile-error) — profile load errors
- [File Not Found (VBA)](/languages/vba/file-not-found) — file access errors
