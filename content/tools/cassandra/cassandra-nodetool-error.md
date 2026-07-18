---
title: "[Solution] Cassandra Nodetool Error - Fix Nodetool Command Failed"
description: "Fix Cassandra nodetool command failures. Resolve JMX connection, permission, and nodetool operation errors for Cassandra maintenance."
tools: ["cassandra"]
error-types: ["nodetool-error"]
severities: ["error"]
weight: 5
---

This error means a nodetool command failed to execute. Nodetool is the primary management tool for Cassandra but requires JMX connectivity and proper permissions.

## What This Error Means

When nodetool fails, you see:

```
Failed to connect to JMX at localhost:7199
# or
Operation failed: No live nodes
# or
Error: Could not retrieve node information
```

Nodetool communicates with Cassandra via JMX. Failures indicate connectivity, permission, or operational issues.

## Why It Happens

- JMX is not configured or not running on the node
- The JMX port is not accessible from the nodetool host
- Cassandra is still starting up and not ready for management operations
- Authentication credentials for JMX are incorrect
- The node is down or unreachable
- A previous operation is still in progress

## How to Fix It

### Check JMX configuration

```bash
# cassandra-env.sh or jvm11-server.options
-Dcom.sun.management.jmxremote.port=7199
-Dcom.sun.management.jmxremote.ssl=false
-Dcom.sun.management.jmxremote.authenticate=false
```

### Verify JMX is listening

```bash
netstat -tlnp | grep 7199
# or
ss -tlnp | grep 7199
```

### Start nodetool with correct host

```bash
nodetool -h 127.0.0.1 -p 7199 status
nodetool -h <remote-node-ip> -p 7199 status
```

### Check Cassandra status first

```bash
nodetool status
```

If the node shows `DN` (Down/Normal), it is not responding to management commands.

### Use nodetool with authentication

```bash
nodetool -h localhost -p 7199 -u cassandra -pw cassandra status
```

If JMX authentication is enabled, provide credentials.

### Restart Cassandra if nodetool is unresponsive

```bash
sudo systemctl restart cassandra
```

### Check Cassandra logs

```bash
tail -f /var/log/cassandra/system.log
```

Look for JMX-related errors in the system log.

### Use nodetool for common operations

```bash
nodetool status          # Cluster status
nodetool cleanup keyspace # Remove data not owned by this node
nodetool compact keyspace # Force compaction
nodetool flush keyspace   # Flush memtables to disk
nodetool repair keyspace  # Repair data consistency
```

### Run nodetool on the correct node

```bash
# Run locally on the node
ssh node1
nodetool status

# Or use the correct IP
nodetool -h 10.0.0.1 status
```

## Common Mistakes

- Running nodetool from a different machine without JMX access
- Not waiting for Cassandra to fully start before running nodetool
- Forgetting that JMX authentication may be required in production
- Using nodetool to perform operations that should use CQL
- Not checking JMX port when nodetool hangs without error

## Related Pages

- [Cassandra Connection Error]({{< relref "/tools/cassandra/cassandra-connection-error" >}}) -- connectivity issues
- [Cassandra JMX Error]({{< relref "/tools/cassandra/cassandra-jmx-error" >}}) -- JMX problems
- [Cassandra Unavailable]({{< relref "/tools/cassandra/cassandra-unavailable" >}}) -- availability issues
