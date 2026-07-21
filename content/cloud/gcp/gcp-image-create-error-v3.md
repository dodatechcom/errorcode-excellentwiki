---
title: "[Solution] GCP Image Create Error"
description: "ImageCreateError for custom images."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Image Create Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Image name taken
- Source disk not found
- Licensing requirements not met

## How to Fix

### Create image

```bash
gcloud compute images create myImage --source-disk myDisk --source-disk-zone=us-central1-a
```

## Examples

- Example scenario: image name taken
- Example scenario: source disk not found
- Example scenario: licensing requirements not met

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
