---
title: "[Solution] RabbitMQ Connection Blocked Error"
description: "Fix RabbitMQ connection blocked error. Resolve memory or disk alarm blocking issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Connection Blocked Error

The broker blocks the connection due to resource alarms (memory or disk). Publish operations are paused.

## Common Causes

- Memory alarm is triggered
- Disk free space alarm is triggered
- Flow control is active

## How to Fix

### Solution 1

```bash
rabbitmqctl status
```

### Solution 2

```bash
rabbitmqctl set_vm_memory_high_watermark.relative 0.6
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
