---
title: "[Solution] PowerShell PSWorkflowError Fix"
description: "Fix PowerShell workflow activity errors when workflows fail due to activity or runtime issues."
languages: ["powershell"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["workflow", "PSWorkflowError", "activity", "powershell"]
weight: 5
---

# PowerShell PSWorkflowError Fix

A PowerShell workflow error occurs when a workflow activity fails, a parallel activity has issues, or the workflow runtime encounters a problem.

## What This Error Means

PowerShell workflows use Windows Workflow Foundation. `PSWorkflowError` occurs when activities within a workflow fail, when persistence points have issues, or when workflow sessions are interrupted.

## Common Causes

- Workflow activity throws a terminating error
- Workflow persistence file locked or missing
- Parallel activity has unhandled exceptions
- Workflow host session interrupted
- Long-running activity without checkpoint

## How to Fix

### 1. Add checkpoints for long workflows

```powershell
# CORRECT: Use checkpoint to enable recovery
workflow Test-Workflow {
    # Checkpoint every major step
    Checkpoint-Workflow
    $step1 = Do-Step1
    Checkpoint-Workflow
    $step2 = Do-Step2 $step1
    Checkpoint-Workflow
    return $step2
}
```

### 2. Handle activity errors in workflow

```powershell
# CORRECT: Use inlineScript with error handling
workflow Invoke-SafeWorkflow {
    inlineScript {
        try {
            Get-Service -Name "NonExistent" -ErrorAction Stop
        } catch {
            Write-Warning "Service not found: $($_.Exception.Message)"
        }
    }
}
```

### 3. Clean up persistence files

```powershell
# CORRECT: Clear stale persistence
$persistencePath = "$env:LOCALAPPDATA\Microsoft\Windows\PowerShell\Workflow\Serialization"
if (Test-Path $persistencePath) {
    Remove-Item "$persistencePath\*" -Force -ErrorAction SilentlyContinue
}
```

### 4. Use workflow parameters properly

```powershell
# CORRECT: Define parameters correctly
workflow Start-ProcessWorkflow {
    param(
        [Parameter(Mandatory)]
        [string]$ComputerName
    )

    foreach -parallel ($computer in $ComputerName) {
        inlineScript {
            Test-Connection -ComputerName $using:computer -Count 1
        }
    }
}
```

## Related Errors

- [PowerShell Pipeline Error](powershell-pipeline-error-v2) — pipeline failures
- [PowerShell Job Error](powershell-job-error-v2) — background job failures
- [PowerShell DSC Error](powershell-dsc-error-v2) — DSC configuration errors
