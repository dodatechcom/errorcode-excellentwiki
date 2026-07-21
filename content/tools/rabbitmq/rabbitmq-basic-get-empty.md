---
title: "[Solution] RabbitMQ basic.get Empty Error"
description: "Fix RabbitMQ basic.get empty error. Resolve empty queue polling issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ basic.get Empty Error

The basic.get request returns no messages. The queue is empty or all messages have been consumed.

## Common Causes

- Queue has no messages
- Messages consumed by other consumers
- Message TTL expired all messages

## How to Fix

### Solution 1

```bash
rabbitmqctl list_queues name messages
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
