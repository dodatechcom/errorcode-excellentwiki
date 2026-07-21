---
title: "[Solution] Kafka ZooKeeper Session Expired Error"
description: "Fix Kafka ZooKeeper session expired errors. Resolve broker disconnection from ZooKeeper ensemble."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka ZooKeeper Session Expired Error

Kafka ZooKeeper session expired errors occur when the broker loses its ZooKeeper session for longer than the session timeout, requiring re-registration of all ephemeral nodes.

## Common Causes

- ZooKeeper ensemble under heavy load or unstable
- Network partition between broker and ZooKeeper
- Session timeout set too low for network conditions
- ZooKeeper server crash or restart during an active session

## How to Fix

1. Check ZooKeeper ensemble health:

```bash
echo ruok | nc localhost 2181
echo stat | nc localhost 2181
```

2. Increase ZooKeeper session timeout in the broker:

```properties
zookeeper.connection.timeout.ms=18000
zookeeper.session.timeout.ms=18000
```

3. Verify ZooKeeper connectivity from the broker:

```bash
echo "get /brokers/ids/0" | nc localhost 2181
```

4. Restart ZooKeeper ensemble nodes one at a time:

```bash
# On each ZK node sequentially
zkServer.sh stop
zkServer.sh start
```

## Examples

```bash
# Check ZooKeeper leader
echo stat | nc localhost 2181 | grep "Leader\|Mode"

# List Kafka's ZooKeeper znodes
echo ls /brokers | nc localhost 2181
echo ls /brokers/ids | nc localhost 2181
```
