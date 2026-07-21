---
title: "[Solution] AWS Provisioned Throughput Exceeded"
description: "ProvisionedThroughputExceededException."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Provisioned Throughput Exceeded` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Capacity consumed too quickly
- Hot partition

## How to Fix

### Describe table

```bash
aws dynamodb describe-table --table my-table
```

## Examples

- Example scenario: capacity consumed too quickly
- Example scenario: hot partition

## Related Errors

- [AWS LAMBDA Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General lambda errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
