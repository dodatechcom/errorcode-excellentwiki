---
title: "[Solution] GCP Cloud Run Revision"
description: "CloudRunRevisionError for revisions."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cloud Run Revision` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Revision name not found
- Traffic split not 100%
- Revision not healthy yet

## How to Fix

### Show revisions

```bash
gcloud run revisions list --service=myService
```

## Examples

- Example scenario: revision name not found
- Example scenario: traffic split not 100%
- Example scenario: revision not healthy yet

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
