---
title: "[Solution] AWS RDS Instance Limit"
description: "InstanceLimitExceeded when the DB instance quota has been exceeded."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS Instance Limit` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Per-region DB instance quota reached
- RDS engines have separate limits

## How to Fix

### Check count

```bash
aws rds describe-db-instances --query DBInstances[*].[DBInstanceIdentifier]
```

### Request increase

```bash
aws service-quotas request-service-quota-increase --service-code rds --quota-code L-7B9D5F6A --desired-value 50
```

## Examples

- Example scenario: per-region db instance quota reached
- Example scenario: rds engines have separate limits

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General rds errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
