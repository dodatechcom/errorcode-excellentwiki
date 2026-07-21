---
title: "[Solution] GCP Billing"
description: "BillingError for billing."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Billing` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Billing account not found
- Billing not enabled for project
- Payment method expired

## How to Fix

### List billing accounts

```bash
gcloud billing accounts list
```

## Examples

- Example scenario: billing account not found
- Example scenario: billing not enabled for project
- Example scenario: payment method expired

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
