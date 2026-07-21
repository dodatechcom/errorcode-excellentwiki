---
title: "[Solution] GCP Health Check"
description: "HealthCheckError for health checks."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Health Check` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Health check not found
- Unhealthy threshold too low
- Check interval too short

## How to Fix

### Create health check

```bash
gcloud compute health-checks create tcp myHealthCheck --port=80
```

## Examples

- Example scenario: health check not found
- Example scenario: unhealthy threshold too low
- Example scenario: check interval too short

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
