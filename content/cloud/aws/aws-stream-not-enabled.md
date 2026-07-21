---
title: "[Solution] AWS Stream Not Enabled"
description: "ValidationException when streams off."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Stream Not Enabled` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Stream spec not set
- Trigger without stream

## How to Fix

### Check stream

```bash
aws dynamodb describe-table --table my-table --query StreamSpec
```

## Examples

- Example scenario: stream spec not set
- Example scenario: trigger without stream

## Related Errors

- [AWS DYNAMODB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General dynamodb errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
