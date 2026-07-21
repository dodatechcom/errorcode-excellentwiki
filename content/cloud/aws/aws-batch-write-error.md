---
title: "[Solution] AWS Batch Write Error"
description: "ValidationException for BatchWriteItem."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Batch Write Error` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Too many items (max 25)
- Duplicate items

## How to Fix

### Write one by one

```bash
aws dynamodb put-item --table my-table --item file://item.json
```

## Examples

- Example scenario: too many items (max 25)
- Example scenario: duplicate items

## Related Errors

- [AWS DYNAMODB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General dynamodb errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
