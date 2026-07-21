---
title: "[Solution] GCP Topic Not Found"
description: "PubSubTopicNotFound for topics."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Topic Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Topic name incorrect
- Project mismatch
- Deleted by admin

## How to Fix

### List topics

```bash
gcloud pubsub topics list
```

## Examples

- Example scenario: topic name incorrect
- Example scenario: project mismatch
- Example scenario: deleted by admin

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
