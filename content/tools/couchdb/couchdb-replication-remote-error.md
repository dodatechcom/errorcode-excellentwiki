---
title: "[Solution] CouchDB Replication Remote Error — How to Fix"
description: "Fix CouchDB replication remote errors by resolving remote database connection issues, fixing remote authentication problems, and handling remote database unavailability"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication Remote Error

CouchDB replication remote errors occur when the replicator cannot connect to a remote (external) CouchDB instance during replication.

## Why It Happens

- Remote server is unreachable
- Remote server credentials are invalid
- Remote database does not exist
- Network latency causes timeouts
- Remote server is overloaded
- SSL certificate issues with remote server

## Common Error Messages

```
{ "error": "internal_server_error", "reason": "Remote server unreachable" }
```

```
{ "error": "unauthorized", "reason": "Remote authentication failed" }
```

```
{ "error": "not_found", "reason": "Remote database not found" }
```

```
{ "error": "timeout", "reason": "Remote server timeout" }
```

## How to Fix It

### 1. Test Remote Connection

```bash
# Test remote server
curl -v http://remote-host:5984/

# Test remote database
curl -v -u user:pass http://remote-host:5984/mydb

# Check remote server status
curl http://remote-host:5984/_up
```

### 2. Fix Remote Authentication

```bash
# Test remote authentication
curl -u user:pass http://remote-host:5984/_session

# Use credentials in replication
curl -X PUT http://localhost:5984/_replicator/remote_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "remote_rep",
    "source": {
      "url": "http://remote-host:5984/db",
      "auth": {
        "basic": {
          "username": "replicator",
          "password": "secret"
        }
      }
    },
    "target": "http://localhost:5984/db"
  }'
```

### 3. Fix Network Issues

```bash
# Check network connectivity
ping remote-host

# Check DNS resolution
nslookup remote-host

# Test port connectivity
telnet remote-host 5984

# Check firewall rules
sudo iptables -L -n | grep 5984
```

### 4. Configure Remote Replication

```bash
# Create replication with timeout settings
curl -X PUT http://localhost:5984/_replicator/remote_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "remote_rep",
    "source": "http://remote-host:5984/db",
    "target": "http://localhost:5984/db",
    "connection_timeout": 30000,
    "retries_per_request": 10,
    "worker_processes": 2
  }'
```

## Common Scenarios

- **Remote unreachable**: Check network and firewall settings.
- **Authentication failed**: Verify remote credentials.
- **Remote timeout**: Increase timeout settings and check remote server health.

## Prevent It

- Verify remote connectivity before replication
- Store remote credentials securely
- Monitor remote server health

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Replication Source Error](/tools/couchdb/couchdb-replication-source-error)
- [CouchDB Replication Target Error](/tools/couchdb/couchdb-replication-target-error)
