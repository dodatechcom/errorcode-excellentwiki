---
title: "[Solution] AWS RDS Snapshot Restore"
description: "SnapshotRestoreError when restoring from snapshot fails."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS Snapshot Restore` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Source snapshot not available
- Cross-region copy incomplete
- KMS key mismatch

## How to Fix

### List snapshots

```bash
aws rds describe-db-snapshots --snapshot-type manual
```

### Restore

```bash
aws rds restore-db-instance-from-db-snapshot --db-instance-identifier my-restored-db --db-snapshot-identifier my-snapshot
```

## Examples

- Example scenario: source snapshot not available
- Example scenario: cross-region copy incomplete
- Example scenario: kms key mismatch

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General rds errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
