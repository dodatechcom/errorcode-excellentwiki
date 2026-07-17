---
title: "[Solution] AWS KMS Key Error"
description: "Fix AWS KMS key errors. Resolve KMS encryption and key management issues."
cloud: ["aws"]
error-types: ["api-error"]
severities: ["error"]
tags: ["aws", "kms", "key", "encryption", "decrypt"]
weight: 5
---

An AWS KMS key error occurs when KMS operations fail due to key configuration, permissions, or state issues.

## Common Causes

- KMS key is disabled or pending deletion
- IAM permissions not granted for KMS actions
- Key policy does not allow the operation
- KMS key is in a different region than the service
- Envelope encryption key material mismatch

## How to Fix

### Check Key Status

```bash
aws kms describe-key --key-id alias/my-key
```

### Enable Key

```bash
aws kms enable-key --key-id alias/my-key
```

### Grant KMS Permissions

```bash
aws kms put-key-policy \
  --key-id alias/my-key \
  --policy-name default \
  --policy '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"AWS": "arn:aws:iam::123456789012:role/my-role"},
      "Action": ["kms:Decrypt", "kms:Encrypt"],
      "Resource": "*"
    }]
  }'
```

### Test Encrypt/Decrypt

```bash
aws kms encrypt --key-id alias/my-key --plaintext "test"
aws kms decrypt --ciphertext-blob fileb://encrypted.bin
```

## Examples

```bash
# Example 1: Key disabled
# DisabledException: arn:aws:kms:...
# Fix: aws kms enable-key --key-id alias/my-key

# Example 2: Access denied
# AccessDeniedException
# Fix: add kms:Decrypt permission to the role
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission denied
- [AWS Secrets Manager]({{< relref "/cloud/aws/aws-secrets-manager" >}}) — Secrets Manager error
