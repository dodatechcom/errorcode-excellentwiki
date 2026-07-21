---
title: "[Solution] AWS S3 Bucket Policy Error"
description: "MalformedPolicy/PolicyTooLong when S3 bucket policy fails."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Bucket Policy Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Policy size exceeds 20 KB limit
- Invalid principal or effect syntax
- Missing required Action or Resource statements
- Cross-service confused deputy protection missing
- Resource ARN does not match bucket correctly

## How to Fix

### Get current bucket policy

```bash
aws s3api get-bucket-policy --bucket my-bucket
```

### Delete policy

```bash
aws s3api delete-bucket-policy --bucket my-bucket
```

### Put new policy

```bash
aws s3api put-bucket-policy --bucket my-bucket --policy file://policy.json
```

## Examples

- Example scenario: policy size exceeds 20 kb limit
- Example scenario: invalid principal or effect syntax
- Example scenario: missing required action or resource statements
- Example scenario: cross-service confused deputy protection missing

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
