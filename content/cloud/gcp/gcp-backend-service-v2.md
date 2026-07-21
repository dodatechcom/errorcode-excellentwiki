---
title: "[Solution] GCP Backend Service"
description: "BackendServiceError for backends."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Backend Service` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Backend service not found
- Backend bucket not ready
- Session affinity not set correctly

## How to Fix

### Create backend

```bash
gcloud compute backend-services create myBackend --protocol=HTTP --health-checks myHealthCheck
```

## Examples

- Example scenario: backend service not found
- Example scenario: backend bucket not ready
- Example scenario: session affinity not set correctly

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
