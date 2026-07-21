---
title: "[Solution] AWS Auto Scaling"
description: "ValidationException for scaling."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Auto Scaling` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Target tracking invalid
- Min and max equal

## How to Fix

### Check targets

```bash
aws app-autoscaling describe-scalable-targets --service dynamodb
```

## Examples

- Example scenario: target tracking invalid
- Example scenario: min and max equal

## Related Errors

- [AWS DYNAMODB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General dynamodb errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
