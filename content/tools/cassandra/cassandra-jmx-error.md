---
title: "[Solution] Cassandra JMX Error - Fix JMX Connection Failed"
description: "Fix Cassandra JMX connection failures. Resolve JMX authentication, SSL, and network issues for Cassandra remote management."
tools: ["cassandra"]
error-types: ["jmx-error"]
severities: ["error"]
weight: 5
---

This error means Cassandra's JMX (Java Management Extensions) connection failed. JMX is required for nodetool, monitoring, and remote management operations.

## What This Error Means

When JMX connection fails, you see:

```
Connection refused to JMX service at localhost:7199
# or
Authentication failed for JMX connection
# or
java.rmi.ConnectException: Connection refused to host
```

JMX provides the management interface for Cassandra. Without it, nodetool and monitoring tools cannot communicate with the node.

## Why It Happens

- JMX is disabled in the Cassandra configuration
- The JMX port is not accessible due to firewall rules
- JMX authentication credentials are incorrect
- SSL/TLS configuration is mismatched
- The Cassandra process has not fully started JMX
- Another process is using the JMX port

## How to Fix It

### Verify JMX is enabled

```bash
# cassandra-env.sh or jvm11-server.options
-Dcom.sun.management.jmxremote.port=7199
-Dcom.sun.management.jmxremote.ssl=false
-Dcom.sun.management.jmxremote.authenticate=false
```

### Check if JMX port is listening

```bash
netstat -tlnp | grep 7199
# or
ss -tlnp | grep 7199
```

### Open firewall for JMX

```bash
sudo iptables -A INPUT -p tcp --dport 7190 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 7199 -j ACCEPT
```

### Configure JMX authentication

```bash
# jmxremote.access
cassandra  readwrite

# jmxremote.password
cassandra  cassandra
```

### Connect with credentials

```bash
nodetool -h localhost -p 7199 -u cassandra -pw cassandra status
```

### Enable JMX SSL for production

```bash
# cassandra-env.sh
-Dcom.sun.management.jmxremote.ssl=true
-Dcom.sun.management.jmxremote.ssl.need.client.auth=true
-Djavax.net.ssl.keyStore=/path/to/keystore.jks
-Djavax.net.ssl.trustStore=/path/to/truststore.jks
```

### Check JMX in Cassandra logs

```bash
grep -i "jmx" /var/log/cassandra/system.log
```

Look for JMX startup and error messages.

### Use local JMX for debugging

```bash
# Connect locally without authentication
nodetool -h 127.0.0.1 -p 7199 status
```

### Verify Cassandra is fully started

```bash
nodetool status
```

JMX is not available until Cassandra fully initializes.

### Check for port conflicts

```bash
lsof -i :7199
```

Ensure no other process is using the JMX port.

## Common Mistakes

- Not enabling JMX authentication in production
- Using localhost for remote JMX connections
- Not opening firewall ports for JMX between nodes
- Assuming JMX is available before Cassandra fully starts
- Not using SSL for JMX in production environments

## Related Pages

- [Cassandra Nodetool Error]({{< relref "/tools/cassandra/cassandra-nodetool-error" >}}) -- nodetool failures
- [Cassandra Connection Error]({{< relref "/tools/cassandra/cassandra-connection-error" >}}) -- connectivity issues
- [Cassandra Gossip Error]({{< relref "/tools/cassandra/cassandra-gossip-error" >}}) -- gossip issues
