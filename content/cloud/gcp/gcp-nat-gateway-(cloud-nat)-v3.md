---
title: "[Solution] GCP NAT Gateway (Cloud NAT)"
description: "CloudNATError for NAT."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `NAT Gateway (Cloud NAT)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- NAT already exists for region
- Router already configured
- Cloud NAT IP allocation failed

## How to Fix

### Create Cloud NAT

```bash
gcloud compute routers nats create myNat --router=myRouter --region=us-central1
```

## Examples

- Example scenario: nat already exists for region
- Example scenario: router already configured
- Example scenario: cloud nat ip allocation failed

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
