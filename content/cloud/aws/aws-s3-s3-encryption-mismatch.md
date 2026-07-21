---
title: "[Solution] AWS S3 Encryption Mismatch"
description: "KMS.DecryptException/BadDigest when S3 SSE settings conflict."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Encryption Mismatch` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- SSE-S3 vs SSE-KMS mismatch between bucket and request
- KMS key ID used in request does not match bucket key
- Object was encrypted with different algorithm
- Downgrade from SSE-KMS to SSE-S3 on existing object
- Dual-layer encryption conflict

## How to Fix

### Check bucket encryption

```bash
aws s3api get-bucket-encryption --bucket my-bucket
```

### Update bucket encryption

```bash
aws s3api put-bucket-encryption --bucket my-bucket --server-side-encryption-configuration file://sse-config.json
```

## Examples

- Example scenario: sse-s3 vs sse-kms mismatch between bucket and request
- Example scenario: kms key id used in request does not match bucket key
- Example scenario: object was encrypted with different algorithm
- Example scenario: downgrade from sse-kms to sse-s3 on existing object

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
