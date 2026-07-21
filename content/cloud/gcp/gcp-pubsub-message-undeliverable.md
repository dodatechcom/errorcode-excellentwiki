---
title: "[Solution] GCP Pub/Sub Message Undeliverable"
description: "Fix Pub/Sub undeliverable message errors. Resolve dead-letter, retry, and subscription configuration issues in Google Cloud Pub/Sub."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Pub/Sub Message Undeliverable

The Pub/Sub Message Undeliverable error occurs when messages cannot be delivered to subscribers after exhausting all retry attempts.

## Common Causes

- Dead-letter topic is not configured and message delivery fails
- Acknowledgment deadline is too short for processing time
- Subscriber endpoint is unreachable or returns errors
- Message retention period is exceeded
- Push endpoint rejects messages with non-2xx status

## How to Fix

### 1. Configure dead-letter topic
```bash
gcloud pubsub subscriptions update SUBSCRIPTION_NAME \
  --dead-letter-topic=projects/PROJECT_ID/topics/DEAD_LETTER_TOPIC
```

### 2. Extend acknowledgment deadline
```bash
gcloud pubsub subscriptions update SUBSCRIPTION_NAME \
  --ack-deadline-seconds=120
```

### 3. Check subscription backlog
```bash
gcloud pubsub subscriptions describe SUBSCRIPTION_NAME \
  --format="value(numUnackedMessages)"
```

### 4. Increase message retention
```bash
gcloud pubsub subscriptions update SUBSCRIPTION_NAME \
  --message-retention-duration=86400s
```

## Examples

### Set up dead-letter policy
```bash
gcloud pubsub subscriptions update my-subscription \
  --dead-letter-topic=projects/my-project/topics/dead-letter \
  --max-delivery-attempts=5
```

### Check undelivered messages
```bash
gcloud pubsub topics list --format="table(name)"
```

## Related Errors

- [GCP Pub/Sub Error]({{< relref "/cloud/gcp/gcp-pubsub-error" >}})
- [GCP Dead Letter]({{< relref "/cloud/gcp/gcp-dead-letter" >}})
