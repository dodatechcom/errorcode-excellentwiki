---
title: "[Solution] RabbitMQ Alarm In Effect Error"
description: "Fix RabbitMQ alarm in effect error. Resolve broker alarm conditions."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Alarm In Effect Error

An alarm is active on the broker, preventing normal operations. The broker may block publishers.

## Common Causes

- Memory high watermark alarm
- Disk free space alarm
- Partition alarm in cluster

## How to Fix

### Solution 1

```bash
rabbitmqctl status
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
