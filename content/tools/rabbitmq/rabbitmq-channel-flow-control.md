---
title: "[Solution] RabbitMQ Channel Flow Control Error"
description: "Fix RabbitMQ channel flow control error. Resolve channel-level flow control issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Channel Flow Control Error

Channel flow control is activated. The broker tells the producer to stop sending messages.

## Common Causes

- Consumer is too slow
- Queue is filling up
- Memory pressure is high

## How to Fix

### Solution 1

```bash
rabbitmqctl list_channels
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
