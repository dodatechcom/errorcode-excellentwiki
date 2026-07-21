---
title: "[Solution] GCP Cloud Run Service"
description: "CloudRunError for Cloud Run."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cloud Run Service` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Service name taken
- Container image not found in Artifact Registry
- Min/max instances misconfigured

## How to Fix

### List services

```bash
gcloud run services list
```

## Examples

- Example scenario: service name taken
- Example scenario: container image not found in artifact registry
- Example scenario: min/max instances misconfigured

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
