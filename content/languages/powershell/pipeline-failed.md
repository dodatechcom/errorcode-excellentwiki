---
title: "[Solution] PowerShell PipelineStoppedException Fix"
description: "Fix 'PipelineStoppedException' when a PowerShell pipeline is forcibly terminated."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PowerShell PipelineStoppedException Fix

This error occurs when a running pipeline is stopped before all commands have completed. The error message reads: `PipelineStoppedException: The pipeline has been stopped.`

## Description

PowerShell pipelines stream data between commands. If an upstream command fails, is interrupted by the user, or throws a terminating error, the entire pipeline is stopped. Downstream commands receive this exception when they attempt to read from the pipeline after it has been halted.

## Common Causes

- **Terminating error in pipeline** — a cmdlet in the pipeline threw a terminating error, stopping all downstream commands.
- **User pressed Ctrl+C** — interrupting a running pipeline triggers this exception in all pipeline components.
- **Upstream command returned nothing** — when combined with `-ErrorAction Stop`, empty output can stop the pipeline.
- **Background job cancellation** — a running job was stopped externally while the pipeline was still processing.

## How to Fix

### Fix 1: Use try/catch to handle pipeline stops

```powershell
# Wrap pipeline operations that might be interrupted
try {
    Get-Content "largefile.log" |
        ForEach-Object {
            # Process each line
            $_.ToUpper()
        } |
        Out-File "output.txt"
} catch [System.Management.Automation.PipelineStoppedException] {
    Write-Warning "Pipeline was interrupted — partial results may exist"
}
```

### Fix 2: Use -ErrorAction appropriately

```powershell
# Use Continue to keep pipeline running on errors
Get-Content "mixedfile.log" |
    ForEach-Object {
        # This won't stop the pipeline on non-terminating errors
        $_ / 1  # Some lines may cause errors
    } -ErrorAction Continue

# Use SilentlyContinue to suppress errors
Get-ChildItem "C:\*" -Recurse -ErrorAction SilentlyContinue
```

### Fix 3: Avoid -ErrorAction Stop in pipelines unless intentional

```powershell
# Wrong — this will stop the entire pipeline on first error
Get-ChildItem "C:\*" -Recurse -ErrorAction Stop |
    ForEach-Object { $_.FullName }

# Correct — let the pipeline continue past errors
Get-ChildItem "C:\*" -Recurse -ErrorAction SilentlyContinue |
    ForEach-Object { $_.FullName }
```

### Fix 4: Use -PipelineVariable to inspect intermediate results

```powershell
# Debug pipeline issues by capturing intermediate results
Get-ChildItem "C:\Temp" -PipelineVariable file |
    Where-Object { $_.Length -gt 1MB } -PipelineVariable large |
    ForEach-Object {
        Write-Debug "Processing $($file.Name) — size $($file.Length)"
        $_.FullName
    }
```

## Examples

```powershell
PS> 1..100 | ForEach-Object { if ($_ -eq 5) { throw "error" }; $_ }
PipelineStoppedException: The pipeline has been stopped.

PS> Get-Content "file.txt" | Select-Object -First 5
# User presses Ctrl+C during execution
PipelineStoppedException: The pipeline has been stopped.
```

## Related Errors

- [InvalidOperation](invalid-operation.md) — operation not valid on current state.
- [ScriptSyntaxException](script-syntax.md) — syntax error in pipeline script block.
- [PSRemotingError](remote-error.md) — pipeline failure in remote sessions.
