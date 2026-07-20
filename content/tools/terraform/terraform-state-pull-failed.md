---
title: "[Solution] Terraform State Pull Failed"
description: "Fix Terraform state pull failed errors when downloading state from the backend."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

State pull failures occur when Terraform cannot retrieve the state:

```
Error: Failed to pull state

Error:NoSuchKey: The specified key does not exist.
```

## Common Causes

- State file doesn't exist (first run).
- Wrong S3 bucket or key configured.

## How to Fix

**Check state file existence:**

```bash
aws s3 ls s3://my-bucket/terraform.tfstate
```

**Initialize fresh state:**

```bash
terraform init -migrate-state
```

## Examples

```bash
aws s3 ls s3://my-bucket/ --recursive | grep tfstate
terraform state pull | jq '.resources | length'
```
