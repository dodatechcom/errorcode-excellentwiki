---
title: "[Solution] GCP Pub/Sub Error"
description: "Fix GCP Pub/Sub errors. Resolve Pub/Sub messaging issues."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
tags: ["gcp", "pubsub", "pub-sub", "messaging", "topic"]
weight: 5
---

A GCP Pub/Sub error occurs when messages cannot be published to or subscribed from Pub/Sub topics.

## Common Causes

- Topic or subscription does not exist
- IAM permissions not granted for pubsub actions
- Message size exceeds 10MB limit
- Subscription push endpoint is not accessible
- Dead letter topic configuration errors

## How to Fix

### Check Topic

```bash
gcloud pubsub topics describe my-topic
```

### Create Topic

```bash
gcloud pubsub topics create my-topic
```

### Create Subscription

```bash
gcloud pubsub subscriptions create my-sub --topic=my-topic
```

### Publish Message

```bash
gcloud pubsub topics publish my-topic --message="Hello World"
```

### Pull Messages

```bash
gcloud pubsub subscriptions pull my-sub --auto-ack
```

### Check IAM

```bash
gcloud pubsub topics get-iam-policy my-topic
```

## Examples

```bash
# Example 1: Topic not found
# Resource not found: projects/my-project/topics/my-topic
# Fix: create the topic first

# Example 2: Permission denied
# The caller does not have permission
# Fix: add pubsub.topics.publish role
```

## Related Errors

- [AWS SQS Error]({{< relref "/cloud/aws/aws-sqs-error" >}}) — SQS send failed
- [Azure Service Bus Error]({{< relref "/cloud/azure/azure-service-bus-error" >}}) — Service Bus error
