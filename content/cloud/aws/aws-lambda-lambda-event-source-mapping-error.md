---
title: "[Solution] AWS Lambda Event Source Mapping Error"
description: "InvalidParameterValue/ResourceConflict for event source mapping."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Event Source Mapping Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- DynamoDB/Kinesis stream access denied
- Event source mapping limit reached (per function)
- SQS queue does not exist
- Batch size exceeds the maximum allowed
- Starting position not valid for stream checkpoint

## How to Fix

### List mappings

```bash
aws lambda list-event-source-mappings --function-name my-function
```

### Create mapping

```bash
aws lambda create-event-source-mapping --function-name my-function --event-source-arn arn:aws:sqs:us-east-1:123456789012:my-queue
```

## Examples

- Example scenario: dynamodb/kinesis stream access denied
- Example scenario: event source mapping limit reached (per function)
- Example scenario: sqs queue does not exist
- Example scenario: batch size exceeds the maximum allowed

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
