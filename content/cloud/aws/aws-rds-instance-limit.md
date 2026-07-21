---
title: "[Solution] AWS RDS Instance Limit Exceeded"
description: "QuotaExceededException when the account RDS instance limit is reached."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS Instance Limit Exceeded` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Account limit (default 40) reached
- Stopped instances still count
- Different classes have different quotas
- Trying to create more than allowed

## How to Fix

### Check count

```bash
aws rds describe-db-instances --query "DBInstances[*].[DBInstanceIdentifier,DBInstanceClass]" --output table
```
### Request increase

```bash
aws service-quotas request-service-quota-increase --service-code rds --quota-code L-7B6409FD --desired-value 80 --region us-east-1
```
### Delete unused

```bash
aws rds delete-db-instance --db-instance-identifier my-old-db --skip-final-snapshot
```

## Examples

- Account has 40 DB instances and tries to create 41st
- All 40 are db.t3.micro but quota covers all types

## Related Errors

- [RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General RDS errors
- [DB Instance Not Found]({{< relref "/cloud/aws/aws-rds-instance-not-found" >}}) -- Instance not found
