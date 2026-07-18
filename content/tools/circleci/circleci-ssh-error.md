---
title: "[Solution] CircleCI SSH into Job Error"
description: "Fix CircleCI ssh into job errors. Learn why this happens and how to resolve it quickly."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# CircleCI SSH into Job Error

CircleCI SSH into job errors occur when trying to SSH into a running job for debugging.

## Why This Happens

- SSH not enabled
- Key not added
- Connection refused
- Job completed

## Common Error Messages

- `ssh_not_enabled_error`
- `ssh_key_error`
- `ssh_connection_error`
- `ssh_job_completed_error`

## How to Fix It

### Solution 1: Enable SSH

Enable SSH in project settings.

### Solution 2: Add SSH key

Add your public SSH key in project settings.

### Solution 3: SSH into job

Use the SSH button in the CircleCI UI when a job is running.


## Common Scenarios

- **SSH not enabled:** Enable SSH in project settings.
- **Connection refused:** Check if the job is still running.

## Prevent It

- Enable SSH for debugging
- Add your SSH key
- Use for troubleshooting
