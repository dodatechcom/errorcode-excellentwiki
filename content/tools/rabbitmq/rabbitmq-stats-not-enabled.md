---
title: "[Solution] RabbitMQ Stats Not Enabled Error"
description: "Fix RabbitMQ stats not enabled error. Resolve statistics collection issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Stats Not Enabled Error

Statistics are not being collected. The management stats are disabled or not functioning.

## Common Causes

- Stats collection is disabled
- Management database is disabled
- Stats emission interval is too high

## How to Fix

### Solution 1

```bash
grep management /etc/rabbitmq/rabbitmq.conf
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
