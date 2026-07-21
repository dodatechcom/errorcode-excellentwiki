---
title: "[Solution] RabbitMQ Free Disk Space Error"
description: "Fix RabbitMQ free disk space error. Resolve disk space exhaustion issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Free Disk Space Error

RabbitMQ has insufficient free disk space. The broker cannot write messages to disk.

## Common Causes

- Disk is full or nearly full
- Mnesia database grown too large
- Message store files consuming disk

## How to Fix

### Solution 1

```bash
df -h
```

### Solution 2

```bash
rabbitmqctl list_queues name messages disk_persistent
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
