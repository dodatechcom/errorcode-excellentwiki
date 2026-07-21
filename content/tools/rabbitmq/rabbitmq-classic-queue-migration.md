---
title: "[Solution] RabbitMQ Classic Queue Migration Error"
description: "Fix RabbitMQ classic queue migration error. Resolve queue type migration issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Classic Queue Migration Error

Migration from classic queue to quorum or stream queue fails.

## Common Causes

- Queue cannot be converted in-place
- Queue has messages that block migration
- Properties incompatible with target type

## How to Fix

### Solution 1

```bash
rabbitmqadmin declare queue name=newqueue queue_type=quorum
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
