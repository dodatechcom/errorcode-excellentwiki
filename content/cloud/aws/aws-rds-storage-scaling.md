---
title: "[Solution] AWS RDS Storage Scaling"
description: "InvalidParameterCombination when storage scaling fails."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS Storage Scaling` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Modify not supported
- Storage exceeds max for instance class

## How to Fix

### Describe instance

```bash
aws rds describe-db-instances --db-instance-identifier mydb
```

## Examples

- Example scenario: modify not supported
- Example scenario: storage exceeds max for instance class

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General rds errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
