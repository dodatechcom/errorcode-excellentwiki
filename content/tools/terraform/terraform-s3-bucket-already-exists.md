---
title: "[Solution] Terraform S3 Bucket Already Exists"
description: "Fix Terraform S3 bucket already exists errors when the bucket name is taken globally."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

S3 bucket already exists errors occur when the bucket name is not globally unique:

```
Error: error creating S3 Bucket: BucketAlreadyExists

The requested bucket name is not available.
```

## Common Causes

- Bucket name already taken by another AWS account.
- Previously created bucket not cleaned up.

## How to Fix

**Use a unique naming convention:**

```hcl
resource "random_string" "bucket_suffix" {
  length  = 8
  special = false
  upper   = false
}

resource "aws_s3_bucket" "main" {
  bucket = "my-app-${var.environment}-${random_string.bucket_suffix.result}"
}
```

**Check if bucket exists:**

```bash
aws s3api head-bucket --bucket my-bucket-name 2>&1
```

## Examples

```hcl
resource "aws_s3_bucket" "logs" {
  bucket = "${var.project}-${var.environment}-logs-${random_id.suffix.hex}"
}
```
