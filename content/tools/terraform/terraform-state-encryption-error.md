---
title: "[Solution] Terraform State Encryption Error"
description: "Fix Terraform state encryption errors when the state backend encryption is misconfigured."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

State encryption errors occur when encrypted state cannot be read or written:

```
Error: Error decrypting state

Error: KMS access denied: arn:aws:kms:us-east-1:123456789012:key/abc-123
```

## Common Causes

- KMS key doesn't exist or is in different region.
- IAM role lacks `kms:Decrypt`/`kms:Encrypt` permission.

## How to Fix

**Verify KMS key:**

```bash
aws kms describe-key --key-id abc-123
```

**Grant KMS permissions:**

```hcl
{
  "Effect": "Allow",
  "Action": [
    "kms:Decrypt",
    "kms:Encrypt",
    "kms:GenerateDataKey"
  ],
  "Resource": "arn:aws:kms:us-east-1:123456789012:key/abc-123"
}
```

## Examples

```hcl
terraform {
  backend "s3" {
    bucket     = "my-encrypted-bucket"
    key        = "terraform.tfstate"
    encrypt    = true
    kms_key_id = "arn:aws:kms:us-east-1:123456789012:key/abc-123"
  }
}
```
