---
title: "[Solution] AWS On-Demand Capacity"
description: "RequestLimitExceeded for on-demand table."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `On-Demand Capacity` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Per-table max reached
- Not suitable for steady traffic

## How to Fix

### Switch billing

```bash
aws dynamodb update-table --table my-table --billing PAY_PER_REQUEST
```

## Examples

- Example scenario: per-table max reached
- Example scenario: not suitable for steady traffic

## Related Errors

- [AWS DYNAMODB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General dynamodb errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
