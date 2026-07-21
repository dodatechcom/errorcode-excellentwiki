---
title: "[Solution] GCP Service Usage"
description: "ServiceUsageError for quotas."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Service Usage` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Service usage quota exceeded
- Rate limit exceeded
- Concurrent requests limit

## How to Fix

### Quota info

```bash
gcloud services quota list
```

## Examples

- Example scenario: service usage quota exceeded
- Example scenario: rate limit exceeded
- Example scenario: concurrent requests limit

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
