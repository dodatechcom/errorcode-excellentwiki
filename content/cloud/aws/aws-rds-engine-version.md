---
title: "[Solution] AWS RDS Engine Version"
description: "IncompatibleRestore for engine upgrades."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS Engine Version` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Major version unsupported
- Version unavailable in region

## How to Fix

### Check versions

```bash
aws rds describe-db-engine-versions --engine mysql
```

## Examples

- Example scenario: major version unsupported
- Example scenario: version unavailable in region

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General rds errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
