---
title: "[Solution] AWS Read Capacity Exceeded"
description: "ReadCapacityExceededException."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Read Capacity Exceeded` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- RCU limit reached
- Expensive Scan operation
- Consistent reads cost double

## How to Fix

### Increase RCU

```bash
aws dynamodb update-table --table my-table --provisioned-throughput ReadCapacityUnits=20
```

## Examples

- Example scenario: rcu limit reached
- Example scenario: expensive scan operation
- Example scenario: consistent reads cost double

## Related Errors

- [AWS DYNAMODB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General dynamodb errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
