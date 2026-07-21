---
title: "[Solution] RabbitMQ Queue Not Found Error"
description: "Fix RabbitMQ queue not found error. Resolve missing queue issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Queue Not Found Error

The specified queue does not exist. Publishing or consuming from a non-existent queue fails.

## Common Causes

- Queue was never declared
- Queue was deleted by policy or TTL
- Queue name is misspelled

## How to Fix

### Solution 1

```bash
rabbitmqctl list_queues name
```

### Solution 2

```bash
rabbitmqadmin declare queue name=myqueue durable=true
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
