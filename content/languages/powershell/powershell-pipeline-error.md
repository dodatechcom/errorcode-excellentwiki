---
title: "[Solution] PowerShell PipelineStoppedException"
description: "Fix PowerShell PipelineStoppedException when a pipeline is forcibly stopped by a terminating error or cancellation."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["pipeline", "PipelineStoppedException", "terminating-error", "stop"]
weight: 5
---

# PowerShell PipelineStoppedException Fix

PipelineStoppedException occurs when a pipeline is interrupted by a terminating error, `throw` statement, or Ctrl+C cancellation. It propagates through the pipeline and may mask the original error.

## What This Error Means

PowerShell pipelines process data through a chain of cmdlets. When one cmdlet throws a terminating error, the pipeline stops and all pending operations are cancelled.

## Common Causes

- Terminating error in a pipeline cmdlet
- `$ErrorActionPreference = "Stop"` converting errors to terminating
- Explicit `throw` in pipeline code
- User pressed Ctrl+C during pipeline execution
- Pipeline timeout

## How to Fix

### 1. Catch terminating errors in pipeline

```powershell
# Use try/catch around pipeline
try {
    Get-Content file.txt | ForEach-Object {
        # Process that might throw
        $_ | ConvertFrom-Json
    }
} catch [PipelineStoppedException] {
    Write-Warning "Pipeline was stopped"
} catch {
    Write-Warning "Error: $_"
}
```

### 2. Use -ErrorAction for non-terminating errors

```powershell
# Continue on errors
Get-Content file.txt -ErrorAction SilentlyContinue

# Or warn and continue
Get-Content file.txt -ErrorAction Continue
```

### 3. Avoid $ErrorActionPreference = "Stop" in pipelines

```powershell
# This makes ALL errors terminating
$ErrorActionPreference = "Stop"

# Use per-cmdlet error action instead
Get-Content file.txt -ErrorAction Stop
```

### 4. Use break to stop pipeline intentionally

```powershell
# Break exits the current scope
1..100 | ForEach-Object {
    if ($_ -eq 50) { break }
    $_
}
```

## Related Errors

- [InvalidOperation](invalid-operation) — operation errors
- [ParameterBindingException](powershell-parameter-binding) — parameter issues
- [Job Failed Error](powershell-job-error) — background job errors
