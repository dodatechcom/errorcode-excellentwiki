---
title: "[Solution] ScyllaDB JMX Error — How to Fix"
description: "Fix ScyllaDB JMX errors by configuring JMX ports, fixing authentication, and resolving remote JMX connection failures"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB JMX Error

ScyllaDB JMX errors occur when the Java Management Extensions interface fails, preventing nodetool and monitoring tools from communicating with ScyllaDB.

## Why It Happens

- JMX service (scylla-jmx) is not running
- JMX port 7199 is blocked by firewall
- Java is not installed or wrong version
- JMX authentication credentials are incorrect
- Remote JMX access is not enabled
- JMX heap size is too small

## Common Error Messages

```
Connection refused to localhost:7199
```

```
Failed to retrieve RMIServerStub
```

```
java.rmi.ConnectException: Connection refused
```

```
Authentication failed - JMX password incorrect
```

## How to Fix It

### 1. Start JMX Service

```bash
# Check JMX status
sudo systemctl status scylla-jmx

# Start JMX
sudo systemctl start scylla-jmx

# Verify JMX is listening
ss -tlnp | grep 7199

# Check JMX logs
sudo journalctl -u scylla-jmx -n 50
```

### 2. Configure JMX Port

```bash
# Set JMX port in environment
export JMX_PORT=7199
export LOCAL_JMX=yes

# Or configure in /etc/sysconfig/scylla-jmx
JMX_PORT=7199
LOCAL_JMX=yes

# Restart JMX
sudo systemctl restart scylla-jmx
```

### 3. Fix Java Installation

```bash
# Check Java version
java -version

# Install correct Java version
sudo apt install openjdk-11-jdk

# Set JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# Test nodetool (uses JMX)
nodetool version
```

### 4. Enable Remote JMX Access

```bash
# For remote JMX connections
export JMX_OPTS="-Dcom.sun.management.jmxremote=true \
  -Dcom.sun.management.jmxremote.port=7199 \
  -Dcom.sun.management.jmxremote.authenticate=true \
  -Dcom.sun.management.jmxremote.ssl=false"

# Test remote connection
nodetool -h remote_host status
```

## Common Scenarios

- **nodetool cannot connect**: Start the scylla-jmx service.
- **JMX connection refused from monitoring**: Open port 7199 in firewall.
- **JMX OOM error**: Increase JMX heap size with `-Xmx1G`.

## Prevent It

- Ensure scylla-jmx service is enabled and starts with ScyllaDB
- Monitor JMX service health alongside ScyllaDB
- Keep Java version compatible with ScyllaDB requirements

## Related Pages

- [ScyllaDB Nodetool Error](/tools/scylladb/scylladb-nodetool-error)
- [ScyllaDB Node Error](/tools/scylladb/scylladb-node-error)
- [ScyllaDB Monitoring Error](/tools/scylladb/scylladb-monitoring-error)
