---
title: "[Solution] GCP Requester Pays"
description: "RequesterPaysError for access."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Requester Pays` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Requester pays bucket
- User project not set
- Insufficient quota in user project

## How to Fix

### Access with project

```bash
gsutil cp gs://requester-pays-bucket/file.txt -u
```

## Examples

- Example scenario: requester pays bucket
- Example scenario: user project not set
- Example scenario: insufficient quota in user project

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
