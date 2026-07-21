---
title: "[Solution] GCP Eventarc Trigger"
description: "EventarcError for event triggers."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Eventarc Trigger` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Trigger not found
- Channel connection not active
- Event type not supported

## How to Fix

### List triggers

```bash
gcloud eventarc triggers list
```

## Examples

- Example scenario: trigger not found
- Example scenario: channel connection not active
- Example scenario: event type not supported

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
