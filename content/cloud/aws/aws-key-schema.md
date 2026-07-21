---
title: "[Solution] AWS Key Schema"
description: "ValidationException for key schema."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Key Schema` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Missing partition key
- GSI key mismatch

## How to Fix

### Describe schema

```bash
aws dynamodb describe-table --table my-table --query KeySchema
```

## Examples

- Example scenario: missing partition key
- Example scenario: gsi key mismatch

## Related Errors

- [AWS DYNAMODB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General dynamodb errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
