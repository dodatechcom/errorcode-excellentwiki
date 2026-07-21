---
title: "[Solution] CouchDB Replication Data Center Error — How to Fix"
description: "Fix CouchDB replication data center errors by resolving cross-data center replication issues, fixing WAN replication problems, and handling geo-distributed replication"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication Data Center Error

CouchDB replication data center errors occur when replicating data between geographically distributed data centers.

## Why It Happens

- High network latency between data centers
- WAN connectivity issues
- Bandwidth limitations
- Firewall blocks cross-data center traffic
- SSL/TLS handshake over WAN is slow
- DNS resolution across data centers fails

## Common Error Messages

```
{ "error": "timeout", "reason": "Data center replication timeout" }
```

```
{ "error": "internal_server_error", "reason": "WAN replication failed" }
```

```
{ "error": "timeout", "reason": "Cross-data center connection timeout" }
```

```
{ "error": "internal_server_error", "reason": "Geo-replication error" }
```

## How to Fix It

### 1. Test Cross-Data Center Connectivity

```bash
# Test latency
ping datacenter2-host

# Test CouchDB connectivity
curl -v http://datacenter2-host:5984/

# Test with timeout
curl --connect-timeout 10 --max-time 30 http://datacenter2-host:5984/mydb
```

### 2. Configure WAN Replication

```bash
# Create replication with WAN-optimized settings
curl -X PUT http://localhost:5984/_replicator/dc_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "dc_rep",
    "source": "http://dc1:5984/db",
    "target": "http://dc2:5984/db",
    "connection_timeout": 60000,
    "heartbeat": 30000,
    "retries_per_request": 20,
    "batch_size": 200,
    "worker_processes": 4
  }'
```

### 3. Optimize for WAN

```bash
# Use compression
curl -X PUT http://localhost:5984/_replicator/dc_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "dc_rep",
    "source": "http://dc1:5984/db",
    "target": "http://dc2:5984/db",
    "create_target": true,
    "continuous": true
  }'

# Use filter to replicate only necessary data
curl -X PUT http://localhost:5984/mydb/_design/dc_filter \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/dc_filter",
    "filters": {
      "important": "function(doc) { return doc.priority === \"high\"; }"
    }
  }'
```

### 4. Monitor WAN Replication

```bash
# Monitor replication progress
while true; do
  curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {docs_written, doc_write_failures, source, target}'
  sleep 60
done
```

## Common Scenarios

- **High latency**: Increase timeouts and use compression.
- **WAN connectivity**: Check firewall and network routing.
- **Bandwidth limitations**: Use filters to replicate only necessary data.

## Prevent It

- Test WAN connectivity before replication
- Use appropriate timeout settings for latency
- Monitor cross-data center replication

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Network Error](/tools/couchdb/couchdb-network-error)
- [CouchDB Cluster Error](/tools/couchdb/couchdb-cluster-error)
