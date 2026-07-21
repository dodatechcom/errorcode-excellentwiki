---
title: "[Solution] AWS Encryption mismatch"
description: "KMS.DecryptException/BadDigest SSE settings conflict."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Encryption mismatch` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Bucket SSE and request SSE mismatch
- Algorithm differs between source and dest

## How to Fix

### Check encryption

```bash
aws s3api get-bucket-encryption --bucket my-bucket
```

## Examples

- Example scenario: bucket sse and request sse mismatch
- Example scenario: algorithm differs between source and dest

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
