---
title: "[Solution] GCP Instance Not Found"
description: "InstanceNotFound for GCE instances."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Instance Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Instance name incorrect
- Deleted by admin
- Zone mismatch

## How to Fix

### List instances

```bash
gcloud compute instances list
```

## Examples

- Example scenario: instance name incorrect
- Example scenario: deleted by admin
- Example scenario: zone mismatch

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
