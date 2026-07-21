---
title: "[Solution] RabbitMQ Disk Alarm Error"
description: "Fix RabbitMQ disk alarm error. Resolve disk space threshold issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Disk Alarm Error

The disk free space alarm is triggered. The broker blocks publishers to prevent running out of disk space.

## Common Causes

- Disk free space is below limit
- Queues accumulating messages on disk
- Log files consuming too much space

## How to Fix

### Solution 1

```bash
df -h
```

### Solution 2

```bash
rabbitmqctl set_disk_free_limit '2GB'
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
