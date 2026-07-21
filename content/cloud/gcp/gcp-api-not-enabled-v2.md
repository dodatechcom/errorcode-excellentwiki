---
title: "[Solution] GCP API Not Enabled"
description: "APINotEnabled for GCP APIs."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `API Not Enabled` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- API not enabled for project
- Billing not set up for project
- API quota exhausted

## How to Fix

### Enable API

```bash
gcloud services enable compute.googleapis.com
```

## Examples

- Example scenario: api not enabled for project
- Example scenario: billing not set up for project
- Example scenario: api quota exhausted

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
