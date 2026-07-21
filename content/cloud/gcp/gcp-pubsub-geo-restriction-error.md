---
title: "[Solution] GCP Pub/Sub Geo Restriction Error"
description: "Fix Pub/Sub geo restriction errors. Resolve regional topic, subscription location, and multi-region Pub/Sub configuration issues."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Pub/Sub Geo Restriction Error

The Pub/Sub Geo Restriction error occurs when Pub/Sub topics or subscriptions are created in restricted regions or cross-region access is not configured.

## Common Causes

- Topic or subscription creation is in a restricted region
- Cross-region subscription is not configured
- Organization policy restricts resource locations
- Topic is in a different region than the publisher
- KMS key is not available in the topic region

## How to Fix

### 1. Check topic location
```bash
gcloud pubsub topics describe TOPIC_NAME --format="yaml(name)"
```

### 2. Create regional topic
```bash
gcloud pubsub topics create TOPIC_NAME --location=REGION
```

### 3. Check organization location policy
```bash
gcloud resource-manager org-policies list --folder=FOLDER_ID \
  --filter="constraint=constraints/gcp.resourceLocations"
```

### 4. Update topic labels
```bash
gcloud pubsub topics update TOPIC_NAME --update-labels=region=us-central1
```

## Examples

### Create topic in specific region
```bash
gcloud pubsub topics create regional-topic --location=us-east1
```

### List topics by region
```bash
gcloud pubsub topics list --format="table(name)"
```

## Related Errors

- [GCP Pub/Sub Error]({{< relref "/cloud/gcp/gcp-pubsub-error" >}})
- [GCP Topic Not Found]({{< relref "/cloud/gcp/gcp-topic-not-found" >}})
