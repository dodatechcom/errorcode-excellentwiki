---
title: "[Solution] RabbitMQ Federation Error"
description: "Fix RabbitMQ federation errors. Learn why this happens and how to resolve it quickly."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# RabbitMQ Federation Error

RabbitMQ federation errors occur when federated exchanges or queues fail to sync between brokers.

## Why This Happens

- Federation link down
- Upstream unreachable
- Exchange not federated
- Queue not federated

## Common Error Messages

- `federation_link_error`
- `federation_upstream_error`
- `federation_exchange_error`
- `federation_queue_error`

## How to Fix It

### Solution 1: Configure federation

Set up upstream:

```bash
rabbitmqctl set_parameter federation-upstream my-upstream \
  '{"uri":"amqp://remote-broker"}'
```

### Solution 2: Link exchanges

Federate an exchange:

```bash
rabbitmqctl set_policy federate-exchange "^federated." \
  '{"federation-upstream":"my-upstream"}'
```

### Solution 3: Check federation status

View federation status:

```bash
rabbitmqctl list_federation_links
```


## Common Scenarios

- **Federation link down:** Check the upstream broker.
- **Exchange not federated:** Verify the federation policy.

## Prevent It

- Monitor federation links
- Set up upstream authentication
- Test failover
