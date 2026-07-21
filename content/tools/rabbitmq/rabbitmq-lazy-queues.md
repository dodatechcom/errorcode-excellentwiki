---
title: "[Solution] RabbitMQ Lazy Queue Error"
description: "Fix RabbitMQ lazy queue error. Resolve lazy queue configuration issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Lazy Queue Error

Lazy queue configuration is not working as expected. Messages are not being paged to disk.

## Common Causes

- Lazy queue mode is not enabled
- Queue arguments are not set correctly
- Disk I/O is slow causing paging issues

## How to Fix

### Solution 1

```bash
rabbitmqadmin declare queue name=myqueue arguments='{"x-queue-mode":"lazy"}'
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
