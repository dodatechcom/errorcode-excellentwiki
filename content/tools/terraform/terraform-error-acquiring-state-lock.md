---
title: "[Solution] Terraform Error Acquiring State Lock"
description: "Fix Terraform error acquiring state lock when the state file is locked by another operation."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

State lock acquisition failures prevent Terraform from modifying state:

```
Error: Error acquiring the state lock

Error message: ConditionalCheckFailedException: The conditional
request failed Lock Info: ID: abc-123
```

## Common Causes

- Another Terraform process is running.
- Previous process crashed without releasing the lock.
- DynamoDB lock entry is stale.

## How to Fix

**Force-unlock:**

```bash
terraform force-unlock abc-123
```

**Manually delete the lock entry:**

```bash
aws dynamodb delete-item   --table-name terraform-lock   --key '{"LockID": {"S": "my-bucket/terraform.tfstate"}}'
```

## Examples

```bash
aws dynamodb scan --table-name terraform-lock
terraform force-unlock <LOCK_ID>
```
