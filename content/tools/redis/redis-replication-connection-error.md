---
title: "[Solution] Redis Replication Connection Error"
description: "How to fix Redis replication connection errors between master and replica"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Master IP/port changed in replica config
- Firewall blocking replication port
- Master authentication required but replica not configured
- Network unreachable

## Fix

Check replication config:

```bash
redis-cli CONFIG GET replicaof
```

Update replica to point to master:

```bash
redis-cli REPLICAOF master-ip master-port
```

Set master auth password:

```bash
redis-cli CONFIG SET masterauth "master_password"
```

Check connectivity:

```bash
redis-cli -h master-host -p 6379 PING
```

## Examples

```bash
# Check current master
redis-cli INFO replication | grep master_host

# Update master
redis-cli REPLICAOF 192.168.1.100 6379

# Set master auth
redis-cli CONFIG SET masterauth "password123"
```
