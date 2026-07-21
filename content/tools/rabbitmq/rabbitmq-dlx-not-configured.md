---
title: "[Solution] RabbitMQ Dead Letter Exchange Not Configured Error"
description: "Fix RabbitMQ DLX not configured error. Resolve dead lettering setup issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Dead Letter Exchange Not Configured Error

Messages are rejected or expire but no dead-letter exchange is configured. Messages are lost.

## Common Causes

- No dead-letter-exchange on queue
- Dead-letter-exchange does not exist
- Dead-letter routing key not set

## How to Fix

### Solution 1

```bash
rabbitmqadmin declare exchange name=dlx type=fanout
```

### Solution 2

```bash
rabbitmqadmin declare queue name=dlq
```

### Solution 3

```bash
rabbitmqadmin declare binding source=dlx destination=dlq
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
