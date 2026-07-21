---
title: "[Solution] GCP Image Not Found"
description: "ImageNotFound for images."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Image Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Image name incorrect
- Project does not have image
- Deprecated or deleted

## How to Fix

### List images

```bash
gcloud compute images list
```

## Examples

- Example scenario: image name incorrect
- Example scenario: project does not have image
- Example scenario: deprecated or deleted

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
