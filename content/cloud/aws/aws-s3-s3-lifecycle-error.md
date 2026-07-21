---
title: "[Solution] AWS S3 Lifecycle Error"
description: "MalformedXML/InvalidRequest for S3 Lifecycle rules."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Lifecycle Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Rule ID already exists
- Invalid date format in expiration
- Transition to INTELLIGENT_TIERING not allowed
- Noncurrent version expiration before transition
- Minimal storage size for transition not met (128KB)

## How to Fix

### Get lifecycle config

```bash
aws s3api get-bucket-lifecycle-configuration --bucket my-bucket
```

## Examples

- Example scenario: rule id already exists
- Example scenario: invalid date format in expiration
- Example scenario: transition to intelligent_tiering not allowed
- Example scenario: noncurrent version expiration before transition

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
