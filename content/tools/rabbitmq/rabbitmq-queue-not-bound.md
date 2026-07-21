---
title: "[Solution] RabbitMQ Queue Not Bound Error"
description: "Fix RabbitMQ queue not bound error. Resolve missing queue binding issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Queue Not Bound Error

The queue is not bound to any exchange. Messages published to exchanges may not reach the queue.

## Common Causes

- Queue was never bound to an exchange
- Binding was deleted
- Binding key does not match routing key

## How to Fix

### Solution 1

```bash
rabbitmqctl list_bindings
```

### Solution 2

```bash
rabbitmqadmin declare binding source=myexchange destination=myqueue routing_key=mykey
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
