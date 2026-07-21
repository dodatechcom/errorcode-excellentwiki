---
title: "[Solution] RabbitMQ basic.return Error"
description: "Fix RabbitMQ basic.return error. Resolve unroutable message return issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ basic.return Error

The broker returns a message that could not be routed to any queue. The message is returned to the producer.

## Common Causes

- No queue bound with matching routing key
- Mandatory flag set and message unroutable
- Exchange type does not route expected

## How to Fix

### Solution 1

```bash
rabbitmqctl list_bindings
```

### Solution 2

```bash
rabbitmqctl list_exchanges
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
