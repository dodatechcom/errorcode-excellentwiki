---
title: "[Solution] RabbitMQ Mandatory Flag Error"
description: "Fix RabbitMQ mandatory flag error. Resolve mandatory message delivery issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Mandatory Flag Error

Messages published with mandatory flag are returned because they cannot be routed to any queue.

## Common Causes

- No queue bound with matching routing key
- Exchange type does not support routing pattern
- Queue deleted after binding

## How to Fix

### Solution 1

```bash
rabbitmqctl list_bindings
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
