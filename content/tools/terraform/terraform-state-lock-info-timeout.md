---
title: "[Solution] Terraform State Lock Info Timeout"
description: "Fix Terraform state lock info timeout errors when the lock service is unreachable."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Lock info timeout errors occur when Terraform cannot retrieve lock info:

```
Error: Error acquiring the state lock

timeout while waiting for state lock to become 'not held'
```

## Common Causes

- Backend service (DynamoDB, GCS) is unreachable.
- Network latency or timeout.

## How to Fix

**Check backend connectivity:**

```bash
aws dynamodb describe-table --table-name terraform-lock
```

**Force-unlock:**

```bash
terraform force-unlock <LOCK_ID>
```

**Increase timeout:**

```bash
terraform plan -lock-timeout=300s
```

## Examples

```bash
aws dynamodb scan --table-name terraform-lock --limit 5
```
