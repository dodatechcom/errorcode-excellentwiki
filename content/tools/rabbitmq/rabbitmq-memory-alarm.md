---
title: "[Solution] RabbitMQ Memory Alarm Error"
description: "Fix RabbitMQ memory alarm error. Resolve memory usage threshold issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Memory Alarm Error

The memory high watermark alarm is triggered. The broker blocks publishers to prevent OOM.

## Common Causes

- Memory usage exceeds high watermark
- Queues accumulating faster than consumed
- Memory-intensive operations running

## How to Fix

### Solution 1

```bash
rabbitmqctl set_vm_memory_high_watermark.relative 0.6
```

### Solution 2

```bash
rabbitmqctl status
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
