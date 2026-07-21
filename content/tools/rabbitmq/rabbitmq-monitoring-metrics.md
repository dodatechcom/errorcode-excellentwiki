---
title: "[Solution] RabbitMQ Monitoring Metrics Error"
description: "Fix RabbitMQ monitoring metrics error. Resolve Prometheus and monitoring integration issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Monitoring Metrics Error

Monitoring metrics are not available or incorrect. The metrics endpoint is not configured.

## Common Causes

- Prometheus plugin not enabled
- Metrics endpoint URL is wrong
- Metrics format is incompatible

## How to Fix

### Solution 1

```bash
rabbitmq-plugins list | grep prometheus
```

### Solution 2

```bash
curl http://localhost:15692/metrics
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
