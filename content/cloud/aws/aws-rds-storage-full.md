---
title: "[Solution] AWS RDS Storage Full"
description: "StorageFull when the RDS instance has run out of storage."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS Storage Full` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Allocated storage insufficient
- Transaction logs consuming space
- Binary logging filling storage
- Automated backups need space

## How to Fix

### Check storage

```bash
aws rds describe-db-instances --db-instance-identifier my-db --query "DBInstances[*].[AllocatedStorage,FreeStorageSpace,StorageType]"
```
### Modify storage

```bash
aws rds modify-db-instance --db-instance-identifier my-db --allocated-storage 200 --apply-immediately
```
### Enable autoscaling

```bash
aws rds modify-db-instance --db-instance-identifier my-db --storage-autoscaling --max-allocated-storage 1000 --apply-immediately
```

## Examples

- 100 GB instance with 0.5 GB free
- Binary log retention consuming 80%

## Related Errors

- [RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General RDS errors
- [Storage Scaling]({{< relref "/cloud/aws/aws-rds-storage-scaling" >}}) -- Storage scaling
