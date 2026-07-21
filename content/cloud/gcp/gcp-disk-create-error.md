---
title: "[Solution] GCP Disk Create Error"
description: "DiskCreateError for PD creation."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Disk Create Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Disk name taken
- Snapshot not found
- Size less than source snapshot

## How to Fix

### Create disk

```bash
gcloud compute disks create myDisk --size=10GB --zone=us-central1-a
```

## Examples

- Example scenario: disk name taken
- Example scenario: snapshot not found
- Example scenario: size less than source snapshot

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
