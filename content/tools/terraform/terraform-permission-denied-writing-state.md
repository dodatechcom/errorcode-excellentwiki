---
title: "[Solution] Terraform Permission Denied Writing State"
description: "Fix Terraform permission denied errors when writing to the state backend."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Permission denied writing state errors prevent Terraform from saving state:

```
Error: Error writing state

AccessDenied: Access Denied
status code: 403
```

## Common Causes

- IAM role/user lacks `s3:PutObject` permission.
- S3 bucket policy restricts writes.

## How to Fix

**Check current identity:**

```bash
aws sts get-caller-identity
```

**Grant required permissions:**

```hcl
data "aws_iam_policy_document" "terraform_state" {
  statement {
    actions = [
      "s3:PutObject",
      "s3:GetObject",
      "s3:DeleteObject",
    ]
    resources = ["arn:aws:s3:::my-bucket/terraform/*"]
  }

  statement {
    actions   = ["s3:ListBucket"]
    resources = ["arn:aws:s3:::my-bucket"]
  }
}
```

## Examples

```hcl
resource "aws_s3_bucket_policy" "terraform" {
  bucket = aws_s3_bucket.terraform.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { AWS = "arn:aws:iam::123456789012:role/terraform" }
      Action    = ["s3:PutObject", "s3:GetObject"]
      Resource  = "arn:aws:s3:::my-bucket/terraform/*"
    }]
  })
}
```
