---
title: "[Solution] MongoDB Connection Timed Out"
description: "Resolve MongoDB connection timeout errors during server selection"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Connection Timed Out Error

A connection timeout occurs when the driver cannot reach the MongoDB server within the expected timeframe:

```
MongoServerSelectionError: connection timed out
```

```
MongoNetworkError: Server selection timed out after 30000 ms
```

## Common Causes

- Network latency between the client and server is too high
- The server is overloaded and cannot accept new connections
- DNS resolution is slow or failing
- The server firewall silently drops packets (no RST sent)
- MongoDB is starting up and not yet ready for connections
- Connection pool is exhausted -- all connections are in use
- VPN or proxy is interfering with the TCP connection
- IPv6 vs IPv4 mismatch

## How to Fix

### 1. Increase the server selection timeout

```javascript
const client = new MongoClient(uri, {
  serverSelectionTimeoutMS: 60000,  // 60 seconds
  connectTimeoutMS: 10000,
  socketTimeoutMS: 20000
});
```

### 2. Check network connectivity

```bash
# Ping the server
ping mongo-host.example.com

# Test the port
nc -zv mongo-host.example.com 27017

# Trace the route
traceroute mongo-host.example.com
```

### 3. Verify DNS resolution

```bash
nslookup mongo-host.example.com
dig mongo-host.example.com

# Try with IP directly to rule out DNS
mongosh --host 10.0.1.50 --port 27017
```

### 4. Check for firewall drops

```bash
# On the server
sudo tcpdump -i eth0 port 27017 -n

# Check iptables
sudo iptables -L -n | grep 27017
```

### 5. Optimize connection pool settings

```javascript
const client = new MongoClient(uri, {
  maxPoolSize: 100,
  minPoolSize: 10,
  waitQueueTimeoutMS: 5000
});
```

## Examples

```bash
# Measure latency to the server
time mongosh --host mongo-host --eval "db.runCommand({ping:1})"

# Check server resource usage
ssh mongo-host "uptime && free -h && df -h"

# Monitor active connections
mongosh --eval "db.serverStatus().connections"

# Test with a simpler query to verify connectivity
mongosh --host mongo-host --eval "db.runCommand({connectionStatus:1})"
```