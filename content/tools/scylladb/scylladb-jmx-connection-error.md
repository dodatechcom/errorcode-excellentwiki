---
title: "[Solution] ScyllaDB JMX Connection Error — How to Fix"
description: "Fix ScyllaDB JMX connection errors when monitoring tools cannot connect to the JMX management port"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB JMX Connection Error

JMX connection errors occur when ScyllaDB monitoring tools, nodetool, or Scylla Monitoring stack cannot connect to the JMX service for management and metrics.

## Why It Happens

- JMX service is not running or failed to start
- JMX port is not accessible through the firewall
- JMX authentication is configured but credentials are missing
- SSL/TLS certificate for JMX is expired
- Java runtime is not installed or misconfigured

## Common Error Messages

```
javax.management.Connection refused:Connection refused to host: 127.0.0.1:7199
```

```
error: JMX is not enabled for local connections
```

```
nodetool: Failed to connect to JMX at localhost:7199
```

## How to Fix It

### 1. Verify JMX Port is Listening

```bash
ss -tlnp | grep 7199
curl -v telnet://localhost:7199
```

### 2. Start JMX Service

```bash
sudo systemctl start scylla-jmx
sudo systemctl enable scylla-jmx
```

### 3. Configure JMX Authentication

```bash
# In /etc/scylla/scylla-jmx.conf
LOCAL_JMX=yes
if [ "x$LOCAL_JMX" = "xyes" ]; then
  JVM_OPTS="$JVM_OPTS -Dcom.sun.management.jmxremote.authenticate=false"
  JVM_OPTS="$JVM_OPTS -Dcom.sun.management.jmxremote.ssl=false"
fi
```

### 4. Open Firewall for JMX

```bash
sudo firewall-cmd --add-port=7199/tcp --permanent
sudo firewall-cmd --reload
```

## Examples

```
$ nodetool status
error: Failed to connect to JMX at localhost:7199
Is Scylla JMX running?
```

After fix:

```
$ nodetool status
Datacenter: dc1
===============
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address    Load       Tokens  Owns    Host ID
UN  10.0.0.1   1.23 GB    256     33.3%   abc-123
```

## Prevent It

- Enable scylla-jmx service at boot
- Monitor JMX port availability
- Keep Java runtime updated for JMX compatibility

## Related Pages

- [ScyllaDB JMX Error](/tools/scylladb/scylladb-jmx-error)
- [ScyllaDB Monitoring Error](/tools/scylladb/scylladb-monitoring-error)
- [ScyllaDB Nodetool Error](/tools/scylladb/scylladb-nodetool-error)
