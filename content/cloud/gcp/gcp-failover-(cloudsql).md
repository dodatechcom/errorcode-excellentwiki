---
title: "[Solution] GCP Failover (CloudSQL)"
description: "CloudSQLFailoverError for failover."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Failover (CloudSQL)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- High availability not configured
- Secondary zone same as primary
- Failover already in progress

## How to Fix

### Trigger failover

```bash
gcloud sql instances failover myInstance
```

## Examples

- Example scenario: high availability not configured
- Example scenario: secondary zone same as primary
- Example scenario: failover already in progress

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
