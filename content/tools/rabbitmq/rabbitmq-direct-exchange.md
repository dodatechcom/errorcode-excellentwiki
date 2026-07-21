---
title: "[Solution] RabbitMQ Direct Exchange Error"
description: "Fix RabbitMQ direct exchange error. Resolve direct exchange routing issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Direct Exchange Error

Messages in a direct exchange are not routed correctly. The routing key does not match binding keys.

## Common Causes

- Routing key does not exactly match binding key
- No binding exists for routing key
- Exchange type is not direct

## How to Fix

### Solution 1

```bash
rabbitmqctl list_bindings
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
