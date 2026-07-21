---
title: "[Solution] AWS S3 Event Notification Failed"
description: "InvalidArgument/NotImplemented for S3 Event Notifications."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Event Notification Failed` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Destination SQS/SNS topic not in same region
- SQS policy does not allow S3 to send messages
- Lambda function invocation permission missing
- EventBridge notification conflicts with SQS/SNS
- Event notification configuration quota hit (100 per bucket)

## How to Fix

### Get notification conf

```bash
aws s3api get-bucket-notification-configuration --bucket my-bucket
```

### Check EventBridge

```bash
aws s3api put-bucket-notification-configuration --bucket my-bucket --notification-configuration file://notif.json
```

## Examples

- Example scenario: destination sqs/sns topic not in same region
- Example scenario: sqs policy does not allow s3 to send messages
- Example scenario: lambda function invocation permission missing
- Example scenario: eventbridge notification conflicts with sqs/sns

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
