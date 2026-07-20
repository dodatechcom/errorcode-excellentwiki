---
title: "[Solution] Terraform State Locked By Another Operation"
description: "Fix Terraform state locked errors when another Terraform process holds the lock."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The state is locked by another process:

```
Error: Error acquiring the state lock

Error message: ConditionalCheckFailedException: Lock ID
"is already held by Terraform process (PID: 12345)
```

## Common Causes

- Another developer running Terraform simultaneously.
- CI/CD pipeline has a running job.
- Previous process crashed without releasing lock.

## How to Fix

**Check if the other process is running:**

```bash
ps aux | grep terraform
```

**Force-unlock if process is dead:**

```bash
terraform force-unlock <LOCK_ID>
```

## Examples

```bash
aws dynamodb scan --table-name terraform-lock
terraform force-unlock abc-123-def-456
```
