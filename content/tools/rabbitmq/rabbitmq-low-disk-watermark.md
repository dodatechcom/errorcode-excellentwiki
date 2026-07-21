---
title: "[Solution] RabbitMQ Low Disk Watermark Error"
description: "Fix RabbitMQ low disk watermark error. Resolve disk space monitoring issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Low Disk Watermark Error

The disk space is approaching the low watermark. The broker may trigger the disk alarm soon.

## Common Causes

- Disk space is declining
- Large queues filling disk
- Retention policies not set

## How to Fix

### Solution 1

```bash
df -h
```

### Solution 2

```bash
rabbitmqctl status
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
