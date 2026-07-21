---
title: "[Solution] AWS Event notification"
description: "InvalidArgument for S3 event notifications."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Event notification` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Dest SQS/SNS in different region
- SQS policy missing
- 100 per bucket quota hit

## How to Fix

### Get notification config

```bash
aws s3api get-bucket-notification-config --bucket my-bucket
```

## Examples

- Example scenario: dest sqs/sns in different region
- Example scenario: sqs policy missing
- Example scenario: 100 per bucket quota hit

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
