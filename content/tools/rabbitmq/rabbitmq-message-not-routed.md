---
title: "[Solution] RabbitMQ Message Not Routed Error"
description: "Fix RabbitMQ message not routed error. Resolve message delivery failures."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Message Not Routed Error

The message is not routed to any queue. The exchange does not have a matching binding.

## Common Causes

- Exchange has no bindings to queues
- Routing key does not match binding key
- Exchange type does not match routing pattern

## How to Fix

### Solution 1

```bash
rabbitmqadmin list bindings
```

### Solution 2

```bash
rabbitmqadmin declare binding source=myexchange destination=myqueue routing_key=mykey
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
