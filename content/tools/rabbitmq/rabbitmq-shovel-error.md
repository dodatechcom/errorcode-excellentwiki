---
title: "[Solution] RabbitMQ Shovel Error"
description: "Fix RabbitMQ shovel errors. Learn why this happens and how to resolve it quickly."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# RabbitMQ Shovel Error

RabbitMQ shovel errors occur when message forwarding between brokers or exchanges fails.

## Why This Happens

- Shovel not running
- Source unavailable
- Destination unreachable
- Protocol error

## Common Error Messages

- `shovel_not_running`
- `shovel_source_error`
- `shovel_destination_error`
- `shovel_protocol_error`

## How to Fix It

### Solution 1: Configure shovel

Set up a shovel:

```bash
rabbitmqctl set_parameter shovel my-shovel \
  '{"src-protocol":"amqp091","src-uri":"amqp://source","src-queue":"myqueue","dest-protocol":"amqp091","dest-uri":"amqp://dest","dest-queue":"myqueue"}'
```

### Solution 2: Check shovel status

Monitor shovel status:

```bash
rabbitmqctl list_shovels
```

### Solution 3: Fix connection issues

Verify source and destination brokers are accessible.


## Common Scenarios

- **Shovel not running:** Check the shovel configuration.
- **Connection failed:** Verify network connectivity to brokers.

## Prevent It

- Monitor shovel status
- Set up alerts
- Test failover
