---
title: "[Solution] RabbitMQ Headers Exchange Error"
description: "Fix RabbitMQ headers exchange error. Resolve header-based routing issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Headers Exchange Error

Messages in a headers exchange are not routed correctly. Header matching is not working as expected.

## Common Causes

- x-match logic is incorrect (all vs any)
- Headers do not match binding arguments
- Message headers are missing

## How to Fix

### Solution 1

```bash
rabbitmqctl list_bindings
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
