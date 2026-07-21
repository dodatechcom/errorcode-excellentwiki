---
title: "[Solution] RabbitMQ Exchange Not Found Error"
description: "Fix RabbitMQ exchange not found error. Resolve missing exchange issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Exchange Not Found Error

The specified exchange does not exist. Publishing to a non-existent exchange fails.

## Common Causes

- Exchange was never declared
- Exchange was deleted
- Exchange name is misspelled

## How to Fix

### Solution 1

```bash
rabbitmqctl list_exchanges
```

### Solution 2

```bash
rabbitmqadmin declare exchange name=myexchange type=direct durable=true
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
