---
title: "[Solution] RabbitMQ Queue TTL Expired Error"
description: "Fix RabbitMQ queue TTL expired error. Resolve queue expiration issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Queue TTL Expired Error

The queue itself has expired and been deleted. The queue x-expires argument caused deletion.

## Common Causes

- x-expires set and queue is idle
- No consumers or publishes happened
- Queue was auto-deleted by TTL

## How to Fix

### Solution 1

```bash
rabbitmqadmin declare queue name=myqueue arguments='{"x-expires":3600000}'
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
