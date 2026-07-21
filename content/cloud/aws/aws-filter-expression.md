---
title: "[Solution] AWS Filter Expression"
description: "ValidationException for filter."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Filter Expression` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Syntax error
- Invalid function name
- Type mismatch

## How to Fix

### Query with filter

```bash
aws dynamodb query --table my-table --filter file://filter.json
```

## Examples

- Example scenario: syntax error
- Example scenario: invalid function name
- Example scenario: type mismatch

## Related Errors

- [AWS DYNAMODB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General dynamodb errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
