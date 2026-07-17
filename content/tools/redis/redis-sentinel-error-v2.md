---
title: "Redis Sentinel - no master available"
description: "Redis Sentinel cannot find an available master node for the monitored replication group"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A "no master available" error from Redis Sentinel occurs when all Sentinel instances agree that the current master is down but a new master has not been elected or is unreachable. This leaves the replication group without a writable primary node.

## Common Causes

- Master node failed and Sentinel failover has not completed
- Too few Sentinel instances to achieve quorum
- Sentinel configuration mismatch between instances
- Network partition between Sentinel and master
- All replicas also down, no promotion candidate

## How to Fix

1. Check Sentinel status:

```bash
redis-cli -p 26379 SENTINEL masters
redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster
```

2. Verify quorum is achievable:

```bash
# Check all Sentinel instances
redis-cli -p 26379 SENTINEL masters | grep num-other-sentinels
redis-cli -p 26380 SENTINEL masters | grep num-other-sentinels
redis-cli -p 26381 SENTINEL masters | grep num-other-sentinels
```

3. Force a manual failover if needed:

```bash
redis-cli -p 26379 SENTINEL failover mymaster
```

4. Check Sentinel logs for errors:

```bash
tail -50 /var/log/redis/sentinel.log
```

5. Verify Sentinel configuration:

```conf
# sentinel.conf
sentinel monitor mymaster 127.0.0.1 6379 2
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 10000
sentinel parallel-syncs mymaster 1
```

6. Restart the master or promote a replica:

```bash
# If master is recoverable
sudo systemctl start redis-server

# If master is gone, force replica promotion
redis-cli -p 6380 REPLICAOF NO ONE
```

## Examples

```bash
# Error: no master available
$ redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster
(nil)
# No master found - failover not completed

# Fix: check sentinel logs and force failover
$ redis-cli -p 26379 SENTINEL failover mymaster
OK
```

## Related Errors

- [Connection error]({{< relref "/tools/redis/redis-connection-error" >}})
- [Cluster error]({{< relref "/tools/redis/redis-cluster-error" >}})
