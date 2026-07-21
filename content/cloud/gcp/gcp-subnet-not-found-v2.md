---
title: "[Solution] GCP Subnet Not Found"
description: "SubnetNotFound for subnets."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Subnet Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Subnet name incorrect
- Region mismatch
- Not part of VPC

## How to Fix

### List subnets

```bash
gcloud compute networks subnets list
```

## Examples

- Example scenario: subnet name incorrect
- Example scenario: region mismatch
- Example scenario: not part of vpc

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
