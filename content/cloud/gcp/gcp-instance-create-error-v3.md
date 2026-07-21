---
title: "[Solution] GCP Instance Create Error"
description: "InstanceCreateError for creation."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Instance Create Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Machine type not available
- Disk image deprecated
- Network/ subnet not found

## How to Fix

### Create instance

```bash
gcloud compute instances create myVM --zone=us-central1-a --machine-type=e2-micro
```

## Examples

- Example scenario: machine type not available
- Example scenario: disk image deprecated
- Example scenario: network/ subnet not found

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
