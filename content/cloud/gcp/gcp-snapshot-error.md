---
title: "[Solution] GCP Snapshot Error"
description: "SnapshotError for snapshots."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Snapshot Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Snapshot name taken
- Disk needs to be detached/exclusive
- Snapshot quota exceeded

## How to Fix

### Create snapshot

```bash
gcloud compute disks snapshot myDisk --snapshot-names mySnapshot
```

## Examples

- Example scenario: snapshot name taken
- Example scenario: disk needs to be detached/exclusive
- Example scenario: snapshot quota exceeded

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
