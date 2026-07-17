---
title: "[Solution] PowerShell PSWorkflowError — Workflow Error"
description: "Fix PowerShell workflow errors when workflows fail to compile, run, or persist. Resolve XAML and workflow engine issues."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PowerShell PSWorkflowError — Workflow Error Fix

Workflow errors occur when PowerShell workflows (defined with `workflow` keyword or XAML) fail to compile, encounter unsupported activities, or have persistence issues.

## What This Error Means

PowerShell workflows are built on Windows Workflow Foundation. They support long-running operations with persistence and retry. Errors indicate compilation, activity, or engine issues.

## Common Causes

- Workflow contains unsupported cmdlets (not all cmdlets are workflow-safe)
- XAML syntax errors in custom activities
- Missing Windows Workflow Foundation
- Persistence database issues
- Nested workflow call depth exceeded

## How to Fix

### 1. Check workflow compatibility

```powershell
# Not all cmdlets work in workflows
# Use workflow-safe alternatives
workflow Test-Workflow {
    # WRONG: Get-Content not workflow-safe
    # Get-Content file.txt

    # RIGHT: use inlineScript for non-workflow-safe cmdlets
    inlineScript { Get-Content file.txt }
}
```

### 2. Verify Workflow Foundation is installed

```powershell
# Check if WF is available
Get-WindowsFeature -Name NET-WCF-HTTP-Activation45
```

### 3. Test workflow compilation

```powershell
# Check workflow syntax
$workflow = Get-Command -Name MyWorkflow
# Review any compilation errors
```

### 4. Use foreach -parallel carefully

```powershell
workflow Process-Items {
    $items = 1..10
    foreach -parallel ($item in $items) {
        InlineScript {
            # Process each item
        }
    }
}
```

## Related Errors

- [PipelineStoppedException](powershell-pipeline-error) — pipeline errors
- [DSC Error](powershell-dsc-error) — DSC configuration errors
- [Job Failed Error](powershell-job-error) — background job errors
