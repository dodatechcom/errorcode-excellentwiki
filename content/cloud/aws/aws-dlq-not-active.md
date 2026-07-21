---
title: "[Solution] AWS DLQ not active"
description: "Custom resources lost DLQ missing."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `DLQ not active` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- SQS/SNS target invalid
- No DLQ provided

## How to Fix

### Set DLQ

```bash
aws lambda update-function-config --function my-function --dead-letter TargetArn=arn:aws:sqs::123:mydlq
```

## Examples

- Example scenario: sqs/sns target invalid
- Example scenario: no dlq provided

## Related Errors

- [AWS LAMBDA Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General lambda errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
