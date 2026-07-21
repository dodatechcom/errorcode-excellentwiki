---
title: "[Solution] GCP Connection Error (CloudSQL)"
description: "CloudSQLConnectionError for connectivity."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Connection Error (CloudSQL)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Authorized networks not set
- SSL required but not configured
- Private IP not accessible

## How to Fix

### Add authorized network

```bash
gcloud sql instances patch myInstance --authorized-networks=0.0.0.0/0
```

## Examples

- Example scenario: authorized networks not set
- Example scenario: ssl required but not configured
- Example scenario: private ip not accessible

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
