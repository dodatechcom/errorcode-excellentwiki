---
title: "[Solution] GCP Publish Error"
description: "PubSubPublishError for publishing."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Publish Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Message size > 10 MB
- Ordering key not supported on topic
- Topic throttled (10000 msg/s per region)

## How to Fix

### Publish message

```bash
gcloud pubsub topics publish myTopic --message='hello'
```

## Examples

- Example scenario: message size > 10 mb
- Example scenario: ordering key not supported on topic
- Example scenario: topic throttled (10000 msg/s per region)

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
