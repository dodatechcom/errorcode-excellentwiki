---
title: "[Solution] AWS RDS Storage Full"
description: "StorageFull when the RDS instance storage is exhausted."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS Storage Full` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Allocated storage consumed by data growth
- Binlogs not purged

## How to Fix

### Check size

```bash
aws rds describe-db-instances --db-instance-identifier mydb --query DBInstances[*].AllocatedStorage
```

### Modify

```bash
aws rds modify-db-instance --db-instance-identifier mydb --allocated-storage 200 --apply-immediately
```

## Examples

- Example scenario: allocated storage consumed by data growth
- Example scenario: binlogs not purged

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General rds errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
