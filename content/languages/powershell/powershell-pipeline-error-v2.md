---
title: "[Solution] PowerShell PipelineStoppedException Error Fix"
description: "Fix PowerShell pipeline errors when the pipeline is stopped or broken unexpectedly."
languages: ["powershell"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["pipeline", "PipelineStoppedException", "broken-pipeline", "powershell"]
weight: 5
---

# PowerShell PipelineStoppedException Error Fix

A PowerShell pipeline error occurs when the pipeline is stopped by an exception, typically due to a terminating error in a pipeline command.

## What This Error Means

`PipelineStoppedException` is thrown when a pipeline is forcefully stopped, usually because a cmdlet threw a terminating error. This propagates through the pipeline and stops all downstream commands.

## Common Causes

- Terminating error in pipeline command
- Manual pipeline stop via `$host.SetShouldExit()`
- Nested pipeline with unhandled exceptions
- Pipeline broken by Write-Error with -ErrorAction Stop

## How to Fix

### 1. Handle errors in pipeline

```powershell
# CORRECT: Use try-catch in pipeline
try {
    Get-Content "file.txt" -ErrorAction Stop |
        ForEach-Object { $_.ToUpper() } |
        Out-File "output.txt"
} catch [System.IO.FileNotFoundException] {
    Write-Warning "Input file not found"
} catch {
    Write-Warning "Pipeline error: $($_.Exception.Message)"
}
```

### 2. Use -ErrorAction appropriately

```powershell
# CORRECT: Control error propagation
Get-Content "file.txt" -ErrorAction SilentlyContinue |
    Where-Object { $_ -match "pattern" } |
    ForEach-Object { Write-Output $_ }
```

### 3. Break pipeline safely

```powershell
# CORRECT: Check before processing
$results = @()
Get-Content "data.txt" | ForEach-Object {
    if ($_ -eq "STOP") {
        return  # Exit ForEach, don't break pipeline
    }
    $results += $_.ToUpper()
}
```

### 4. Use try-catch for nested pipelines

```powershell
# CORRECT: Wrap complex pipelines
try {
    $data = Get-ChildItem "C:\logs" -Filter "*.log" -ErrorAction Stop
    $data | Sort-Object Length -Descending |
        Select-Object -First 5 |
        ForEach-Object { Write-Host $_.Name }
} catch {
    Write-Warning "Error accessing logs: $($_.Exception.Message)"
}
```

## Related Errors

- [PowerShell Job Error](powershell-job-error-v2) — background job failures
- [PowerShell Workflow Error](powershell-workflow-error-v2) — workflow errors
- [PowerShell Module Load Error](powershell-module-load-error) — module issues
