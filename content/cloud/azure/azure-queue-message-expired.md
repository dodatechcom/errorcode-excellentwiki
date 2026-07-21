---
title: "[Solution] Azure Queue Message Expired Error"
description: "Fix Azure Queue Storage message expiration errors that cause lost queue messages."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Queue message expiration errors occur when messages are deleted by the time-to-live mechanism before they can be processed. This causes silent data loss in messaging workflows.

## Common Causes

- Time-to-live is set too short for the processing time required
- Message dequeue count exceeds the maximum delivery attempts
- Poison message queue is not configured to capture failed messages
- Message visibility timeout is too short and causes duplicate processing

## How to Fix

### Check queue TTL configuration

```bash
az storage queue show \
  --account-name mystorageaccount \
  --name myqueue \
  --query "properties.messageTimeToLive"
```

### Update queue TTL

```bash
az storage queue update \
  --account-name mystorageaccount \
  --name myqueue \
  --fail-on-existing false \
  --message-ttl 259200
```

### Configure dead letter queue

```bash
az storage queue create \
  --account-name mystorageaccount \
  --name myqueue-poison
```

### Check message expiry

```bash
az storage message peek \
  --account-name mystorageaccount \
  --queue-name myqueue \
  --peek-count 10 \
  --query "[].{Content:content,Inserted:insertedOn,Expires:expiresOn}"
```

## Examples

- Messages disappear from the queue after 7 days because the default TTL is 7 days
- Consumer processes a message but it expires before the delete confirmation
- Poison messages keep reappearing because the max dequeue count is set to 5

## Related Errors

- [Azure Queue Error]({{< relref "/cloud/azure/azure-queue-error" >}}) -- General queue errors.
- [Azure Queue Storage Error]({{< relref "/cloud/azure/azure-queue-storage-error" >}}) -- Queue storage issues.
