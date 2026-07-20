---
title: "[Solution] Terraform State Backup Failed"
description: "Fix Terraform state backup failed errors when creating state backup before modification."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

State backup failures occur when Terraform cannot create a backup:

```
Error: Failed to backup state

Error: AccessDeniedException: User is not authorized to perform:
s3:PutObject
```

## Common Causes

- S3 bucket permissions don't allow writes.
- Bucket policy blocks the backup path.

## How to Fix

**Grant write permissions:**

```json
{
  "Effect": "Allow",
  "Action": ["s3:PutObject", "s3:GetObject"],
  "Resource": "arn:aws:s3:::my-bucket/terraform.tfstate*"
}
```

**Configure backup path:**

```hcl
terraform {
  backend "s3" {
    bucket     = "my-bucket"
    key        = "prod/terraform.tfstate"
    backup_key = "backup/prod/terraform.tfstate"
  }
}
```

## Examples

```bash
terraform state pull > terraform.tfstate.backup
```
