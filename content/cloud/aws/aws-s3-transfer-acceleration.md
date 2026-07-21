---
title: "[Solution] AWS S3 Transfer Acceleration"
description: "S3TransferAccelerationError acceleration endpoint fails."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Transfer Acceleration` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Bucket not enabled
- Upload more than 10 Gbps in region

## How to Fix

### Check status

```bash
aws s3api get-bucket-accelerate-config --bucket my-bucket
```

### Enable

```bash
aws s3api put-bucket-accelerate-config --bucket my-bucket --state Enabled
```

## Examples

- Example scenario: bucket not enabled
- Example scenario: upload more than 10 gbps in region

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) -- General s3 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
