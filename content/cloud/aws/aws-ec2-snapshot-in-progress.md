---
title: "[Solution] AWS EC2 Snapshot In Progress"
description: "ResourceAlreadyInProgressException when a snapshot is already being processed."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Snapshot In Progress` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- A snapshot for this volume is already in progress
- Previous snapshot not completed
- Concurrent snapshot limit reached
- Lifecycle policy triggered overlapping snapshots

## How to Fix

### Check snapshot state

```bash
aws ec2 describe-snapshots --filters Name=volume-id,Values=vol-0abc --query 'Snapshots[*].[SnapshotId,State,Progress]'
```
### Wait for completion

```bash
aws ec2 wait snapshot-completed --snapshot-ids snap-0abc123
```
### Cancel snapshot

```bash
aws ec2 cancel-snapshot --snapshot-id snap-0abc123
```

## Examples

- Creating snapshot when snap-old is still 45% complete
- Lifecycle policy triggered new snapshot before previous finished

## Related Errors

- [Snapshot Error]({{< relref "/cloud/aws/aws-ec2-snapshot-error" >}}) -- Snapshot errors
- [EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
