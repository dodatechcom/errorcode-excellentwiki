---
title: "[Solution] RabbitMQ Queue Master Balancing Error"
description: "Fix RabbitMQ queue master balancing errors. Resolve uneven master distribution across cluster nodes."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Queue Master Balancing Error

RabbitMQ queue master balancing errors occur when queue masters are unevenly distributed across cluster nodes, causing hot spots and degraded performance.

## Common Causes

- Queue master locator strategy not configured
- Node added to cluster without rebalancing queues
- All queues created on a single node before scaling
- Least-discussed or min-masters strategy misconfigured

## How to Fix It

### Solution 1: Set queue master locator strategy

Configure the master locator policy:

```bash
rabbitmqctl set_policy master-balancing ".*" \
  '{"queue-master-locator": "min-masters"}' \
  --apply-to queues
```

### Solution 2: Rebalance queues using the CLI

Trigger a queue rebalance:

```bash
rabbitmq-queues rebalance
```

### Solution 3: Check master distribution

View queue master distribution:

```bash
rabbitmq-queues list -q name node
```

## Prevent It

- Apply a master locator policy cluster-wide
- Rebalance queues after adding or removing nodes
- Monitor queue distribution with Prometheus metrics
