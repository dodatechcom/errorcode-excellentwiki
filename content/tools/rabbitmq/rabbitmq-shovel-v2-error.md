---
title: "[Solution] RabbitMQ Shovel v2 Error"
description: "Fix RabbitMQ shovel v2 errors. Learn why this happens and how to resolve it quickly."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# RabbitMQ Shovel v2 Error

RabbitMQ Shovel v2 errors occur when the modern Shovel plugin fails to replicate messages.

## Why This Happens

- Shovel not running
- Source unreachable
- Destination error
- Protocol mismatch

## Common Error Messages

- `shovel_v2_not_running_error`
- `shovel_v2_source_error`
- `shovel_v2_destination_error`
- `shovel_v2_protocol_error`

## How to Fix It

### Solution 1: Configure Shovel v2

Set up modern shovel:

```bash
rabbitmqctl set_parameter shovel my-shovel \
  '{"src-protocol":"amqp10","src-uri":"amqp://source","src-queue":"myqueue","dest-protocol":"amqp10","dest-uri":"amqp://dest","dest-queue":"myqueue"}'
```

### Solution 2: Check shovel status

Monitor shovel status:

```bash
rabbitmqctl list_shovels
```

### Solution 3: Fix connection issues

Verify source and destination are accessible.


## Common Scenarios

- **Shovel not running:** Check shovel configuration.
- **Source unreachable:** Verify source broker connectivity.

## Prevent It

- Monitor shovel status
- Set up alerts
- Test failover
