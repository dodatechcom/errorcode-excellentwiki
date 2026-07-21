---
title: "[Solution] GCP Disk Not Found"
description: "DiskNotFound for persistent disks."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Disk Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Disk name incorrect
- Disk detached from instance
- Zone mismatch

## How to Fix

### List disks

```bash
gcloud compute disks list
```

## Examples

- Example scenario: disk name incorrect
- Example scenario: disk detached from instance
- Example scenario: zone mismatch

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
