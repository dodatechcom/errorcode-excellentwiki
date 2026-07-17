---
title: "[Solution] GCP Pub/Sub — topic not found"
description: "Fix Pub/Sub topic not found. Resolve Pub/Sub topic and subscription issues."
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A Pub/Sub topic not found error means the specified topic does not exist in the project, or the caller lacks the required IAM permissions to access it. Publish or subscribe operations fail immediately.

## What This Error Means

Google Cloud Pub/Sub identifies topics by their full resource name: `projects/project-id/topics/topic-name`. When a client attempts to publish to or create a subscription for a topic, Pub/Sub first verifies the topic exists and the caller has access. A "not found" error can mean the topic was never created, was deleted, the name is misspelled, or the caller lacks `pubsub.topics.get` permission. The error appears as a gRPC `NOT_FOUND` or HTTP 404 status.

## Common Causes

- Topic does not exist in the specified project
- Topic name is misspelled or wrong project specified
- Topic was deleted by another process or automation
- Caller lacks `pubsub.topics.get` or `pubsub.topics.publish` permission
- Region mismatch (Pub/Sub is global, but resource naming may confuse)
- Default topic created by GCP service (e.g., logging) does not exist yet

## How to Fix

### List Available Topics

```bash
gcloud pubsub topics list --project=my-project
```

### Check Topic Exists

```bash
gcloud pubsub topics describe my-topic --project=my-project
```

### Create Missing Topic

```bash
gcloud pubsub topics create my-topic --project=my-project
```

### Check Permissions

```bash
gcloud pubsub topics get-iam-policy my-topic
```

### Grant Publish Permission

```bash
gcloud pubsub topics add-iam-policy-binding my-topic \
  --member="serviceAccount:my-sa@my-project.iam.gserviceaccount.com" \
  --role="roles/pubsub.publisher"
```

### Test Publish

```bash
gcloud pubsub topics publish my-topic --message="test"
```

### Verify Topic in Different Project

```bash
gcloud pubsub topics list --project=other-project --filter="my-topic"
```

### Create Subscription

```bash
gcloud pubsub subscriptions create my-sub \
  --topic=my-topic \
  --project=my-project
```

### Check Service Account Access

```bash
gcloud iam service-accounts describe my-sa@my-project.iam.gserviceaccount.com
```

## Related Errors

- [GCP IAM Error]({{< relref "/cloud/gcp/gcp-iam-error-v2" >}}) — permission denied
- [GCP Storage Error]({{< relref "/cloud/gcp/gcp-storage-error-v2" >}}) — bucket not found
- [AWS SNS Error]({{< relref "/cloud/aws/aws-sns-error-v2" >}}) — topic not found
