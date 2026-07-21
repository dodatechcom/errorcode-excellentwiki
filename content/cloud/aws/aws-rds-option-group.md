---
title: "[Solution] AWS RDS Option Group"
description: "InvalidOptionGroupState for option groups."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS Option Group` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Group not compatible with engine
- Cannot remove permanent option

## How to Fix

### List groups

```bash
aws rds describe-option-groups
```

## Examples

- Example scenario: group not compatible with engine
- Example scenario: cannot remove permanent option

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General rds errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
