---
title: "[Solution] GCP Pub/Sub Lite Error -- topic subscription capacity errors"
description: "Fix GCP Pub/Sub Lite errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 135
---

Pub/Sub Lite errors occur when there are issues with topic creation, subscription management, or capacity configuration.

## Common Causes
- Partition count insufficient for throughput
- Subscription backlog exceeds storage capacity
- Zone outage affecting Lite topic availability
- Publish rate exceeds partition limits
- Pub/Sub Lite API not enabled

## How to Fix

### 1. Enable Pub/Sub Lite API
```bash
gcloud services enable pubsublite.googleapis.com --project=PROJECT_ID
```

### 2. List topics and subscriptions
```bash
gcloud pubsub lite topics list --location=REGION
gcloud pubsub lite subscriptions list --location=REGION
```

### 3. Create topic with partitions
```bash
gcloud pubsub lite topics create TOPIC_NAME \
  --location=REGION \
  --partitions=3 \
  --storage-capacity=30GiB
```

### 4. Create subscription
```bash
gcloud pubsub lite subscriptions create SUBSCRIPTION_NAME \
  --location=REGION \
  --topic=TOPIC_NAME \
  --delivery-requirement=deliver-after-storage-latest \
  --offset-retention-time=604800s
```

### 5. Update topic capacity
```bash
gcloud pubsub lite topics update TOPIC_NAME \
  --location=REGION \
  --partitions=6
```

## Examples

### Create regional topic
```bash
gcloud pubsub lite topics create orders-topic \
  --location=us-central1-a \
  --partitions=5 \
  --storage-capacity=50GiB
```

### Create subscription with skip backlog
```bash
gcloud pubsub lite subscriptions create orders-sub \
  --location=us-central1-a \
  --topic=orders-topic \
  --delivery-requirement=deliver-now
```

## Related Errors
- [GCP Pub/Sub Error](/cloud/gcp/gcp-pubsub-error/)
- [GCP Cloud Tasks Error](/cloud/gcp/gcp-cloud-tasks-error/)
- [GCP Dataflow Error](/cloud/gcp/gcp-dataflow-error/)