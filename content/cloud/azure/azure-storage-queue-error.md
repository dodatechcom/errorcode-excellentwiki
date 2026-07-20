---
title: "[Solution] Azure Storage Queue Error — visibility, poison, and lease failures"
description: "Fix Azure Storage Queue error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 123
---

Storage Queue errors involve messages becoming invisible during processing, poison messages causing infinite loops, or lease conflicts during batch operations.

## Common Causes
- Message visibility timeout expiring before processing completes
- Poison messages exceeding dequeue count without being moved to poison queue
- Storage account key rotation breaking application queue connections
- Queue message size exceeding 64KB limit
- Concurrent dequeue operations causing visibility conflicts

## How to Fix
### Check queue message count
```bash
az storage queue stats \
  --name myQueue \
  --account-name myStorageAccount \
  --account-key myAccountKey
```

### Peek at queue messages
```bash
az storage message peek \
  --queue-name myQueue \
  --account-name myStorageAccount \
  --account-key myAccountKey \
  --num-messages 10
```

### Increase visibility timeout
```bash
az storage message update \
  --queue-name myQueue \
  --account-name myStorageAccount \
  --account-key myAccountKey \
  --message-id myMessageId \
  --pop-receipt myPopReceipt \
  --visibility-timeout 300
```

### Clear all messages in queue
```bash
az storage queue clear \
  --name myQueue \
  --account-name myStorageAccount \
  --account-key myAccountKey
```

## Examples
### Create queue and send message
```bash
az storage queue create \
  --name myQueue \
  --account-name myStorageAccount \
  --account-key myAccountKey
az storage message send \
  --queue-name myQueue \
  --account-name myStorageAccount \
  --account-key myAccountKey \
  --content "Task data"
```

### Delete processed message
```bash
az storage message delete \
  --queue-name myQueue \
  --account-name myStorageAccount \
  --account-key myAccountKey \
  --message-id myMessageId \
  --pop-receipt myPopReceipt
```

## Related Errors
- {{< relref "/cloud/azure/azure-storage-error" >}}
- {{< relref "/cloud/azure/azure-service-bus-error" >}}
- {{< relref "/cloud/azure/azure-functions-error" >}}
