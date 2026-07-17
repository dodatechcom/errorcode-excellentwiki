---
title: "[Solution] Azure Service Bus Error"
description: "Fix Azure Service Bus errors. Resolve Service Bus connectivity and message issues."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

An Azure Service Bus error occurs when messages cannot be sent to or received from Service Bus queues and topics.

## Common Causes

- Namespace does not exist or wrong region
- Connection string is incorrect
- Queue or topic does not exist
- Message size exceeds limit (256KB)
- Shared access policy lacks required permissions

## How to Fix

### Check Namespace

```bash
az servicebus namespace show --name mynamespace --resource-group myRG
```

### Check Queue Status

```bash
az servicebus queue show --namespace-name mynamespace --resource-group myRG \
  --name myqueue
```

### Send Test Message

```bash
az servicebus queue message send --namespace-name mynamespace \
  --queue-name myqueue --body "test message"
```

### Check Shared Access Policy

```bash
az servicebus namespace authorization-rule keys list \
  --namespace-name mynamespace --name RootManageSharedAccessKey
```

### Check Connection String

```bash
az servicebus namespace authorization-rule keys list \
  --namespace-name mynamespace --name RootManageSharedAccessKey \
  --query 'primaryConnectionString'
```

## Examples

```bash
# Example 1: Queue not found
# The messaging entity 'myqueue' could not be found
# Fix: create the queue in Service Bus namespace

# Example 2: Authorization failed
# Put token failed: 401 Unauthorized
# Fix: verify connection string and permissions
```

## Related Errors

- [Azure Event Hub Error]({{< relref "/cloud/azure/azure-event-hub-error" >}}) — Event Hub error
- [Azure Functions Error]({{< relref "/cloud/azure/azure-functions-error" >}}) — Functions error
