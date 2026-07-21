---
title: "[Solution] AWS Condition Expression"
description: "ConditionalCheckFailedException."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Condition Expression` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Expression false
- Attribute nonexistent

## How to Fix

### Put with condition

```bash
aws dynamodb put-item --table my-table --item file://item.json --condition attribute_not_exists(PK)
```

## Examples

- Example scenario: expression false
- Example scenario: attribute nonexistent

## Related Errors

- [AWS DYNAMODB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General dynamodb errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
