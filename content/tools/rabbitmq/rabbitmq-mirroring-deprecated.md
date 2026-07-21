---
title: "[Solution] RabbitMQ Mirroring Deprecated Error"
description: "Fix RabbitMQ mirroring deprecated error. Resolve legacy mirroring migration issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Mirroring Deprecated Error

Queue mirroring is deprecated in favor of quorum queues. Policies using mirroring should be migrated.

## Common Causes

- Mirroring policy is still in use
- Application relies on mirrored queues
- Migration not planned

## How to Fix

### Solution 1

```bash
rabbitmqctl list_policies
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
