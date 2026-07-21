---
title: "[Solution] AWS Item Too Large"
description: "ValidationException size exceeds 400KB."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Item Too Large` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Size over 400 KB
- Binary data not compressed

## How to Fix

### Check item

```bash
aws dynamodb get-item --table my-table
```

## Examples

- Example scenario: size over 400 kb
- Example scenario: binary data not compressed

## Related Errors

- [AWS DYNAMODB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General dynamodb errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
