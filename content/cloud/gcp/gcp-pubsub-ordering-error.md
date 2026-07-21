---
title: "[Solution] GCP Pub/Sub Message Ordering Error"
description: "Fix Pub/Sub message ordering errors. Resolve ordering key, publish ordering, and subscriber ordering issues in Google Cloud Pub/Sub."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Pub/Sub Message Ordering Error

The Pub/Sub Message Ordering error occurs when message ordering guarantees are violated due to publisher or subscriber configuration issues.

## Common Causes

- Publisher does not use ordering keys when publishing messages
- Subscriber acknowledges messages out of order
- Ordering key assignment is inconsistent across publishers
- Message retention expired for ordered messages
- Subscriber pull mode causes batch processing that ignores order

## How to Fix

### 1. Create subscription with ordering
```bash
gcloud pubsub subscriptions create SUBSCRIPTION_NAME \
  --topic=TOPIC_NAME \
  --enable-message-ordering \
  --ack-deadline-seconds=60
```

### 2. Enable message ordering on topic
```bash
gcloud pubsub topics update TOPIC_NAME \
  --message-ordering
```

### 3. Publish with ordering key
```python
from google.cloud import pubsub_v1
publisher = pubsub_v1.PublisherClient()
future = publisher.publish(
    TOPIC_PATH,
    data=b"hello",
    ordering_key="customer-123"
)
```

### 4. Acknowledge in order
```python
subscriber = pubsub_v1.SubscriberClient()
# Messages with same ordering_key arrive in order
# Ack each before pulling next
```

## Examples

### Publish ordered messages
```python
publisher = pubsub_v1.PublisherClient()
for i, event in enumerate(events):
    publisher.publish(
        TOPIC_PATH,
        data=json.dumps(event).encode(),
        ordering_key=f"order-{event['order_id']}"
    )
```

### Check subscription ordering status
```bash
gcloud pubsub subscriptions describe SUBSCRIPTION_NAME \
  --format="value(enableMessageOrdering)"
```

## Related Errors

- [GCP Pub/Sub Error]({{< relref "/cloud/gcp/gcp-pubsub-error" >}})
- [GCP Schema Pub Sub]({{< relref "/cloud/gcp/gcp-schema-(pub-sub)" >}})
