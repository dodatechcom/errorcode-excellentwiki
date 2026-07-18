---
title: "[Solution] ScyllaDB Nodetool Error — How to Fix"
description: "Fix ScyllaDB nodetool errors by resolving connection failures, fixing permission issues, and recovering from nodetool command timeouts"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Nodetool Error

ScyllaDB nodetool errors occur when the `nodetool` utility fails to communicate with the ScyllaDB process or cannot execute administrative commands.

## Why It Happens

- ScyllaDB process is not running
- JMX/RMI port (7199) is not accessible
- Nodetool cannot connect to local or remote node
- JMX authentication is misconfigured
- Java is not installed or incorrect version
- Memory limit is too low for nodetool operations

## Common Error Messages

```
Failed to connect to 'localhost:7199'
```

```
Error: Connection refused to localhost:7199
```

```
nodetool: Failed to call class: java.lang.OutOfMemoryError
```

```
Error: Unable to retrieve nodetool information
```

## How to Fix It

### 1. Check JMX Connectivity

```bash
# Verify JMX port is listening
ss -tlnp | grep 7199

# Test JMX connection
curl -v localhost:7199

# Check JMX configuration
cat /etc/scylla/scylla.yaml | grep -i jmx
cat /etc/sysconfig/scylla-jmx | grep -i port
```

### 2. Fix JMX Configuration

```bash
# Set JMX port in scylla.yaml
# JMX port is configured in /etc/scylla/scylla.yaml
# or via /etc/sysconfig/scylla-jmx

# Set environment variables
export LOCAL_JMX=yes
export JMX_PORT=7199

# Start ScyllaDB with JMX enabled
sudo systemctl start scylla-server
sudo systemctl start scylla-jmx
```

### 3. Fix Java Issues

```bash
# Check Java version
java -version

# Install Java if missing
sudo apt install default-jdk

# Fix Java memory for nodetool
export JAVA_OPTS="-Xmx1G"

# Test nodetool
nodetool version
nodetool status
```

### 4. Common Nodetool Commands

```bash
# Check node status
nodetool status

# View cluster info
nodetool describecluster

# Run repair
nodetool repair mykeyspace

# Check compaction status
nodetool compactionstats

# View thread pool status
nodetool tpstats

# Clear snapshots
nodetool clearsnapshot --all
```

## Common Scenarios

- **nodetool times out on large tables**: Increase JMX heap size or use `--timeout` flag.
- **Cannot connect to remote node**: Use `nodetool -h <remote_host>` with proper credentials.
- **JMX not started**: Ensure `scylla-jmx` service is running.

## Prevent It

- Keep JMX port accessible only to trusted networks
- Monitor JMX service health alongside ScyllaDB
- Use ScyllaDB Monitoring Stack instead of manual nodetool commands

## Related Pages

- [ScyllaDB Node Error](/tools/scylladb/scylladb-node-error)
- [ScyllaDB JMX Error](/tools/scylladb/scylladb-jmx-error)
- [ScyllaDB Monitoring Error](/tools/scylladb/scylladb-monitoring-error)
