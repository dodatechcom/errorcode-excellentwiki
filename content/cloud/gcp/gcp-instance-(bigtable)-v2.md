---
title: "[Solution] GCP Instance (Bigtable)"
description: "BigtableInstanceError for instances."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Instance (Bigtable)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Instance ID taken
- Cluster already exists in zone
- Storage type (SSD vs HDD) locked after creation

## How to Fix

### List instances

```bash
gcloud bigtable instances list
```

## Examples

- Example scenario: instance id taken
- Example scenario: cluster already exists in zone
- Example scenario: storage type (ssd vs hdd) locked after creation

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
