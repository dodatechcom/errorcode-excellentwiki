---
title: "[Solution] PowerShell PSJobFailedError — Job Failed"
description: "Fix PowerShell job errors when background jobs fail, return errors, or cannot be started. Handle Start-Job and Receive-Job failures."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PowerShell PSJobFailedError — Job Failed Fix

Job errors occur when `Start-Job` fails to create a job, the job script encounters errors, or `Receive-Job` fails to retrieve results.

## What This Error Means

PowerShell jobs run commands in separate runspaces. Jobs can fail during creation, execution, or result retrieval. The `HasErrors` property on the job indicates failure.

## Common Causes

- Job script contains errors
- Insufficient memory to start new job
- Job exceeds execution time limit
- Module not available in job's runspace
- Remote session disconnected

## How to Fix

### 1. Check job status

```powershell
# List all jobs
Get-Job

# Check specific job for errors
Get-Job -Id 1 | Select-Object State, HasErrors

# Get job errors
Get-Job -Id 1 | Receive-Job -ErrorAction SilentlyContinue
```

### 2. Start job with error handling

```powershell
$job = Start-Job -ScriptBlock {
    try {
        Get-Process | Where-Object { $_.CPU -gt 100 }
    } catch {
        $_ | Out-String
    }
}
$job | Wait-Job
$results = $job | Receive-Job
```

### 3. Import modules in job

```powershell
# WRONG: module not available in job
Start-Job { Get-Module ModuleName }

# RIGHT: import in job script
Start-Job {
    Import-Module ModuleName
    Get-Module ModuleName
}
```

### 4. Clean up failed jobs

```powershell
# Remove all completed/failed jobs
Get-Job | Where-Object { $_.State -in 'Completed','Failed','Stopped' } | Remove-Job
```

## Related Errors

- [PipelineStoppedException](powershell-pipeline-error) — pipeline interruption
- [WorkflowError](powershell-workflow-error) — workflow errors
- [RemoteError](powershell-remote-error) — remote job failures
