---
title: "[Solution] AWS RDS Subnet Group"
description: "InvalidVPCNetworkStateFault for subnet groups."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS Subnet Group` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- References deleted subnets
- Subnets in different AZs

## How to Fix

### List groups

```bash
aws rds describe-db-subnet-groups
```

## Examples

- Example scenario: references deleted subnets
- Example scenario: subnets in different azs

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General rds errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
