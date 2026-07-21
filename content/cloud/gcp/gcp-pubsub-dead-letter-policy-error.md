---
title: "[Solution] GCP Pub/Sub Dead Letter Policy Error"
description: "Fix Pub/Sub dead letter policy errors. Configure dead-letter topics, max delivery attempts, and message routing in Google Cloud Pub/Sub."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Pub/Sub Dead Letter Policy Error

The Pub/Sub Dead Letter Policy error occurs when dead-letter topics are misconfigured, causing messages to be lost or retried indefinitely.

## Common Causes

- Dead-letter topic does not exist in the project
- Subscription does not have dead-letter policy configured
- Max delivery attempts is set to 0 (infinite retries)
- Dead-letter topic lacks publish permissions
- Acknowledgment deadline is too short for processing

## How to Fix

### 1. Create dead-letter topic
```bash
gcloud pubsub topics create DEAD_LETTER_TOPIC
```

### 2. Update subscription with dead-letter policy
```bash
gcloud pubsub subscriptions update SUBSCRIPTION_NAME \
  --dead-letter-topic=projects/PROJECT_ID/topics/DEAD_LETTER_TOPIC \
  --max-delivery-attempts=5
```

### 3. Check dead-letter policy
```bash
gcloud pubsub subscriptions describe SUBSCRIPTION_NAME \
  --format="yaml(deadLetterPolicy)"
```

### 4. Grant publish permission
```bash
gcloud pubsub topics add-iam-policy-binding DEAD_LETTER_TOPIC \
  --member="serviceAccount:SA@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/pubsub.publisher"
```

## Examples

### Configure dead-letter with retry
```bash
gcloud pubsub subscriptions update my-sub \
  --dead-letter-topic=projects/my-project/topics/dlq \
  --max-delivery-attempts=3
```

### Monitor dead-letter messages
```bash
gcloud pubsub subscriptions describe dlq-sub \
  --format="value(numUnackedMessages)"
```

## Related Errors

- [GCP Pub/Sub Error]({{< relref "/cloud/gcp/gcp-pubsub-error" >}})
- [GCP Dead Letter]({{< relref "/cloud/gcp/gcp-dead-letter" >}})
