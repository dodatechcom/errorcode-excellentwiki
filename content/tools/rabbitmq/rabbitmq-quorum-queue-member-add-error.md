---
title: "[Solution] RabbitMQ Quorum Queue Member Add Error"
description: "Fix RabbitMQ quorum queue member add errors. Resolve failures adding members to quorum queues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Quorum Queue Member Add Error

RabbitMQ quorum queue member add errors occur when the cluster cannot add a new member to a quorum queue due to node unavailability or membership limits.

## Common Causes

- Target node is down or unreachable from the leader
- Quorum queue already has the maximum number of members
- Node is not part of the same Erlang cluster
- Raft log replication cannot keep up with the new member

## How to Fix It

### Solution 1: Check quorum queue status

View current members:

```bash
rabbitmqctl list_queues -q name members leader pid
```

### Solution 2: Add a member via CLI

Add a member to the quorum queue:

```bash
rabbitmq-queues add_member quorum-queue-1 node3@rabbit
```

### Solution 3: Ensure all nodes are clustered

Check cluster status:

```bash
rabbitmqctl cluster_status
```

## Prevent It

- Ensure all nodes are healthy before adding quorum queue members
- Monitor quorum queue membership regularly
- Use the rebalance command after scaling the cluster
