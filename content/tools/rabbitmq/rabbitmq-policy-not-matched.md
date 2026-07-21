---
title: "[Solution] RabbitMQ Policy Not Matched Error"
description: "Fix RabbitMQ policy not matched error. Resolve policy application issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Policy Not Matched Error

The policy does not match any queues or exchanges. The policy is not being applied.

## Common Causes

- Policy pattern does not match resources
- Policy priority is too low
- Policy vhost does not match

## How to Fix

### Solution 1

```bash
rabbitmqctl list_policies
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
