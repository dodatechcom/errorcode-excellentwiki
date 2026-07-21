---
title: "[Solution] Kafka Broker ID Duplicate Error"
description: "Fix Kafka broker ID duplicate errors. Resolve conflicts when two brokers use the same broker.id."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Broker ID Duplicate Error

Kafka broker ID duplicate errors occur when two or more brokers in the same cluster are configured with the same broker.id value, preventing the cluster from electing a valid controller.

## Common Causes

- Copying server.properties without updating broker.id
- Automated provisioning script assigning duplicate IDs
- Manual configuration error during cluster scaling

## How to Fix

1. Check the current broker ID setting:

```bash
grep 'broker.id' /etc/kafka/server.properties
```

2. Assign a unique broker.id to each node:

```properties
broker.id=3
```

3. Verify broker IDs across the cluster:

```bash
for node in broker1 broker2 broker3; do
  echo "$node: $(ssh $node grep 'broker.id' /etc/kafka/server.properties)"
done
```

4. Restart the broker after changing the ID:

```bash
kafka-server-stop.sh
kafka-server-start.sh -daemon /etc/kafka/server.properties
```

## Examples

```bash
# List all brokers in the cluster
kafka-metadata.sh --snapshot /var/kafka-logs/__cluster_metadata-0/00000000000000000000.log \
  --cluster-id $(cat /var/kafka-logs/meta.properties | grep cluster.id | cut -d= -f2)
```
