---
title: "[Solution] AWS S3 Transfer Acceleration"
description: "S3TransferAccelerationError when Transfer Acceleration endpoint fails."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Transfer Acceleration` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Bucket not enabled for Transfer Acceleration
- Upload rate exceeds 10 Gbps per bucket and region
- RTT less than 100ms to S3 endpoint
- TCP throughput lower than direct S3 endpoint
- Client has IP reputation issues

## How to Fix

### Check acceleration status

```bash
aws s3api get-bucket-accelerate-configuration --bucket my-bucket
```

### Enable acceleration

```bash
aws s3api put-bucket-accelerate-configuration --bucket my-bucket --status Enabled
```

### Test acceleration speed

```bash
aws s3 cp largefile.bin s3://my-bucket/ --region us-east-1 --endpoint-url https://my-bucket.s3-accelerate.amazonaws.com
```

## Examples

- Example scenario: bucket not enabled for transfer acceleration
- Example scenario: upload rate exceeds 10 gbps per bucket and region
- Example scenario: rtt less than 100ms to s3 endpoint
- Example scenario: tcp throughput lower than direct s3 endpoint

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
