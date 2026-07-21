---
title: "[Solution] GCP Origin (CDN)"
description: "CDNOriginError for origins."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Origin (CDN)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Origin not accessible from Edge cache
- Origin returns 5xx
- HTTPS only backend requires valid cert

## How to Fix

### Create backend bucket

```bash
gcloud compute backend-buckets create myBucket --gcs-bucket-name=myBucket
```

## Examples

- Example scenario: origin not accessible from edge cache
- Example scenario: origin returns 5xx
- Example scenario: https only backend requires valid cert

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
