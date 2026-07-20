---
title: "[Solution] Redis Replication Reconnect Error"
description: "How to fix Redis replication reconnection errors after temporary disconnection"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Master restarted and lost replication state
- Network partition resolved but backlog expired
- Replication ID changed on master

## Fix

Check connection status:

```bash
redis-cli INFO replication | grep master_link_status
```

Force reconnection:

```bash
redis-cli REPLICAOF NO ONE
sleep 1
redis-cli REPLICAOF master-host master-port
```

Increase backlog TTL:

```bash
redis-cli CONFIG SET repl-backlog-ttl 86400
```

Monitor reconnection:

```bash
watch -n 2 'redis-cli INFO replication | grep master_link_status'
```

## Examples

```bash
# Check replication status
redis-cli INFO replication | grep -E "master_link|master_last_io"

# Force full resync
redis-cli REPLICAOF NO ONE
redis-cli REPLICAOF master 6379

# Monitor reconnection
tail -f /var/log/redis/redis-server.log | grep -i replic
```
