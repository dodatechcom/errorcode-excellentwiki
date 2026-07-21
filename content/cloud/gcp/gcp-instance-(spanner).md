---
title: "[Solution] GCP Instance (Spanner)"
description: "SpannerInstanceError for Spanner instances."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Instance (Spanner)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Instance name taken
- Configuration not available in region
- Processing units out of range (100-100000)

## How to Fix

### List instances

```bash
gcloud spanner instances list
```

## Examples

- Example scenario: instance name taken
- Example scenario: configuration not available in region
- Example scenario: processing units out of range (100-100000)

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
