---
title: "[Solution] GCP VPC Not Found"
description: "VPCNotFound for VPC networks."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VPC Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Network name incorrect
- Deleted by admin
- Project mismatch

## How to Fix

### List VPCs

```bash
gcloud compute networks list
```

## Examples

- Example scenario: network name incorrect
- Example scenario: deleted by admin
- Example scenario: project mismatch

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
