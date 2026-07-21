---
title: "[Solution] AWS Lambda DLQ Not Configured"
description: "Custom resource events not delivered when DLQ is missing."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda DLQ Not Configured` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- DLQ target ARN (SQS/SNS) is invalid
- DLQ resource-based policy does not allow Lambda
- TOCTOU race in async invocation without DLQ
- Max retries (2) exhausted without DLQ configured
- Delivery to DLQ would exceed SQS/SNS throttles

## How to Fix

### Check DLQ config

```bash
aws lambda get-function-configuration --function-name my-function
```

### Set DLQ

```bash
aws lambda update-function-configuration --function-name my-function --dead-letter-config TargetArn=arn:aws:sqs:us-east-1:123456789012:my-dlq
```

## Examples

- Example scenario: dlq target arn (sqs/sns) is invalid
- Example scenario: dlq resource-based policy does not allow lambda
- Example scenario: toctou race in async invocation without dlq
- Example scenario: max retries (2) exhausted without dlq configured

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
