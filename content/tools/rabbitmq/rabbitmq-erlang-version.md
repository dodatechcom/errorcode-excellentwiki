---
title: "[Solution] RabbitMQ Erlang Version Error"
description: "Fix RabbitMQ Erlang version error. Resolve Erlang compatibility issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Erlang Version Error

The Erlang version is not compatible with the RabbitMQ version. Startup fails or features are broken.

## Common Causes

- Erlang version is too old
- Erlang compiled without required features
- Erlang package from incompatible source

## How to Fix

### Solution 1

```bash
rabbitmq-diagnostics erlang_version
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
