---
title: "[Solution] GitHub Actions Runner Removal Failed Error"
description: "Fix GitHub Actions runner removal failed errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Runner removal failures occur when the runner cannot be cleanly unregistered:

```
Error: Failed to remove runner: Runner is currently executing a job
```

## Common Causes

- Runner is actively executing a job.
- Network issues preventing communication with GitHub API.
- Insufficient permissions to remove the runner.

## How to Fix

**Wait for running jobs to finish:**

```bash
sleep 30
./config.sh remove
```

**Force remove via API:**

```bash
gh api repos/{owner}/{repo}/actions/runners/{RUNNER_ID} -X DELETE
```

## Examples

```bash
# Check if runner is busy
gh api repos/{owner}/{repo}/actions/runners/{RUNNER_ID} | jq '.status'
```
