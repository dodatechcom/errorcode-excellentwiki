---
title: "[Solution] GCP Dead Letter"
description: "PubSubDeadLetterError for DLQ."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Dead Letter` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Dead letter topic not set
- Max delivery attempts (5-100) out of range
- Forwarding loop detected

## How to Fix

### Set DLQ

```bash
gcloud pubsub subscriptions update mySubscription --dead-letter-topic=myDLQTopic
```

## Examples

- Example scenario: dead letter topic not set
- Example scenario: max delivery attempts (5-100) out of range
- Example scenario: forwarding loop detected

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
