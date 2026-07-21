---
title: "[Solution] GCP Subscription Not Found"
description: "PubSubSubscriptionNotFound for subscriptions."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Subscription Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Subscription name incorrect
- Pull vs push mismatch
- Subscription detached from topic

## How to Fix

### List subscriptions

```bash
gcloud pubsub subscriptions list
```

## Examples

- Example scenario: subscription name incorrect
- Example scenario: pull vs push mismatch
- Example scenario: subscription detached from topic

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
