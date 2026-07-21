---
title: "[Solution] AWS RDS Parameter Group"
description: "InvalidParameterValue for parameter group."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS Parameter Group` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Group incompatible with engine version
- Value out of range

## How to Fix

### List groups

```bash
aws rds describe-db-parameter-groups
```

## Examples

- Example scenario: group incompatible with engine version
- Example scenario: value out of range

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General rds errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
