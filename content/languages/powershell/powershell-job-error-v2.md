---
title: "[Solution] PowerShell PSJobFailedError Fix"
description: "Fix PowerShell background job failures when Start-Job or Invoke-Command -AsJob fails."
languages: ["powershell"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["job", "Start-Job", "background", "PSJobFailedError", "powershell"]
weight: 5
---

# PowerShell PSJobFailedError Fix

A PowerShell job error occurs when a background job fails to start, complete, or returns an error state.

## What This Error Means

PowerShell jobs run commands in the background. `PSJobFailedError` occurs when a job fails due to script errors, resource limits, connection issues, or improper job handling.

## Common Causes

- Script block has syntax errors
- Job exceeds memory or time limits
- Remote job connection lost
- Not retrieving job output/errors
- Job state not checked before accessing results

## How to Fix

### 1. Check job state before getting results

```powershell
# WRONG: Accessing job without checking state
$job = Start-Job -ScriptBlock { Get-Process }
$results = Receive-Job $job  # May fail

# CORRECT: Wait and check state
$job = Start-Job -ScriptBlock { Get-Process }
$job | Wait-Job -Timeout 30
if ($job.State -eq 'Completed') {
    $results = Receive-Job $job
} else {
    Write-Warning "Job failed: $($job.ChildJobs[0].JobStateInfo.Reason)"
}
```

### 2. Handle job errors properly

```powershell
# CORRECT: Get errors from failed jobs
$job = Start-Job -ScriptBlock {
    throw "Something went wrong"
}
$job | Wait-Job
$job.ChildJobs[0].JobStateInfo.Reason | Format-List
$errors = Receive-Job $job -ErrorAction SilentlyContinue
```

### 3. Limit concurrent jobs

```powershell
# CORRECT: Manage job count
$maxJobs = 5
$jobs = @()

foreach ($item in $items) {
    while (($jobs | Where-Object { $_.State -eq 'Running' }).Count -ge $maxJobs) {
        $jobs | Wait-Job -Any | Out-Null
    }
    $jobs += Start-Job -ScriptBlock { param($i) Process-Item $i } -ArgumentList $item
}
$jobs | Wait-Job
```

### 4. Use proper cleanup

```powershell
# CORRECT: Always clean up jobs
$job = Start-Job -ScriptBlock { Start-Sleep 10 }
try {
    $job | Wait-Job -Timeout 5
} finally {
    $job | Stop-Job -ErrorAction SilentlyContinue
    $job | Remove-Job -Force -ErrorAction SilentlyContinue
}
```

## Related Errors

- [PowerShell Pipeline Error](powershell-pipeline-error-v2) — pipeline failures
- [PowerShell Workflow Error](powershell-workflow-error-v2) — workflow errors
- [PowerShell Remote Error](remote-error) — remote session errors
