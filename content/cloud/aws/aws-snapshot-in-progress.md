---
title: "[Solution] AWS Snapshot in progress"
description: "SnapshotCreationPermission when another snapshot is active."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Snapshot in progress` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Another snapshot running for the volume
- Too many concurrent snapshots
- Snap quota reached

## How to Fix

### Check progress

```bash
aws ec2 describe-snapshots --owner self --filters Name=volume,Values=vol-0abc
```

### Wait for completion

```bash
aws ec2 wait snapshot-completed --snap snap-0abc
```

## Examples

- Example scenario: another snapshot running for the volume
- Example scenario: too many concurrent snapshots
- Example scenario: snap quota reached

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
