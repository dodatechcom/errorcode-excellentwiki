---
title: "[Solution] AWS Write Capacity Exceeded"
description: "WriteCapacityExceededException."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Write Capacity Exceeded` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- WCU limit reached
- Burst consumed

## How to Fix

### Increase WCU

```bash
aws dynamodb update-table --table my-table --provisioned-throughput WriteCapacityUnits=20
```

## Examples

- Example scenario: wcu limit reached
- Example scenario: burst consumed

## Related Errors

- [AWS DYNAMODB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General dynamodb errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
