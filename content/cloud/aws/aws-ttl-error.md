---
title: "[Solution] AWS TTL Error"
description: "ValidationException for TTL config."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `TTL Error` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- TTL attribute missing from schema
- Wrong data type

## How to Fix

### Check TTL

```bash
aws dynamodb describe-time-to-live --table my-table
```

## Examples

- Example scenario: ttl attribute missing from schema
- Example scenario: wrong data type

## Related Errors

- [AWS DYNAMODB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General dynamodb errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
