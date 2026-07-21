---
title: "[Solution] AWS Batch Get Error"
description: "ValidationException for BatchGetItem."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Batch Get Error` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Too many items (max 100)
- Total request more than 16MB

## How to Fix

### Retry unprocessed

```bash
aws dynamodb batch-get-item --request file://batch.json
```

## Examples

- Example scenario: too many items (max 100)
- Example scenario: total request more than 16mb

## Related Errors

- [AWS DYNAMODB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General dynamodb errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
