---
title: "[Solution] PowerShell Background Job Failed Error Fix"
description: "Fix PowerShell background job failures. Learn why PowerShell jobs fail and how to manage job errors, states, and output retrieval."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A PowerShell job error occurs when a background job started with `Start-Job`, `Start-ThreadJob`, or `Invoke-Command -AsJob` fails during execution. Jobs run in separate runspaces and errors are captured in the job's error stream. The job state changes to `Failed` when the script block throws an unhandled error.

## Why It Happens

- The script block contains an error that is not handled with try/catch
- The job does not have access to the same modules or variables as the parent session
- Memory limits are exceeded in the job's runspace
- The job times out before completing
- The job tries to access resources that require elevation
- Module auto-loading does not work in isolated job sessions
- The job's script block references a variable from the parent session that is not passed

## How to Fix It

### Check job status and retrieve errors

```powershell
# WRONG: Starting job without checking results
Start-Job -ScriptBlock { Get-Process }
# Never retrieves output or errors

# CORRECT: Monitor job state and retrieve errors
$job = Start-Job -ScriptBlock { Get-Process }
$job | Wait-Job
if ($job.State -eq "Failed") {
    $job | Receive-Job  # shows error details
}
$job | Remove-Job
```

### Pass variables and modules to jobs explicitly

```powershell
# WRONG: Job cannot see parent session variables
$apiKey = "secret123"
Start-Job -ScriptBlock { Call-API $apiKey }  # $apiKey is null in job

# CORRECT: Use argument list
$apiKey = "secret123"
Start-Job -ScriptBlock { param($key) Call-API $key } -ArgumentList $apiKey
```

### Import modules inside the job

```powershell
# WRONG: Module not available in job runspace
Start-Job -ScriptBlock { Get-AzVM }  # Az not imported in job

# CORRECT: Import module inside job script block
Start-Job -ScriptBlock {
    Import-Module Az.Compute
    Get-AzVM
}
```

### Handle job timeouts

```powershell
# WRONG: No timeout, job may run indefinitely
$job = Start-Job -ScriptBlock {
    Start-Sleep -Seconds 300
    "Done"
}

# CORRECT: Use Receive-Job with timeout
$job = Start-Job -ScriptBlock {
    Start-Sleep -Seconds 300
    "Done"
}

$result = Receive-Job -Job $job -Wait -AutoRemoveJob -TimeoutSeconds 60
if ($null -eq $result) {
    Stop-Job $job
    Write-Warning "Job timed out"
}
```

### Use thread jobs for lightweight parallelism

```powershell
# WRONG: Start-Job creates a new process (heavyweight)
1..100 | ForEach-Object { Start-Job -ScriptBlock { Process-Item $_ } }

# CORRECT: Use thread jobs for better performance
Install-Module ThreadJob -Scope CurrentUser -Force
1..100 | ForEach-Object {
    Start-ThreadJob -ScriptBlock { Process-Item $_ }
} | Receive-Job -Wait -AutoRemoveJob
```

### Collect all job errors properly

```powershell
# CORRECT: Aggregate errors from multiple jobs
$jobs = 1..5 | ForEach-Object {
    Start-Job -ScriptBlock {
        param($id)
        if ($id -eq 3) { throw "Error on job $id" }
        "Job $id completed"
    } -ArgumentList $_
}

$jobs | Wait-Job | Out-Null

# Check for failures
$failedJobs = $jobs | Where-Object { $_.State -eq "Failed" }
if ($failedJobs) {
    $failedJobs | Receive-Job  # shows all errors
}

$jobs | Remove-Job
```

## Common Mistakes

- Not using `Wait-Job` before `Receive-Job`, causing incomplete output
- Forgetting that jobs run in isolated sessions without access to parent variables
- Not removing completed jobs, causing memory leaks
- Using `Start-Job` for lightweight tasks where `ForEach-Object -Parallel` is more efficient
- Assuming `$Error` from the parent session captures job errors

## Related Pages

- [PowerShell Remote Session Error](ps-remote-session-error) - remoting failed
- [PowerShell Scheduled Task](ps-scheduled-task) - scheduled task failed
- [PowerShell DSC Error](ps-dsc-error) - DSC configuration failed
- [PowerShell Script Block Error](ps-script-block-error) - script block failed
